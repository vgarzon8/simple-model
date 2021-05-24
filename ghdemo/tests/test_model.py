# Test cases for model training functions

import pytest
import pandas as pd
import numpy as np
from sklearn.datasets import make_classification
from ghdemo.model import train_model

# Constants
Y_CHECK = np.array([1, 1, 0, 1, 1, 0, 0, 1, 1, 0])
TEST_SIZE = 0.3
N_ESTIM = 5
SEED = 991


@pytest.fixture
def simple_data():
    _X, _y = make_classification(
        n_samples=10, n_features=4, n_informative=2, random_state=SEED
    )
    df = pd.DataFrame(_X)
    df["target"] = _y
    return df


def test_train_model_random_forest(simple_data):
    # Test model training with random forest method
    est = train_model(
        simple_data,
        "target",
        classifier="random_forest",
        test_size=TEST_SIZE,
        n_estimators=N_ESTIM,
        seed=SEED,
    )
    y_pred = est.predict(simple_data.drop(columns=["target"]))
    np.testing.assert_array_equal(y_pred, Y_CHECK)


def test_train_model_gradient_boost(simple_data):
    # Test model training with gradient boosting method
    est = train_model(
        simple_data,
        "target",
        classifier="gradient_boost",
        test_size=TEST_SIZE,
        n_estimators=N_ESTIM,
        seed=SEED,
    )
    y_pred = est.predict(simple_data.drop(columns=["target"]))
    np.testing.assert_array_equal(y_pred, Y_CHECK)


def test_train_model_classifier(simple_data):
    # Test model training rises ValueError for unrecognized classifier
    with pytest.raises(ValueError):
        _ = train_model(
            simple_data,
            "target",
            classifier="_other_",
        )
