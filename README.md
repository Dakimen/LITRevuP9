# LITRevu

**LITRevu** is a Django web application for book/article reviews written primarily in Python, with HTML/CSS/JS frontend components.  
It allows users to request, publish reviews of books and articles and follow other user accounts.

---

## Features

- User registration, login, and profile management
- Create and manage review requests
- Publish reviews for books or articles
- Search for users to follow through their nicknames
- Dashboard for users to view their own requests & reviews as well as those by accounts they follow

---

## Technologies & Dependencies

- **Language**: Python
- **Framework**: Django
- **Frontend**: HTML, CSS, a bit of JavaScript
- **Dependencies**: as listed in `requirements.txt`

---

## Installation & Setup

### Prerequisites

- Python 3

### Steps

1. Clone the repo

   ```bash
   git clone https://github.com/Dakimen/LITRevuP9.git
   cd LITRevuP9
   ```

2. Create & activate a virtual environment
   ```
   python3 -m venv .venv
   source venv/bin/activate   # (on Unix/macOS)
   # or .venv\Scripts\activate on Windows
   ```
3. Install dependencies
   ```
   pip install -r requirements.txt
   ```
4. Apply migrations & set up database
   ```
   cd LITRevu
   python manage.py makemigrations
   python manage.py migrate
   ```
5. Run the development server
   ```
   python manage.py runserver
   ```
6. Go to http://127.0.0.1:8000/

#### Usage Examples

- Register a user or log in

- Create a new review request via the interface

- Submit reviews under your account

- Search for users to follow and manage subscriptions

#### Additional info

This project was realized in the context of a Python/Django bachelor program, intended to be a study project only.
