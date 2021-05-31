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

## Module example for GitHub demo

### Setup

1. Create conda environment
2. Activate environment
3. Install requirements
4. Install package in development mode (edit)

```bash
conda create -y -n simple python=3.8.10 && \
    conda activate simple && \
    pip install -r requirements.txt && \
    pip install -e . --no-deps
```
