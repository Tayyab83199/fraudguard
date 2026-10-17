# FraudGuard — UPI Fraud Detection System

FraudGuard is a Django & Machine Learning based fraud detection platform designed to predict and flag fraudulent UPI transactions in real-time.

> 👥 **Team Members:** Please check the [Team Member Onboarding & Setup Guide (TEAM_SETUP_GUIDE.md)](TEAM_SETUP_GUIDE.md) for full setup instructions, Git workflow, and troubleshooting.

---

## 📁 Project Structure
```
fraudguard/
├── config/               # Django project settings & URL routing
├── core/                 # Auth, core dashboard pages, analytics API
├── transactions/         # Transaction model & scoring API
├── alerts/               # FraudAlert, ModelMetric & alert notifications
├── ml/
│   ├── predictor.py      # Inference pipeline
│   └── artifacts/        # Model artifacts (model.joblib, meta.json)
├── notebooks/            # Colab training notebooks
├── templates/            # HTML templates
├── static/               # CSS, JS, and image assets
├── .env.example          # Environment variable template
├── manage.py
├── requirements.txt
└── TEAM_SETUP_GUIDE.md   # Step-by-step setup guide for team members
```

---

## Quick Start (Summary)

```bash
git clone https://github.com/Wasil728/fraudguard.git
cd fraudguard

# Virtual environment
python -m venv venv
venv\Scripts\activate   # Mac/Linux: source venv/bin/activate

# Install requirements
pip install -r requirements.txt

# Environment variables
copy .env.example .env  # Mac/Linux: cp .env.example .env

# Database & Migrations (Create DB 'fraudguard' in MySQL first)
python manage.py migrate
python manage.py createsuperuser
python manage.py runserver
```

For full details, see **[TEAM_SETUP_GUIDE.md](TEAM_SETUP_GUIDE.md)**.
