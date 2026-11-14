# FreshCart Pipelines

Data Engineering assignment: From Git to Gold.

## Project structure
- `elt/`: FreshCart ELT notebook and SQL assets.
- `iris_project/`: Mage-style Iris machine-learning pipeline.
- `stream/`: RabbitMQ dispatcher and driver scripts.
- `tests/`: Automated tests.
- `.github/workflows/ci.yml`: GitHub Actions CI workflow.

## Local setup
```bash
python -m venv .venv
# Windows: .venv\Scripts\activate
# macOS/Linux: source .venv/bin/activate
pip install -r requirements.txt
pytest -q
```
