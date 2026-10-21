# Student Management System

A full-stack Django + MySQL web application for managing student records.

---

## Tech Stack
- **Backend:** Python 3.10+, Django 4.2
- **Database:** MySQL 8.0
- **Frontend:** Bootstrap 5, HTML5, CSS3, JavaScript

---

## Step 1 — MySQL Setup (run in MySQL Workbench or CLI)

```sql
CREATE DATABASE student_management CHARACTER SET utf8mb4 COLLATE utf8mb4_unicode_ci;
CREATE USER 'sms_user'@'localhost' IDENTIFIED BY 'YourPasswordHere';
GRANT ALL PRIVILEGES ON student_management.* TO 'sms_user'@'localhost';
FLUSH PRIVILEGES;
```

---

## Step 2 — Project Setup (Windows CMD / VS Code Terminal)

```bash
# 1. Navigate to project folder
cd "c:\Users\JAYAN\OneDrive\Desktop\Jayan Project\ALL PROJECT\Student Management System"

# 2. Create and activate virtual environment
python -m venv venv
venv\Scripts\activate

# 3. Install dependencies
pip install -r requirements.txt

# 4. Edit .env — set your MySQL password
# Open .env and replace YourPasswordHere with your actual password

# 5. Run migrations
python manage.py migrate

# 6. Create superuser (admin login)
python manage.py createsuperuser

# 7. Start the server
python manage.py runserver
```

Open: http://127.0.0.1:8000

---

## Step 3 — Verify in MySQL Workbench

```sql
USE student_management;
SHOW TABLES;
SELECT * FROM students_student;
SELECT * FROM students_course;
```

---

## Troubleshooting

| Error | Fix |
|---|---|
| `django.db.utils.OperationalError: (1045)` | Wrong MySQL user/password in `.env` |
| `ModuleNotFoundError: No module named 'MySQLdb'` | Run `pip install mysqlclient` |
| `django.core.exceptions.ImproperlyConfigured` | Check `DJANGO_SETTINGS_MODULE` = `config.settings` |
| Static files not loading | Run `python manage.py collectstatic` |

---

## Default URLs

| Page | URL |
|---|---|
| Login | http://127.0.0.1:8000/login/ |
| Dashboard | http://127.0.0.1:8000/ |
| Students | http://127.0.0.1:8000/students/ |
| Add Student | http://127.0.0.1:8000/students/add/ |
| Courses | http://127.0.0.1:8000/courses/ |
| Django Admin | http://127.0.0.1:8000/admin/ |
