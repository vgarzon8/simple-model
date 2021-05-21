# Command line interface functions

import logging

logger = logging.getLogger(__name__)


def train(cfg):
    """Train and persist model
    Args:
        cfg (dict): Configuration settings
    """

    import pickle
    from yaml import safe_load
    from ghdemo.data import DataHandler
    from ghdemo.model import train_model

    logging.info("*** Train Model ***")
    logging.debug(cfg)

    db_config_file = cfg["db_param"]["config_file"]
    table_name = cfg["db_param"]["table_name"]

    with open(db_config_file, "r") as fh:
        db_config = safe_load(fh.read())

    dh = DataHandler(db_config)
    df = dh.read_table(table_name)

    est = train_model(df, **cfg["train_param"])

    # Persist model to file
    model_file = cfg["model_file"]
    buf = pickle.dumps(est)

    logging.info(f"Saving model to file {model_file}")
    with open(model_file, "wb") as fh:
        fh.write(buf)

    return None


def predict(cfg):

    import pickle
    from yaml import safe_load
    from ghdemo.data import DataHandler

    logging.info("*** Predict with Model ***")

    db_config_file = cfg["db_param"]["config_file"]
    table_name = cfg["db_param"]["table_name"]
    model_file = cfg["model_file"]

    with open(db_config_file, "r") as fh:
        db_config = safe_load(fh.read())

    dh = DataHandler(db_config)
    df = dh.read_table(table_name)

    with open(model_file, "rb") as fh:
        buf = fh.read()

    est = pickle.loads(buf)

    y_pred = est.predict(df.values)

    print(y_pred)

    return None


def main():
    import argparse
    from yaml import safe_load
    from pathlib import Path

    parser = argparse.ArgumentParser(description="Example model for GitHub demo")
    parser.add_argument("action", help="Actions names")
    parser.add_argument("config_file", default="config.yml", help="Config YAML file")
    parser.add_argument(
        "--verbose",
        "-v",
        action="count",
        help="Increase output verbosity",
        default=0,
    )
    args = parser.parse_args()

    # Setup logging
    if args.verbose > 1:
        log_level = logging.DEBUG
    elif args.verbose > 0:
        log_level = logging.INFO
    else:
        log_level = logging.WARN

    logging.basicConfig(
        level=log_level,
        format="%(asctime)s|%(levelname)s|%(funcName)s: %(message)s",
        datefmt="%y%m%d%H%M%S",
    )

    # Read config file
    p_config = Path(args.config_file)
    assert p_config.exists(), "Config file not found"
    with open(p_config) as f:
        cfg = safe_load(f.read())

    if args.action == "train":
        train(cfg)
    elif args.action == "predict":
        predict(cfg)
    else:
        logging.error(f"Action {args.action} not implemented")
        raise ValueError(args.action)

    return None


if __name__ == "__main__":

    main()
