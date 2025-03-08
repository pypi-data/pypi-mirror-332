import math
import random

import pytest

from entmoot import Enting, GurobiOptimizer, ProblemConfig
from entmoot.benchmarks import (
    build_multi_obj_categorical_problem,
    eval_multi_obj_cat_testfunc,
)
from entmoot.models.model_params import (
    EntingParams,
    TrainParams,
    TreeTrainParams,
    UncParams,
)


def get_leaf_center(bnds):
    return [
        (b[0] + b[1]) / 2 if not isinstance(b, set) else random.choice(list(b))
        for b in bnds
    ]


def run_gurobi(rnd_seed, n_obj, params, params_opt, num_samples=20, no_cat=False):
    # define benchmark problem
    problem_config = ProblemConfig(rnd_seed=rnd_seed)
    build_multi_obj_categorical_problem(problem_config, n_obj=n_obj, no_cat=no_cat)

    # sample data
    rnd_sample = problem_config.get_rnd_sample_list(num_samples=num_samples)
    testfunc_evals = eval_multi_obj_cat_testfunc(rnd_sample, n_obj=n_obj, no_cat=no_cat)

    # build model
    enting = Enting(problem_config, params=params)
    enting.fit(rnd_sample, testfunc_evals)

    # solve gurobi
    opt = GurobiOptimizer(problem_config, params=params_opt)

    x_sol, obj, mu, unc, leafs = opt.solve(enting)

    # predict enting model with solution
    x_sol_enc = problem_config.encode([x_sol])

    leaf_bnd = [
        enting.leaf_bnd_predict(f"obj_{obj}", opt.get_active_leaf_sol()[obj])
        for obj in range(n_obj)
    ]

    leaf_mid = [get_leaf_center(b) for b in leaf_bnd]

    mu_pred = [enting.mean_model.predict([m])[0][i] for i, m in enumerate(leaf_mid)]
    unc_pred = enting.unc_model.predict([x_sol_enc])[0]

    # compare model mean and uncertainty to prediction
    for m_opt, m_pred in zip(mu, mu_pred):
        assert math.isclose(
            m_opt, m_pred, abs_tol=1e-4
        ), f"`{m_opt}` and `{m_pred}` tree values are too small to test"

    assert (
        unc > 0.001 and unc_pred > 0.001
    ), f"`{unc}` and `{unc_pred}` are too small to test"
    assert math.isclose(
        unc, unc_pred, abs_tol=0.001
    ), f"`{unc}` and `{unc_pred}` unc values are not the same"


@pytest.mark.parametrize("dist_metric", ["l1", "l2", "euclidean_squared"])
@pytest.mark.parametrize("cat_metric", ["overlap", "of", "goodall4"])
@pytest.mark.parametrize("acq_sense", ["exploration"])
@pytest.mark.parametrize("rnd_seed", [100, 101, 102])
@pytest.mark.parametrize("n_obj", [1, 2])
def test_gurobi_consistency1(rnd_seed, n_obj, acq_sense, dist_metric, cat_metric):
    # define model params
    params = EntingParams(
        unc_params=UncParams(
            dist_metric=dist_metric,
            acq_sense=acq_sense,
            dist_trafo="normal",
            cat_metric=cat_metric,
        )
    )
    params_opt = {"LogToConsole": 1, "MIPGap": 0}
    run_gurobi(rnd_seed, n_obj, params, params_opt, num_samples=200)


@pytest.mark.parametrize("dist_metric", ["l1", "euclidean_squared"])
@pytest.mark.parametrize("cat_metric", ["overlap", "of", "goodall4"])
@pytest.mark.parametrize("acq_sense", ["penalty"])
@pytest.mark.parametrize("rnd_seed", [100, 101, 102])
@pytest.mark.parametrize("n_obj", [1, 2])
def test_gurobi_consistency2(rnd_seed, n_obj, acq_sense, dist_metric, cat_metric):
    # define model params
    params = EntingParams(
        unc_params=UncParams(
            dist_metric=dist_metric,
            acq_sense=acq_sense,
            dist_trafo="normal",
            cat_metric=cat_metric,
        )
    )
    params.unc_params.beta = 0.05
    params_opt = {"LogToConsole": 1, "MIPGap": 0}

    run_gurobi(rnd_seed, n_obj, params, params_opt, num_samples=300)


@pytest.mark.parametrize("dist_metric", ["l2"])
@pytest.mark.parametrize("cat_metric", ["overlap", "of", "goodall4"])
@pytest.mark.parametrize("acq_sense", ["penalty"])
@pytest.mark.parametrize("rnd_seed", [100, 101, 102])
@pytest.mark.parametrize("n_obj", [1, 2])
def test_gurobi_consistency3(rnd_seed, n_obj, acq_sense, dist_metric, cat_metric):
    # define model params
    params = EntingParams(
        unc_params=UncParams(
            dist_metric=dist_metric,
            acq_sense=acq_sense,
            dist_trafo="normal",
            cat_metric=cat_metric,
        ),
        # make tree model smaller to reduce testing time
        tree_train_params=TreeTrainParams(
            train_lib="lgbm",
            train_params=TrainParams(
                objective="regression",
                metric="rmse",
                boosting="gbdt",
                num_boost_round=2,
                max_depth=2,
                min_data_in_leaf=1,
                min_data_per_group=1,
                verbose=-1,
            ),
        ),
    )

    params.unc_params.beta = 0.05
    params_opt = {"LogToConsole": 1}

    if n_obj == 1:
        params_opt["MIPGap"] = 0
    else:
        # gurobi takes a long time to fully prove optimality here
        params_opt["MIPGapAbs"] = 0.001

    run_gurobi(rnd_seed, n_obj, params, params_opt, num_samples=300)


@pytest.mark.parametrize("dist_metric", ["l1", "l2", "euclidean_squared"])
@pytest.mark.parametrize("acq_sense", ["exploration"])
@pytest.mark.parametrize("rnd_seed", [100, 101, 102])
def test_gurobi_consistency4(rnd_seed, acq_sense, dist_metric):
    params = EntingParams(
        unc_params=UncParams(
            dist_metric=dist_metric,
            acq_sense=acq_sense,
            dist_trafo="standard",
        )
    )

    params.unc_params.beta = 0.1
    params_opt = {"LogToConsole": 1, "MIPGap": 1e-5}

    run_gurobi(rnd_seed, 1, params, params_opt, num_samples=20, no_cat=True)


@pytest.mark.parametrize("dist_metric", ["l1", "euclidean_squared"])
@pytest.mark.parametrize("acq_sense", ["penalty"])
@pytest.mark.parametrize("rnd_seed", [100, 101, 102])
def test_gurobi_consistency5(rnd_seed, acq_sense, dist_metric):
    params = EntingParams(
        unc_params=UncParams(
            dist_metric=dist_metric,
            acq_sense=acq_sense,
            dist_trafo="standard",
        )
    )
    params.unc_params.beta = 0.1
    params_opt = {"LogToConsole": 1, "MIPGap": 1e-5}

    run_gurobi(rnd_seed, 1, params, params_opt, num_samples=200, no_cat=True)


@pytest.mark.parametrize("dist_metric", ["l2"])
@pytest.mark.parametrize("acq_sense", ["penalty"])
@pytest.mark.parametrize("rnd_seed", [100, 101, 102])
def test_gurobi_consistency6(rnd_seed, acq_sense, dist_metric):
    params = EntingParams(
        unc_params=UncParams(
            dist_metric=dist_metric,
            acq_sense=acq_sense,
            dist_trafo="standard",
        )
    )
    params.unc_params.beta = 0.05
    params_opt = {"LogToConsole": 1, "MIPGapAbs": 0.01}

    run_gurobi(rnd_seed, 1, params, params_opt, num_samples=200, no_cat=True)
