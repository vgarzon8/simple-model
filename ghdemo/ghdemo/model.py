# Training and prediction functions

from sklearn.model_selection import train_test_split
from sklearn.metrics import classification_report
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

    idx_train, idx_test = train_test_split(
        df.index, test_size=test_size, stratify=df[target], random_state=seed
    )

    X_train = df.drop(columns=target).loc[idx_train].values
    y_train = df[target].loc[idx_train].values

    X_test = df.drop(columns=target).loc[idx_test].values
    y_test = df[target].loc[idx_test].values

    if classifier == "random_forest":
        est = RandomForestClassifier(n_estimators=n_estimators, random_state=seed)
    elif classifier == "gradient_boost":
        est = GradientBoostingClassifier(n_estimators=n_estimators, random_state=seed)
    else:
        logging.error(f"Classifier {classifier} not implemented")
        raise ValueError(classifier)

    est.fit(X_train, y_train)

    y_pred_train = est.predict(X_train)
    y_pred_test = est.predict(X_test)

    logging.debug(classification_report(y_train, y_pred_train))
    logging.info(classification_report(y_test, y_pred_test))

    return est
