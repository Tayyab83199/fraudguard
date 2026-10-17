# ml/predictor.py
# Loads the trained model and provides a predict() function.
# The model artifact (model.joblib) is created in Part 2 (Google Colab)
# and placed in ml/artifacts/ before running the server.

import os
import json
import joblib
import numpy as np

ARTIFACTS_DIR = os.path.join(os.path.dirname(__file__), "artifacts")
MODEL_PATH = os.path.join(ARTIFACTS_DIR, "model.joblib")
META_PATH = os.path.join(ARTIFACTS_DIR, "meta.json")

_model = None
_meta = None


def _load():
    global _model, _meta
    if _model is None:
        _model = joblib.load(MODEL_PATH)
    if _meta is None:
        with open(META_PATH, "r") as f:
            _meta = json.load(f)


def predict(features: dict) -> dict:
    """
    Accept a dict of raw feature values, return fraud probability and label.

    Args:
        features: dict mapping feature names to values

    Returns:
        dict with keys: probability (float), is_fraud (bool)
    """
    _load()

    feature_names = _meta.get("features", _meta.get("feature_names", []))
    X = np.array([[features[col] for col in feature_names]])

    prob = float(_model.predict_proba(X)[0][1])
    raw_thresh = _meta.get("recommended_threshold", _meta.get("threshold", 0.5))
    threshold = raw_thresh / 100.0 if raw_thresh > 1.0 else raw_thresh
    is_fraud = prob >= threshold

    return {"probability": prob, "is_fraud": is_fraud, "threshold": threshold}
