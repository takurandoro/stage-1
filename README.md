# Stage 1 - Django Project

## Project Overview
Stage 1 is the foundational phase of a Django-based project aimed at developing a robust and scalable web application. This repository contains the initial setup, including essential configurations, directory structure, and dependencies.

## Repository Structure
```
stage-1/
├── api/                # Contains the API-related files and configurations
├── uninest/            # Core Django project directory
├── db.sqlite3          # Default SQLite database file
├── manage.py           # Django management script
├── requirements.txt    # Python dependencies for the project
```

### 1. `api/`
This directory will house all the API-related modules, including serializers, views, and URL configurations. It serves as the backbone of the application's backend services.

### 2. `uninest/`
The main Django project directory containing settings, URLs, and WSGI configurations. This is the central point for project-wide settings and configurations.

### 3. `db.sqlite3`
A lightweight SQLite database used for development and testing purposes. You can switch to a more robust database like PostgreSQL or MySQL for production.

### 4. `manage.py`
A script for managing various Django functionalities, such as running the server, applying migrations, and creating apps.

### 5. `requirements.txt`
This file lists all the Python dependencies required for the project. Install them using the following command:
```bash
pip install -r requirements.txt
```

## Getting Started
Follow these steps to set up the project locally:

### Prerequisites
- Python (>= 3.8)
- pip (Python package manager)

### Installation
1. Clone the repository:
   ```bash
   git clone <repository_url>
   cd stage-1
   ```

2. Create a virtual environment:
   ```bash
   python -m venv venv
   source venv/bin/activate   # On Windows: venv\Scripts\activate
   ```

3. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```

4. Run database migrations:
   ```bash
   python manage.py migrate
   ```

5. Start the development server:
   ```bash
   python manage.py runserver
   ```

6. Access the application at `http://127.0.0.1:8000/`.

## Future Enhancements
- Implementing the API endpoints in the `api/` directory.
- Adding authentication and authorization mechanisms.
- Setting up a production database and deploying the project.

---
Stay tuned for updates in Stage 2!
