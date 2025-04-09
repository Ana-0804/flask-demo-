# 🧪 Flask Demo App — Message Board

This is a simple web application built with **Flask** and **SQLite** that allows users to submit their name and a message. All submitted messages are displayed on the home page.

> Ideal for beginners learning Flask, form handling, SQLite, and database interaction using SQLAlchemy ORM.

---

##  UI Preview

> Here's what the app does:
- Displays a clean message board
- Accepts name and message through a form
- Saves to a local SQLite database
- Shows success or error feedback via flash messages

---

##  Tech Stack

| Component       | Technology Used     |
|-----------------|---------------------|
| Backend         | Flask (Python)      |
| Database        | SQLite + SQLAlchemy |
| Frontend        | HTML + CSS          |

---

## Project Structure

flask-demo-app/ │ ├─ app.py # Main Flask application ├─ templates/ │ └─ index.html # HTML template ├── static/ │ └─ style.css # CSS for style ├─ messages.db # SQLite DB file (auto-created) └ README.md

##  Setup Instructions

###  Clone the Repository


git clone https://github.com/Ana-0804/flask-demo-app.git
cd flask-demo-app


---

## Install dependencies

pip install Flask Flask_SQLAlchemy


----

## Run The App

python app.py
