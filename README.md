# Django Bookmark Project

A simple bookmark management website built using Django and Python.

## About the Project

This project is a beginner-friendly web application developed to practise Django web development and HTML frontend design.

## Technologies Used

- Python
- Django
- HTML
- CSS
- SQLite

## Features

- Simple and user-friendly website interface
- Bookmark management
- Background images and static image resources

## Project Structure

```text
Django-bookmark-project/
├── bookmark_project/
├── bookmarks/
├── manage.py
├── requirements.txt
├── .gitignore
└── README.md
```

## How to Run the Project

1. Clone this repository:

   ```bash
   git clone https://github.com/malsha-pathirana/Django-bookmark-project.git
   ```

2. Open the project folder.

3. Create and activate a virtual environment.

4. Install the required packages:

   ```bash
   pip install -r requirements.txt
   ```

5. Create a `.env` file in the project root and add your Django secret key:

   ```text
   DJANGO_SECRET_KEY=your-secret-key
   ```

6. Run database migrations:

   ```bash
   python manage.py migrate
   ```

7. Start the development server:

   ```bash
   python manage.py runserver
   ```

8. Open `http://127.0.0.1:8000/` in your browser.

## Author

Malsha Pathirana