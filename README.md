# Expense Tracker

A full-stack Expense Tracker web application built with **Django**. The application allows users to securely manage their daily expenses with custom authentication, authorization, session management, and expense analytics.

---

## Features

### Authentication

* User Registration
* User Login
* User Logout
* Session-Based Authentication

### Expense Management

* Add Expense
* Edit Expense
* Delete Expense
* View All Expenses
* Category-wise Expense Management

### Security

* User Authorization
* User-Specific Expenses
* User-Specific Reports

### Reports

* Total Expense
* Highest Expense
* Average Expense
* Total Number of Expenses
* Total Categories

---

## Tech Stack

* Python
* Django
* SQLite
* HTML5
* CSS3

---

## Project Structure

```
Expense_Tracker/
│
├── Expense/
├── ExpenseTracker/
├── static/
├── manage.py
├── requirements.txt
└── README.md
```

---

## Installation

Clone the repository:

```bash
git clone https://github.com/anshukumarmishra/Expense_Tracker.git
```

Move into the project directory:

```bash
cd Expense_Tracker
```

Create a virtual environment:

```bash
python -m venv venv
```

Activate the virtual environment:

### Windows

```bash
venv\Scripts\activate
```

Install dependencies:

```bash
pip install -r requirements.txt
```

Run migrations:

```bash
python manage.py migrate
```

Start the development server:

```bash
python manage.py runserver
```

Open your browser:

```
http://127.0.0.1:8000/
```

---

## What I Learned

* Django Models
* Django Forms & ModelForms
* CRUD Operations
* Django ORM
* Aggregation Functions (Sum, Avg, Max)
* Custom Authentication
* Authorization
* Session Management
* Password Hashing
* Git & GitHub

---

## Future Improvements

* Class Based Views (CBV)
* Django REST Framework (DRF)
* React Frontend
* Expense Charts
* Monthly Reports
* Category Analytics
* PostgreSQL Database
* Email Verification
* Password Reset

---

## Author

**Anshu Kumar Mishra**

MCA Student

GitHub: https://github.com/anshukumarmishra
