# 📝 Django Blog App

A full-featured blog web application built with Django. Users can register, log in, create, update, and delete their own blog posts, as well as comment on posts by others. This project was created as part of a personal learning journey to understand Django fundamentals and web development best practices.

---

## 🚀 Features

- ✅ User registration, login & logout
- 📝 Create, update, and delete blog posts
- 💬 Comment system for user interaction
- 🔒 Authentication and authorization
- 🛠️ Django admin panel for managing posts and comments
- 📱 Responsive design

---

## 🛠️ Tech Stack

- **Backend:** Django (Python)
- **Frontend:** HTML, CSS (Bootstrap)
- **Database:** SQLite (can be upgraded to PostgreSQL)
- **Other Tools:** Django Admin, Django Auth

---

## 📁 Project Structure

blog_project/
|--athentication/
├── blog/ # Blog app (models, views, urls, templates)

├── users/ # Handles user authentication (register/login)
├── templates/ # HTML templates
├── static/ # CSS, JS, images
├── db.sqlite3 # Default SQLite database
├── manage.py
├── requirements.txt
└── README.md


---

## ⚙️ Installation

Follow the steps below to run the project locally:

### 1. Clone the repository

```bash
git clone https://github.com/GrehTek/django-blog.git
cd django-blog

# Create virtual environment
python -m venv venv

# Activate it
# For Windows:
venv\Scripts\activate
# For macOS/Linux:
source venv/bin/activate

#install requirement
pip install -r requirements.txt

python manage.py migrate

#create superuser
python manage.py createsuperuser

#run server
python manage.py runserver

#open in your browser
http://127.0.0.1:8000/ or http://localhost:8000

🤝 Contributing
Pull requests are welcome! If you have suggestions or improvements, feel free to open an issue or a pull request.

🙋‍♂️ Author
Daniel Daniel
GitHub: @GrehTek
LinkedIn: linkedin.com/in/daniel-daniel-427203111
