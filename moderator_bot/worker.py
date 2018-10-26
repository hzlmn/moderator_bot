import pickle

import numpy as np

_model = None


def warm(model_path):
    global _model
    if _model is None:
        with model_path.open('rb') as fp:
            pipeline = pickle.load(fp)
            _model = pipeline
    return True


def predict(message):
    results = _model.predict_proba([message])
    return np.array(results).T[1].tolist()
