# Task Tracker Backend
 
 This is the backend for the **Task Tracker** project, built using Django and Django REST Framework (DRF). It provides a RESTful API for managing tasks and user authentication.
 
 ---
 
 ## Table of Contents
 
 - [Features](#features)
 - [Technologies Used](#technologies-used)
 - [Installation & Setup](#installation--setup)
 - [API Endpoints](#api-endpoints)
 - [Authentication](#authentication)
 - [Testing](#testing)
   - [Automated Testing](#automated-testing)
   - [Manual Testing](#manual-testing)
 - [Models](#models)
 - [Deployment (Heroku)](#deployment-heroku)
 - [Notes](#notes)
 - [Author](#author)
 
 ---
 
 ## Features
 
 This backend is designed for individual users or small teams to manage their personal or shared task lists. It is suitable for applications where each user needs secure authentication and private task management via a simple API interface.
 
 - User Registration
 - Token-based Authentication (Login)
 - CRUD functionality for tasks (Create, Read, Update, Delete)
 - Authorization: Users can only view and manage their own tasks
 - Deployed to Heroku
 
 ---
 
 ## Technologies Used
 
 - Python 3.13
 - Django 5.1.7
 - Django REST Framework 3.15.2
 - Gunicorn (for Heroku deployment)
 - PostgreSQL (Neon hosted)
 - Heroku for deployment
 
 ---
 
 ## Installation & Setup
 
 1. Clone the repository:
 
 
bash
 git clone https://github.com/itjosephk2/task-tracker-drf.git
 cd task-tracker-drf

 
 2. Create and activate a virtual environment:
 
 
bash
 python -m venv venv
 source venv/bin/activate  # On Windows use `venv\Scripts\activate`

 
 3. Install dependencies:
 
 
bash
 pip install -r requirements.txt

 
 4. Create a .env file in the root directory:
 
 
env
 SECRET_KEY=your-secret-key
 DEBUG=True
 ALLOWED_HOSTS=127.0.0.1,localhost
 database_url=your-postgres-url

 
 5. Run migrations and start the server:
 
 
bash
 python manage.py migrate
 python manage.py runserver

 
 ---
 
 ## API Endpoints
 
 | Method | Endpoint            | Description              |
 |--------|---------------------|--------------------------|
 | POST   | /api/register/      | Register a new user      |
 | POST   | /api/login/         | Login & get auth token   |
 | GET    | /api/tasks/         | List user's tasks        |
 | POST   | /api/tasks/         | Create new task          |
 | GET    | /api/tasks/<id>/    | Retrieve task by ID      |
 | PUT    | /api/tasks/<id>/    | Fully update task        |
 | PATCH  | /api/tasks/<id>/    | Partially update task    |
 | DELETE | /api/tasks/<id>/    | Delete a task            |
 
 ---
 
 ## Authentication
 
 Authentication is handled using **token-based authentication** from Django REST Framework.
 
 ### Login
 - Endpoint: POST /api/login/
 - Request Body:
 
 
json
 {
   "username": "your_username",
   "password": "your_password"
 }

 
 - Response:
 
json
 {
   "token": "your_token_here"
 }

 
 Use this token in the Authorization header for all protected endpoints:
 
 
Authorization: Token your_token_here

 
 ---
 
 ## Testing
 
 ### Automated Testing
 
 Automated tests were implemented using Django’s built-in TestCase framework to ensure that core backend functionality works as intended.
 
 #### Coverage
 
 - **User Authentication**
   - Token-based login authentication tested for validity and security.
 
 - **Task API CRUD Operations**
   - POST /api/tasks/ - Create tasks
   - GET /api/tasks/ - List user tasks
   - GET /api/tasks/<id>/ - Retrieve individual tasks
   - PUT /api/tasks/<id>/ - Fully update tasks
   - PATCH /api/tasks/<id>/ - Partially update tasks
   - DELETE /api/tasks/<id>/ - Delete tasks
 
 - **Permissions**
   - Only authenticated users can access the API.
   - Each user can only access their own tasks.
 
 #### File Location
 
 All test cases are located in:
 
tasks/tests.py

 
 #### Running Tests
 
 To run tests locally:
 
bash
 python manage.py test

 
 ### Manual Testing
 
 Manual testing was conducted using [ReqBin](https://reqbin.com/), a browser-based API testing tool.
 
 #### Example Requests
 
 **Registration**
 
POST /api/register/
 {
   "username": "testuser",
   "email": "test@example.com",
   "password": "secure123"
 }

 
 **Login**
 
POST /api/login/
 {
   "username": "testuser",
   "password": "secure123"
 }

 Response:
 
json
 {"token": "abc123"}

 
 **Create Task**
 
POST /api/tasks/
 Headers: Authorization: Token abc123
 {
   "title": "New Task",
   "description": "Do something important",
   "due_date": "2025-03-30"
 }

 
 **List Tasks**
 
GET /api/tasks/
 Headers: Authorization: Token abc123

 
 **Update Task**
 
PATCH /api/tasks/1/
 Headers: Authorization: Token abc123
 {
   "completed": true
 }

 
 **Delete Task**
 
DELETE /api/tasks/1/
 Headers: Authorization: Token abc123

 
 ---
 
 ## Models
 
 | Field       | Type      | Description                      |
 |-------------|-----------|----------------------------------|
 | id          | Integer   | Auto-incremented primary key     |
 | title       | String    | Title of the task                |
 | description | Text      | Detailed task description        |
 | due_date    | Date      | Due date for the task            |
 | completed   | Boolean   | Task completion status           |
 | created_at  | DateTime  | Timestamp when task was created  |
 | owner       | FK(User)  | Reference to the user who owns it|
 
 ---
 
 ## Deployment (Heroku)
 
 1. Create Heroku app:
 
bash
 heroku create your-app-name

 
 2. Set environment variables:
 
bash
 heroku config:set SECRET_KEY=your-secret-key
 heroku config:set DEBUG=False
 heroku config:set ALLOWED_HOSTS=your-app-name.herokuapp.com
 heroku config:set DATABASE_URL=your-postgres-url

 
 3. Disable collectstatic if not using static files:
 
bash
 heroku config:set DISABLE_COLLECTSTATIC=1

 
 4. Deploy to Heroku:
 
bash
 git push heroku main

 
 5. Run migrations:
 
bash
 heroku run python manage.py migrate

 
 ---
 
 ## Notes
 
 - Replace all placeholders with your actual secret keys, database URLs, and app name.
 - This backend is designed to work seamlessly with a React frontend.
 
 ---
 
 ## Author
 
 Built with care by Joseph Keane, 2025.
