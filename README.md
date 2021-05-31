# simple-model

Simple model to demo Git / GitHub workflows

- UCLA Graduate school data set
  - 400 samples, 3 features, 3 classes
- Data queried from a PostgreSQL database
- Random forest or gradient boosting classifier
- YAML configuration files for training and prediction
- Simple command-line interface
- Simple model serialization (Pickle files)
- Prediction using serialized model and data from configurable table

## Modules

`ghdemo`: Simple module with command line interface for classification model.

`tests`: Unit tests

## Environment

### Docker container

- `make build`: to create image
- `make dev`: to start

### Local install

See [ghdemo/README.md](ghdemo/README.md)

## Config file examples

### Train

```yaml
db_param:
    config_file: secrets/toydb.yml
    table_name: uclagrad

train_param:
    target: admit
    classifier: random_forest
    n_estimators: 10
    test_size: 0.3
    seed: 997

model_file: models/rfc-210521-0858.pkl
```

### Predict

```yaml
db_param:
    config_file: secrets/toydb.yml
    table_name: uclagrad_pred

model_file: models/rfc-210521-0858.pkl
```

### PostgreSQL database config file

#### Running on host

```yaml
drivername: postgresql
database: <database name>
username: <user name>
password: <password>
host: <host>
port: 5432
```

#### Docker container with database running on host

macOS: Replace host IP address with `host.docker.internal`
