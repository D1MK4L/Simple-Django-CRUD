# 🧪 Simple Django CRUD API

A Django REST Framework project featuring user registration, login, JWT authentication, and CRUD operations on posts — all documented with Swagger UI.

---

## 🚀 Features

- ✅ User Registration & Login (`/api/register/`, `/api/login/`)
- 🔐 JWT Authentication (`/api/token/`)
- 📬 Full CRUD for Posts (`/api/posts/`)
- 📖 Swagger UI at `/swagger/` or `/docs/`
- ⚙️ Environment variable-based DB config

---

## 📦 Requirements

- Python 3.10+
- PostgreSQL
- Virtualenv (recommended)

---

## ⚙️ Setup Instructions

### 1. Clone the Repository

```bash
git clone https://github.com/your-username/simple-django-crud.git
cd simple-django-crud
```

### 2. Create Virtual Environment & Install Dependencies

```bash
python -m venv venv
venv\Scripts\activate  # Windows
# Or on Unix/macOS:
# source venv/bin/activate

pip install -r requirements.txt
```

### 3. Set Environment Variables (Windows Example)

```env
Simple_App_DB_User=your_db_user
Simple_App_DB_Password=your_db_password
Simple_App_DB_Name=your_db_name
DB_HOST=localhost
DB_PORT=5432
```
- Restart your terminal (or reboot your PC) after setting them.

### 4. Run Migrations

```bash
python manage.py makemigrations
python manage.py migrate
```

### 5. Create Superuser (optional)

```bash
python manage.py createsuperuser
```

### 6. Start the Development Server

```bash
python manage.py runserver
```
- Access at : http://127.0.0.1:8000

🧪 API Endpoints

All endpoints are prefixed with /api/.
Method	Endpoint	Description
POST	/api/register/	Register new users
POST	/api/login/	Log in and receive token
POST	/api/token/	JWT authentication token
GET	/api/posts/	List all posts
POST	/api/posts/	Create a new post
GET	/api/posts/{id}/	Retrieve a specific post
PUT	/api/posts/{id}/	Fully update a post
PATCH	/api/posts/{id}/	Partially update a post
DELETE	/api/posts/{id}/	Delete a post
DELETE	/api/posts/{id}/delete_post/	Custom delete endpoint

📘 Swagger UI

Interactive API docs at: 
```url
http://127.0.0.1:8000/api/swagger/
```

Happy Coding D1MK4L