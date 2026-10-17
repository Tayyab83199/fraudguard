# 🚀 FraudGuard — Team Member Onboarding & Setup Guide

Welcome to the **FraudGuard** team! Follow this step-by-step guide to get the project running on your computer and start contributing.

---

## 📋 Table of Contents
1. [Prerequisites](#1-prerequisites)
2. [Step-by-Step Setup](#2-step-by-step-setup)
   - [Step 1: Clone the Repository](#step-1-clone-the-repository)
   - [Step 2: Create and Activate Virtual Environment](#step-2-create-and-activate-virtual-environment)
   - [Step 3: Install Dependencies](#step-3-install-dependencies)
   - [Step 4: Configure Environment Variables (.env)](#step-4-configure-environment-variables-env)
   - [Step 5: Set Up the MySQL Database](#step-5-set-up-the-mysql-database)
   - [Step 6: Place the ML Model Artifacts](#step-6-place-the-ml-model-artifacts)
   - [Step 7: Apply Migrations & Create Superuser](#step-7-apply-migrations--create-superuser)
   - [Step 8: Start the Development Server](#step-8-start-the-development-server)
3. [Git Workflow for Team Members](#3-git-workflow-for-team-members)
4. [Troubleshooting & Common Issues](#4-troubleshooting--common-issues)

---

## 1. Prerequisites

Make sure you have the following installed on your laptop before starting:

* **Python 3.11, 3.12, or 3.13** ([Download Python](https://www.python.org/downloads/))  
  *(⚠️ Check **"Add python.exe to PATH"** during installation)*
* **Git** ([Download Git](https://git-scm.com/downloads))
* **MySQL Server 8.0+** & **MySQL Workbench** ([Download MySQL Installer](https://dev.mysql.com/downloads/installer/))
* **VS Code** ([Download VS Code](https://code.visualstudio.com/))

---

## 2. Step-by-Step Setup

### Step 1: Clone the Repository

Open your terminal (PowerShell, Command Prompt, or Terminal on Mac) and run:

```bash
git clone https://github.com/Wasil728/fraudguard.git
cd fraudguard
```

Open the project in VS Code:
```bash
code .
```

---

### Step 2: Create and Activate Virtual Environment

A virtual environment ensures your libraries don't clash with other projects.

#### **On Windows (PowerShell / Command Prompt):**
```powershell
python -m venv venv
venv\Scripts\activate
```
> *If PowerShell shows a "Script Execution" error, run this first: `Set-ExecutionPolicy -Scope Process -ExecutionPolicy Bypass` then activate again.*

#### **On macOS / Linux:**
```bash
python3 -m venv venv
source venv/bin/activate
```

*(You know it worked when `(venv)` appears at the start of your terminal line).*

---

### Step 3: Install Dependencies

With `(venv)` activated, install all required packages:

```bash
pip install -r requirements.txt
```

---

### Step 4: Configure Environment Variables (.env)

The `.env` file holds database passwords and secret keys. It is never uploaded to GitHub.

1. Make a copy of `.env.example` named `.env`:
   - **Windows:**
     ```powershell
     copy .env.example .env
     ```
   - **macOS / Linux:**
     ```bash
     cp .env.example .env
     ```
2. Open `.env` in VS Code and update with your local MySQL password:
   ```ini
   SECRET_KEY=django-insecure-local-dev-key-change-in-production
   DEBUG=True

   DB_NAME=fraudguard
   DB_USER=root
   DB_PASSWORD=YOUR_MYSQL_PASSWORD_HERE    # <-- Put your actual MySQL password
   DB_HOST=127.0.0.1
   DB_PORT=3306
   ```

---

### Step 5: Set Up the MySQL Database

Open **MySQL Workbench** (or MySQL CLI) and run this SQL query:

```sql
CREATE DATABASE fraudguard CHARACTER SET utf8mb4 COLLATE utf8mb4_unicode_ci;
```

---

### Step 6: Place the ML Model Artifacts

Because model weights are large, they are excluded from GitHub.

1. Get `model.joblib` and `meta.json` from the team lead or project Google Drive.
2. Place both files directly inside the `ml/artifacts/` folder:
   ```
   fraudguard/
   └── ml/
       └── artifacts/
           ├── model.joblib    <-- drop here
           ├── meta.json       <-- drop here
           └── .gitkeep
   ```

---

### Step 7: Apply Migrations & Create Superuser

Run migrations to create the database tables:

```bash
python manage.py migrate
```

Create an admin account to log into the Django panel:

```bash
python manage.py createsuperuser
```
*(Enter your desired username, email, and password).*

---

### Step 8: Start the Development Server

```bash
python manage.py runserver
```

Open your browser and visit:
* **Home / App:** [http://127.0.0.1:8000/](http://127.0.0.1:8000/)
* **Admin Panel:** [http://127.0.0.1:8000/admin/](http://127.0.0.1:8000/admin/)

If you can log in, your setup is **100% complete and working!** 🎉

---

## 3. Git Workflow for Team Members

To prevent code conflicts and keep `main` clean, follow these rules:

### ⚠️ Golden Rules:
1. **Never commit directly to `main`.**
2. **Always pull the latest changes before starting work.**
3. **Never commit `.env` or files containing passwords.**

---

### Daily Workflow

#### 1. Start of the day — Update your local `main`:
```bash
git checkout main
git pull origin main
```

#### 2. Create a new branch for your task:
Give your branch a descriptive name:
```bash
# Format: feature/<feature-name> or fix/<bug-name>
git checkout -b feature/transaction-scoring
```

#### 3. Do your work & test it locally
Make your code changes, run the server, and verify everything works.

#### 4. Save and commit your changes:
```bash
git status                     # Check what files you changed
git add .                      # Stage your changes
git commit -m "Add scoring API endpoint for transactions"
```

#### 5. Push your branch to GitHub:
```bash
git push -u origin feature/transaction-scoring
```

#### 6. Open a Pull Request (PR):
1. Go to the repo: **[https://github.com/Wasil728/fraudguard](https://github.com/Wasil728/fraudguard)**
2. You will see a banner: **"Compare & pull request"**. Click it.
3. Add a title and short description of what you did.
4. Click **Create pull request** and notify the team lead for review!

---

## 4. Troubleshooting & Common Issues

| Issue | Solution |
|-------|----------|
| **PowerShell says `activate.ps1 cannot be loaded because running scripts is disabled`** | Run `Set-ExecutionPolicy -Scope Process -ExecutionPolicy Bypass` in your terminal and re-run `venv\Scripts\activate`. |
| **`Access denied for user 'root'@'localhost'`** | Check `DB_PASSWORD` in your `.env` file. Make sure it matches your local MySQL password. |
| **`Unknown database 'fraudguard'`** | Run the SQL command `CREATE DATABASE fraudguard;` in MySQL Workbench. |
| **`Port 8000 is already in use`** | Run on a different port: `python manage.py runserver 8080`. |
| **`FileNotFoundError: model.joblib`** | Make sure you downloaded `model.joblib` and `meta.json` and placed them into `ml/artifacts/`. |
| **`XGBoost / deserialization error`** | Ensure your virtual environment is using `xgboost==2.0.3` (run `pip install xgboost==2.0.3`). |

---

*Need help? Reach out to the team lead on our group chat!*
