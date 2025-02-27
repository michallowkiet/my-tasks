# My Tasks APP

App for help with manage every day tasks like shopping, day to day activities and more. Plus it has a calendar view where you can see all your tasks in one place. Extra features include:

## Features
- [ ] User authentication and authorization*.
- [ ] Task creation and editing*.
- [ ] Task deletion*.
- [ ] Task categorization*.
- [ ] Task priority setting*.
- [ ] Calendar integration for task scheduling*.
- [ ] Dark mode support*.
- [ ] Responsive design for mobile devices*.
- [ ] Task filtering by date, category, or priority*.
- [ ] Task reminders with customizable notification settings*.
- [ ] Docker containerization for easy deployment*.
  
  *Note: The asterisk (\*) indicates that the feature is currently under development and may not be fully functional yet.*

## Installation

Project setup have 2 parts:

### Frontend

1. **WIP** Probably using Angular or React.
   

### Backend

Django REST Framework is used for building the backend API. For managing project dependencies, [uv](https://github.com/astral-sh/uv) is used.

To install My Tasks APP, follow these steps:
1. **Clone the Repository:**
   - Open your terminal or command prompt.
   - Navigate to the directory where you want to store the project.
   - Run the following command to clone the repository:
     - ```bash git clone https://github.com/michallowkiet/my-tasks-app.git```
2. **Install Dependencies:**
    - Change into the project directory:
      - ```cd my-tasks-app/backend```
      - Run the following command to install all dependencies. UV take care of installing Python packages and managing virtual environments.:
      - ``` uv sync ```
3. **Run the Application:**
    - Ensure that your database is set up (e.g., PostgreSQL, SQLite).
    - Apply migrations to create the necessary database tables:
      - ```uv run python manage.py migrate```
    - Start the Django development server by running:
      - ```uv run manage.py runserver```