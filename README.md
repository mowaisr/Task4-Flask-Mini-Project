Task 4 - Flask Mini Project

Overview

This project is a simple Task Manager Web Application developed using Flask.

The application allows users to add tasks, view tasks, mark tasks as completed, and delete tasks.

Technologies Used

- Python
- Flask
- HTML
- Bootstrap
- Jinja2

Features

- Add new tasks
- Display all tasks
- Mark tasks as completed
- Delete tasks
- Form handling using POST
- Flask routing
- Jinja2 templates
- Responsive UI using Bootstrap
- In-memory task storage

CRUD Operations

The project demonstrates basic CRUD functionality:

- Create: Add a new task
- Read: View all tasks
- Update: Mark a task as completed
- Delete: Remove a task

How to Run

1. Install Flask

pip install flask

2. Run the application

python app.py

3. Open in browser

http://127.0.0.1:5000/

Project Structure

Task4-Flask-Mini-Project/
│
├── app.py
├── README.md
│
├── templates/
│   └── index.html
│
└── screenshots/
    ├── 01_home_page.png
    ├── 02_add_task.png
    ├── 03_completed_task.png
    └── 04_delete_task.png

Screenshots

The screenshots demonstrate:

1. Home page with existing tasks
2. Adding a new task
3. Marking a task as completed
4. Deleting a task

Learning Outcome

Through this project, I learned how to create Flask routes, handle HTML forms using GET and POST methods, use Jinja2 templates, implement basic CRUD operations, and create a simple web interface using Bootstrap.

Note

The application currently uses temporary in-memory storage, so tasks are reset when the Flask server is restarted.