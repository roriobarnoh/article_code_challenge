# 🏫 School Management CLI System

A CLI-based application to manage Teachers and Students using Python, SQLAlchemy ORM, Alembic, and Pipenv.

This project is built for Phase 3 of the Coding Bootcamp and demonstrates the use of Object Relational Mapping (ORM), CLI interfaces, and professional software practices.

---

## 📚 Features

- 🚀 Easy-to-use CLI interface
- 👩‍🏫 Teacher management: add, find, delete, and view assigned students
- 👧 Student management: add, find, transfer, delete, list by grade
- 🧠 Input validation for emails (teachers) and grades (K–12)
- 📈 Advanced tools: list students by grade, view teacher workload
- 💾 Persistent database with Alembic migrations
- 🧪 Sample data: 5 teachers and 10 students (elementary to high school)

---

## 🛠️ Technologies Used

- **Python 3.11**
- **SQLAlchemy 2.0** – ORM for database operations
- **Alembic** – schema migrations
- **Pipenv** – virtual environment and dependency manager
- **SQLite** – lightweight local database
- **Email-Validator** – email address validation

---

## 🧰 Setup Instructions

### 1️⃣ Clone the Repository

## Install Dependencies with Pipenv
pipenv install
pipenv shell
alembic init lib/db/migrations
### Edit alembic.ini and set:
sqlalchemy.url = sqlite:///lib/db/school.db
### Edit lib/db/migrations/env.py:
from lib.db.models import Base  # import your Base
target_metadata = Base.metadata
### Generate and Apply Initial Migration
alembic revision --autogenerate -m "Initial schema"
alembic upgrade head

##  Initialize Alembic for Migrations
### Seed the Database
python lib/db/seed.py
### Run the CLI Application
python lib/cli.py

```bash
git clone https://github.com/your-username/school-management-cli.git
cd school-management-cli
##v
##
