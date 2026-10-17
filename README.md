# FraudGuard — UPI Fraud Detection System

FraudGuard is a Django & Machine Learning based fraud detection platform designed to predict and flag fraudulent UPI transactions in real-time.

## Project Structure
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
└── requirements.txt
```

## Team Setup Instructions

### 1. Clone the repository
```bash
git clone <repo-url>
cd fraudguard
```

### 2. Set up virtual environment
```bash
# Windows
python -m venv venv
venv\Scripts\activate

# macOS / Linux
python3 -m venv venv
source venv/bin/activate
```

### 3. Install dependencies
```bash
pip install -r requirements.txt
```

### 4. Configure environment variables
Copy `.env.example` to `.env` and fill in your MySQL credentials:
```bash
# Windows
copy .env.example .env

# macOS / Linux
cp .env.example .env
```

### 5. Create MySQL Database
```sql
CREATE DATABASE fraudguard CHARACTER SET utf8mb4 COLLATE utf8mb4_unicode_ci;
```

### 6. Run Migrations & Start Server
```bash
python manage.py migrate
python manage.py runserver
```

Open `http://127.0.0.1:8000/` in your browser.
