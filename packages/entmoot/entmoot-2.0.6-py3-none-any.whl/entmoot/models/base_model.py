class BaseModel:
    def __init__(self, problem_config, num_obj, params):
        raise NotImplementedError()

    def predict(self, X):
        raise NotImplementedError()

    def fit(self, X, y):
        raise NotImplementedError()

    def add_to_gurobipy_model(self, model_core):
        raise NotImplementedError()

    def add_to_pyomo_model(self, model_core):
        raise NotImplementedError()
