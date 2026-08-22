# Auth Login Protect API

A secure authentication API built with **FastAPI** and **Supabase Auth**.

This project implements user registration and login using Supabase Authentication and will progressively add protected routes, JWT verification, reusable authentication dependencies, logout, and Swagger UI bearer authentication.

## Tech Stack

* Python 3.10+
* FastAPI
* Supabase Auth
* Supabase Python SDK
* Uvicorn
* Git & GitHub

## Project Structure

```text
auth-login-protect-api/
│
├── app/
│   ├── __init__.py
│   ├── main.py
│   ├── auth.py
│   └── dependencies.py
│
├── .env
├── .gitignore
├── requirements.txt
└── README.md
```

## Setup

### 1. Clone the repository

```bash
git clone <your-github-repository-url>
cd auth-login-protect-api
```

### 2. Create a virtual environment

```bash
python -m venv .venv
```

Activate it on Windows:

```powershell
.venv\Scripts\activate
```

### 3. Install dependencies

```bash
pip install -r requirements.txt
```

### 4. Configure Supabase

Create a Supabase project and obtain the **Project URL** and client **Publishable/Anon key** from the Supabase dashboard.

Create a `.env` file in the project root:

```env
SUPABASE_URL=your_project_url
SUPABASE_KEY=your_publishable_or_anon_key
```

**Never commit `.env` or Supabase secret/service-role keys to GitHub.**

## Run the API

Start the development server with:

```bash
uvicorn app.main:app --reload
```

The API will be available at:

```text
http://localhost:8000
```

Interactive Swagger documentation:

```text
http://localhost:8000/docs
```

## Current Endpoints

| Method | Endpoint               | Authentication | Status      |
| ------ | ---------------------- | -------------- | ----------- |
| GET    | `/`                    | No             | Implemented |
| POST   | `/auth/signup`         | No             | Implemented |
| POST   | `/auth/login`          | No             | Implemented |
| GET    | `/public/info`         | No             | Planned     |
| GET    | `/protected/profile`   | Bearer Token   | Planned     |
| GET    | `/protected/dashboard` | Bearer Token   | Planned     |
| POST   | `/auth/logout`         | Bearer Token   | Planned     |

## Authentication Flow

The authentication flow uses Supabase as the Identity Provider:

```text
Client
   │
   │ Email + Password
   ▼
Supabase Auth
   │
   │ Access Token (JWT)
   ▼
Client
   │
   │ Authorization: Bearer <token>
   ▼
FastAPI
   │
   │ Verify token with Supabase
   ▼
Protected API Resource
```


## Security

Sensitive environment variables are stored in `.env` and excluded from Git using `.gitignore`.

Do not commit:

* Supabase secret keys
* Service-role keys
* `.env` files
* Access tokens
* Refresh tokens

## License

This project was created as part of a Backend AI Engineering assignment.
