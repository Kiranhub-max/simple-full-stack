Below is a complete **README.md** that you can directly copy into your GitHub repository.

# 🚀 Simple Full Stack Login page

<img width="1233" height="897" alt="Screenshot 2026-08-03 191134" src="https://github.com/user-attachments/assets/15862a43-66fe-48b1-91fe-b010dbce4ba6" />


A beginner-friendly Full Stack CRUD application built using:

* ⚛️ React (Frontend)
* ⚡ FastAPI (Backend)
* 🐬 MySQL (Database)

This project demonstrates how a React frontend communicates with a FastAPI backend, which then performs CRUD operations on a MySQL database.

---

# 📋 Prerequisites

Before running the project, make sure the following software is installed on your computer.

### 1. Python (3.10 or above)

Check the installation:

```bash
python --version
```

or

```bash
python3 --version
```

---

### 2. Node.js and npm

Check the installation:

```bash
node -v
```

```bash
npm -v
```

---

### 3. MySQL Server

Make sure your MySQL server is running.

Create a database for this project.

Example:

```sql
CREATE DATABASE school_demo;
```

Update the database connection details in `backend/database.py`.

Example:

```python
DATABASE_URL = "mysql+pymysql://username:password@localhost/school_demo"
```

Replace:

* `username`
* `password`
* `school_demo`

with your own MySQL credentials.

---

# 📥 Step 1: Clone the Repository

Open a terminal and run:

```bash
git clone https://github.com/<your-github-username>/<repository-name>.git
```

Go inside the project folder:

```bash
cd <repository-name>
```

---

# 🐍 Step 2: Backend Setup (FastAPI)

Go to the backend folder.

```bash
cd backend
```

---

## Create a Virtual Environment

Windows:

```bash
python -m venv venv
```

This creates a folder named:

```
venv/
```

---

## Activate the Virtual Environment

### Git Bash

```bash
source venv/Scripts/activate
```

### Windows Command Prompt (CMD)

```cmd
venv\Scripts\activate
```

### Windows PowerShell

```powershell
venv\Scripts\Activate.ps1
```

After activation, your terminal should look similar to:

```
(venv)
```

---

## Install Python Packages

Install all required dependencies.

```bash
pip install fastapi uvicorn sqlalchemy pymysql
```

---

## Start the FastAPI Server

```bash
uvicorn main:app --reload
```

If everything is correct, you will see:

```
INFO: Uvicorn running on http://127.0.0.1:8000
```

Keep this terminal running.

---

# ⚛️ Step 3: Frontend Setup (React)

Open **another terminal**.

Go to the frontend folder.

If you are currently inside the backend folder:

```bash
cd ..
```

Now enter:

```bash
cd frontend
```

---

## Install Node Modules

```bash
npm install
```

Wait for the installation to finish.

---

## Start the React Application

```bash
npm run dev
```

You should see something similar to:

```
Local: http://localhost:5173/
```

Open the URL in your browser.

---

# 🌐 Project URLs

### Frontend

```
http://localhost:5173
```

### Backend

```
http://127.0.0.1:8000
```

### FastAPI Swagger Documentation

```
http://127.0.0.1:8000/docs
```

---

# 📁 Project Structure

```
simple-full-stack/
│
├── backend/
│   ├── venv/
│   ├── main.py
│   ├── database.py
│   ├── models.py
│   ├── schemas.py
│  
│   
│
└── frontend/
    ├── src/
    ├── package.json
    ├── package-lock.json
    └── ...
```

---

# ▶️ Running the Project

You need **two terminals**.

### Terminal 1 (Backend)

```bash
cd backend

python -m venv venv

source venv/Scripts/activate      # Git Bash
# OR
venv\Scripts\activate             # CMD
# OR
venv\Scripts\Activate.ps1         # PowerShell

pip install fastapi uvicorn sqlalchemy pymysql

uvicorn main:app --reload
```

---

### Terminal 2 (Frontend)

```bash
cd frontend

npm install

npm run dev
```

---

# ✅ Features

* Add User
* View Users
* Update User
* Delete User

This project demonstrates all four CRUD operations.

---

# 🛠️ Technologies Used

### Frontend

* React
* JavaScript
* Fetch API

### Backend

* FastAPI
* SQLAlchemy
* Pydantic
* Uvicorn

### Database

* MySQL

---

# 🔄 Application Flow

```
User
   │
   ▼
React Frontend
   │
HTTP Request (Fetch API)
   │
   ▼
FastAPI Backend
   │
SQL Queries
   │
   ▼
MySQL Database
```

---

# ❗ Common Errors

## ModuleNotFoundError

Install dependencies again:

```bash
pip install -r requirements.txt
```

---

## MySQL Connection Error

* Make sure MySQL is running.
* Verify your username and password in `database.py`.
* Check that the database exists.

---

## CORS Error

Make sure the FastAPI server is running before starting the React application.

Also verify that `CORSMiddleware` is configured correctly in `main.py`.

---

## Port Already in Use

If port **8000** or **5173** is already being used, close the existing process or restart your computer.

---

# 📚 Git Commands

Check project status:

```bash
git status
```

Stage all changes:

```bash
git add .
```

Commit changes:

```bash
git commit -m "Added new feature"
```

Push changes:

```bash
git push
```

---

# 🎯 Learning Objectives

By completing this project, you will learn:

* React Basics
* FastAPI Basics
* REST APIs
* CRUD Operations
* SQLAlchemy
* MySQL Integration
* Fetch API
* CORS
* Decoupled Architecture
* Git & GitHub Workflow

  
