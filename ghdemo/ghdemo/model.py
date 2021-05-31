# Training and prediction functions

from sklearn.model_selection import train_test_split
from sklearn.metrics import f1_score
from sklearn.ensemble import RandomForestClassifier, GradientBoostingClassifier
import logging

logger = logging.getLogger(__name__)


def train_model(
    df, target, classifier="random_forest", test_size=0.3, n_estimators=10, seed=None
):
    """Train simple classifer model

    Args:
        df (pandas.DataFrame): Features and target in a single data frame
        target (str): Target column name
        classifier (str): Classifier algorithm, choices: "random_forest",
            "gradient_boost"
        test_size (float): Test split, default: 0.3
        n_estimators (int): Number of estimators, default: 10
        seed (int): Random state, default: None

    Returns:
        sklearn_estimator: Estimator fit to data
    """

    # Supported classifiers
    CLASSIF = {
        "random_forest": RandomForestClassifier,
        "gradient_boost": GradientBoostingClassifier,
    }

    idx_train, idx_test = train_test_split(
        df.index, test_size=test_size, stratify=df[target], random_state=seed
    )

    X_train = df.drop(columns=target).loc[idx_train].values
    y_train = df[target].loc[idx_train].values

    X_test = df.drop(columns=target).loc[idx_test].values
    y_test = df[target].loc[idx_test].values

    try:
        est = CLASSIF[classifier](n_estimators=n_estimators, random_state=seed)
    except KeyError as err:
        logging.error(f"Classifier {err} not implemented. Choices: f{CLASSIF.keys()}")
        raise err

    est.fit(X_train, y_train)
    y_pred_train = est.predict(X_train)
    y_pred_test = est.predict(X_test)

    # Calculate f1 metric
    f1 = {
        _lbl: {_pos: f1_score(_y_true, _y_pred, pos_label=_pos) for _pos in (0, 1)}
        for _lbl, (_y_true, _y_pred) in {
            "train": (y_train, y_pred_train),
            "test": (y_test, y_pred_test),
        }.items()
    }

    logging.debug(f"train f1_0: {f1['train'][0]:5.3f} f1_1: {f1['train'][1]:5.3f}")
    logging.info(f"test f1_0: {f1['test'][0]:5.3f} f1_1: {f1['test'][1]:5.3f}")

    return est
