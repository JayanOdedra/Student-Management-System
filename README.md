# Student Management System

A Django-based web application to manage student records (Add, View, Update, Delete).

## Prerequisites

- Python 3.8+
- pip

## Installation

1. **Clone the repository**
   ```bash
   git clone <repository-url>
   cd "Student Management System"
   ```

2. **Create and activate a virtual environment**
   ```bash
   python -m venv venv

   # Windows
   venv\Scripts\activate

   # macOS/Linux
   source venv/bin/activate
   ```

3. **Install dependencies**
   ```bash
   pip install -r requirements.txt
   ```

4. **Apply migrations**
   ```bash
   python manage.py migrate
   ```

## Running the App

```bash
python manage.py runserver
```

Open your browser and go to: [http://127.0.0.1:8000](http://127.0.0.1:8000)

## Features

- Add, view, update, and delete student records
- SQLite database (no extra setup needed)
- Admin panel available at `/admin/`

## Create Admin User (Optional)

```bash
python manage.py createsuperuser
```
