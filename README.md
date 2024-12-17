# Project Management API

The Project Management Tool API provides a robust backend to enable teams to collaborate efficiently. It includes functionalities for user authentication, project management, task tracking, and communication through comments. The API is designed for consumption by web and mobile applications, supporting seamless user experiences.


## Key Features

### User Management
- User registration, authentication (JWT), and profile management.
- CRUD operations for user accounts.

### Project Management
- Create, retrieve, update, delete projects.
- Manage project ownership and member roles (Admin, Member).

### Task Management
- Assign tasks, track statuses (To Do, In Progress, Done), set priorities (Low, Medium, High).
- CRUD operations for tasks under specific projects.

### Comment System
- Task-specific discussions with comments.
- CRUD operations for task comments.

### Authentication & Security
- Secure API access with JWT tokens.
- Role-based access control for proper permissions.

## Deliverables
- Well-structured database schema for users, projects, tasks, and comments.

---
## Postman Collection for Test
[Project Management API.postman_collection.json](https://github.com/user-attachments/files/18169352/Project.Management.API.postman_collection.json)


## How to Run the Project

### Clone the Repository:
```bash
git clone https://github.com/MehediHasanNasim/project_management_api.git
cd project_management

```
### Set Up Environment:

```bash
python3 -m venv venv
source venv/bin/activate  # For Windows: `venv\Scripts\activate`
```
### Install Dependencies
```bash
pip install -r requirements.txt
```
### Apply Migrations
```bash
python manage.py makemigrations
python manage.py migrate
```
### Run the Development Server
```bash
python manage.py runserver
```
### Note
Before running the project, you need to set up your environment variables, especially for production environments. 

1. **Create a `.env` file** in the root of your project (same level as `manage.py`).
   
2. **Add the following environment variables** to the `.env` file:
   
   ```env
   SECRET_KEY=<your_secret_key>
   DEBUG=True  # Set to False in production environments


# Project Management API

This API is designed for a project management tool to manage users, projects, tasks, and comments. It can be used for both web and mobile applications.

## Testing the API

Use Postman or similar tools to test the endpoints listed below.

### Authentication Endpoints

| Method | Endpoint            | Description             | Example JSON                                             |
|--------|---------------------|-------------------------|----------------------------------------------------------|
| POST   | `/auth/users/register`      | Register a user.        | `{ "username": "user", "email": "user@email.com", "password": "password123" }` |
| POST   | `/auth/users/login/` | Obtain a JWT token.     | `{ "username": "user", "password": "password123" }`      |


---

### User Endpoints

| Method | Endpoint            | Description             | Example JSON                                             |
|--------|---------------------|-------------------------|----------------------------------------------------------|
| GET    | `/users/`           | List all users.         | —                                                        |
| GET    | `/users/{id}/`      | Retrieve user details.  | —                                                        |
| PUT    | `/users/{id}/`      | Update user details.    | `{ "first_name": "John", "last_name": "Doe" }`           |
| DELETE | `/users/{id}/`      | Delete a user.          | —                                                        |

---

### Project Endpoints

| Method | Endpoint            | Description             | Example JSON                                             |
|--------|---------------------|-------------------------|----------------------------------------------------------|
| POST   | `/projects/`        | Create a new project.   | `{ "name": "Project A", "description": "Details", "owner": 1 }` |
| GET    | `/projects/`        | List all projects.      | —                                                        |
| GET    | `/projects/{id}/`   | Retrieve project details.| —                                                        |
| PUT    | `/projects/{id}/`   | Update project details. | `{ "name": "Updated Project Name" }`                     |
| DELETE | `/projects/{id}/`   | Delete a project.       | —                                                        |

---

### Project Member Endpoints

| Method | Endpoint                | Description             | Example JSON                                             |
|--------|-------------------------|-------------------------|----------------------------------------------------------|
| POST   | `/project-members/`     | Add a member to project.| `{ "project": 1, "user": 2, "role": "Admin" }`           |
| GET    | `/project-members/`     | List all project members.| —                                                        |
| GET    | `/project-members/{id}/`| Retrieve member details.| —                                                        |
| PUT    | `/project-members/{id}/`| Update member's role.   | `{ "role": "Member" }`                                   |
| DELETE | `/project-members/{id}/`| Remove a member.        | —                                                        |

---

### Task Endpoints

| Method | Endpoint            | Description             | Example JSON                                             |
|--------|---------------------|-------------------------|----------------------------------------------------------|
| POST   | `/tasks/`           | Create a new task.      | `{ "title": "Task 1", "description": "Details", "status": "To Do", "priority": "High", "assigned_to": 2, "project": 1 }` |
| GET    | `/tasks/`           | List all tasks.         | —                                                        |
| GET    | `/tasks/{id}/`      | Retrieve task details.  | —                                                        |
| PUT    | `/tasks/{id}/`      | Update task details.    | `{ "status": "In Progress", "priority": "Medium" }`      |
| DELETE | `/tasks/{id}/`      | Delete a task.          | —                                                        |

---

### Comment Endpoints

| Method | Endpoint            | Description             | Example JSON                                             |
|--------|---------------------|-------------------------|----------------------------------------------------------|
| POST   | `/comments/`        | Add a comment to task.  | `{ "content": "Great work!", "user": 1, "task": 3 }`     |
| GET    | `/comments/`        | List all comments.      | —                                                        |
| GET    | `/comments/{id}/`   | Retrieve comment.       | —                                                        |
| PUT    | `/comments/{id}/`   | Update a comment.       | `{ "content": "Updated comment." }`                      |
| DELETE | `/comments/{id}/`   | Delete a comment.       | —                                                        |
