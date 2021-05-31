## Module example for GitHub demo

### Environment setup

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

Use `requirements-dev.txt` for development environment.
