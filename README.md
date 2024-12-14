![DeepSource](https://static.deepsource.io/deepsource-badge-light-mini.svg)


# Django Blog Application

This is a simple blogging platform built using Django, allowing users to create, edit, and manage blog posts with features like cover image uploads, Markdown syntax for content, and user authentication.

## Features

- User authentication (sign up, login, logout).
- Create, edit, delete blog posts.
- Upload cover images (max size: 1 MB).
- Use Markdown for styling blog content.
- Desktop design using HTML/CSS and JavaScript.
- SQLite database for development;
- Dockerized for deployment and development environments.

---

## Requirements

Ensure you have the following installed:

- Python 3.9 or higher
- pip (Python package manager)
- SQLite (for development database)
- Docker (optional, for containerized setup)
- A virtual environment tool like `venv` or `virtualenv`

---

## Installation

1. Clone the repository:

   ```bash
   git https://github.com/<username>/first-django-blog.git
   cd first-django-blog
   ```

2. Create a virtual environment and activate it:

   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows, use venv\Scripts\activate
   ```

3. Install the required packages:

   ```bash
   pip install -r requirements/local.txt
   ```

4. Apply migrations:

   ```bash
   python manage.py migrate
   ```

5. Create Superuser

   ```bash
   python manage.py createsuperuser
   ```

6. Run the development server

   ```bash
   python manage.py runserver
   ```

Visit the app at http://127.0.0.1:8000/



