# Django Application

## Description
This is a Django-based application. Follow the instructions below to set up and run the application on your local environment.

---

## Prerequisites
Ensure you have the following installed on your system:

1. **Python** (Version 3.8 or later) - [Download Python](https://www.python.org/downloads/)
2. **Pip** - Comes bundled with Python.

---

## Installation Steps

### Step 1: Download the Repository
Download the project as a ZIP file from the repository:

- Navigate to [FYP_CVE_DJANGO](https://github.com/umairniaziofficial/FYP_CVE_DJANGO).
- Click the "Code" button and select "Download ZIP".
- Extract the ZIP file to a folder on your system.

### Step 2: Install Python
If Python is not already installed on your system, download and install it from [Python's official website](https://www.python.org/downloads/).

During installation, make sure to select the option **"Add Python to PATH"**.

### Step 3: Install Dependencies
Navigate to the project folder and use `pip` to install the required dependencies listed in `requirements.txt`.
```bash
# Navigate to the project folder
cd FYP_CVE_DJANGO

# Install dependencies
pip install -r requirements.txt
```

### Step 4: Set Up the Database
Run the following Django management commands to set up the database.
```bash
# Apply migrations
python manage.py migrate

# Optional: Create a superuser to access the admin panel
python manage.py createsuperuser
```

### Step 5: Run the Development Server
Start the Django development server.
```bash
python manage.py runserver
```

### Step 6: Access the Application
Open your browser and navigate to:
```
http://127.0.0.1:8000/
```

---

## Troubleshooting

- **Dependency issues:** Use `pip install` for individual packages as needed.
- **Database errors:** Verify migrations with `python manage.py showmigrations` and reapply them if needed.

---

## License
This project is licensed under the MIT License. See the `LICENSE` file for more information.
