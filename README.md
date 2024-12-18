# Quiz Master - A Django Application

Welcome to the Quiz Master, a Django-based web application that lets users take quizzes and view their scores. This project includes features such as question sets, a leaderboard, and user authentication.

## Table of Contents

- [Features](#features)
- [Installation](#installation)
- [Folder Structure](#folder-structure)
- [Running the Application](#running-the-application)
- [Usage](#usage)

## Features

- **User Authentication**: Users can register, log in, and log out.
- **Quiz Creation and Participation**: Admins can create quizzes with multiple-choice questions.
- **Leaderboard**: View scores and rank participants based on their performance.

## Installation

Follow these steps to set up the project on your local machine:

### 1. Clone the repository
```bash
git clone https://github.com/VikasAdhikari07/QuizApplication
cd quizApp
```

### 2. Set up a virtual environment
It’s recommended to use a virtual environment to manage dependencies.

```bash
python -m venv venv
venv\Scripts\activate # for windows user
```

### 3. Install dependencies
Install the required packages from the `requirements.txt` file.

```bash
pip install -r requirements.txt
```

### 4. Setup database
Make sure you have `db.sqlite3` in your root directory. If not, you can create one by running:

```bash
python manage.py migrate
```

### 5. Run the application
Start the Django development server.

```bash
python manage.py runserver
```

Now, open your web browser and go to `http://127.0.0.1:8000/`. You should see the Quiz Master homepage.

## Folder Structure

- **quizApp**: This folder contains the main Django application.
- **db.sqlite3**: SQLite database for storing quiz data.
- **manage.py**: Django management script.
- **quiz**: Directory containing models, views, and URL patterns related to quizzes.
- **quizApp**: Directory containing the main application URL patterns, setting etc.
- **requirements.txt**: List of Python packages required for the project.
- **static**: Directory for static files (CSS).
- **templates**: Directory for HTML templates.

## Usage

### Creating and Managing Quizzes
1. **Admin Login**: Log in using the Django admin credentials (default: `admin` / `admin`). Go to `/admin/` to create quizzes.
2. **Taking a Quiz**: After logging in, users can navigate to available quizzes and start answering questions.
3. **Leaderboard**: After completing a quiz, users can see their rank and score compared to other participants.

