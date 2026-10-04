# Automated Model Retraining System

Level: 11 — ML Engineering

Skills: Python, drift and freshness gates

Retrain is recommended when drift is true or age_days > 30. It does not launch training.

```bash
pip install -r requirements.txt
pytest -q
```

This is a local laptop proof. It does not call a hosted model and it does not apply production changes.
