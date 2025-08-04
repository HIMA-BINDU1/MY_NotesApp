# 📝 Notes App

A simple and elegant Django-powered Notes App that lets users register, log in, and manage their personal notes.

---

## 🔥 Features

-User Registration & Login
Users can sign up and log in securely.
Built-in Django authentication system.
-Logout Functionality
Users can sign out from their session safely.
-Create, View, Edit, and Delete Notes (CRUD)
Users can create new notes, view them, update content, or delete them.
-Secure, User-Specific Notes
Notes are private; each user can only see their own notes.
-Search Notes by Title
Search bar to find notes based on title keywords.
-Pin/Unpin Notes
Highlight important notes by pinning them to the top.
-Dark/Light Mode Toggle
Switch between light and dark modes for better user experience.
-Responsive UI with Bootstrap
Fully styled using Bootstrap for mobile-friendly and clean design.

---

## 🛠️ Technologies Used

- **Backend**: Django
- **Frontend**: HTML, CSS (Bootstrap)
- **Database**: SQLite3

---

## 🚀 Setup Instructions

Follow these steps to set up and run the project locally.

### ✅ 1. Clone the Repository

```bash
git clone https://github.com/HIMA-BINDU1/MY-Notes-App.git
cd MY-Notes-App
---
Now, create a virtual environment using the command python -m venv venv. This will create an isolated environment for your dependencies.
Once the virtual environment is created, activate it. If you are on Windows, run venv\Scripts\activate. If you are using macOS or Linux, use source venv/bin/activate.
After activation, install all the required packages using the command pip install -r requirements.txt.
Now, run the database migrations using the command python manage.py migrate to set up your database schema.
Once migrations are complete, you can start the Django development server using python manage.py runserver.
Finally, open your browser and go to http://127.0.0.1:8000/ to view the application.

---
### 📁 Project Structure

MY-Notes-App/
│
├── notes/               # Django app with views, models, forms
├── templates/           # HTML templates for the project
├── static/              # CSS and JS files
├── db.sqlite3           # Default database file
├── manage.py            # Django command-line utility
├── requirements.txt     # Project dependencies
└── README.md            # Project documentation
