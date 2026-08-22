from fastapi import Depends, FastAPI, HTTPException, Response
from pydantic import BaseModel, EmailStr

from app.auth import login_user, signup_user, supabase
from app.dependencies import get_current_user


app = FastAPI(
    title="Auth Login Protect API",
    version="1.0.0"
)


class AuthRequest(BaseModel):
    email: EmailStr
    password: str


@app.get("/")
def root():
    return {
        "name": "Auth Login Protect API",
        "version": "1.0.0"
    }


@app.post("/auth/signup", status_code=201)
def signup(data: AuthRequest):
    if not data.email or not data.password:
        raise HTTPException(
            status_code=400,
            detail="Email and password are required"
        )

    try:
        response = signup_user(
            data.email,
            data.password
        )

        if response.user is None:
            raise HTTPException(
                status_code=400,
                detail="Unable to create user"
            )

        return {
            "user": response.user
        }

    except HTTPException:
        raise

    except Exception:
        raise HTTPException(
            status_code=400,
            detail="Unable to create user"
        )


@app.post("/auth/login")
def login(data: AuthRequest):
    if not data.email or not data.password:
        raise HTTPException(
            status_code=400,
            detail="Email and password are required"
        )

    try:
        response = login_user(
            data.email,
            data.password
        )

        if response.session is None:
            raise HTTPException(
                status_code=401,
                detail="Invalid login credentials"
            )

        return {
            "access_token": response.session.access_token,
            "refresh_token": response.session.refresh_token
        }

    except HTTPException:
        raise

    except Exception:
        raise HTTPException(
            status_code=401,
            detail="Invalid login credentials"
        )


@app.get("/public/info")
def public_info():
    return {
        "message": "Welcome stranger! This info is public."
    }


@app.get("/protected/profile")
def protected_profile(
    user=Depends(get_current_user)
):
    return {
        "id": user.id,
        "email": user.email,
        "created_at": user.created_at
    }


@app.get("/protected/dashboard")
def protected_dashboard(
    user=Depends(get_current_user)
):
    return {
        "message": "Welcome to your protected dashboard.",
        "user_id": user.id
    }


@app.post("/auth/logout", status_code=204)
def logout(
    user=Depends(get_current_user)
):
    try:
        supabase.auth.sign_out()
        return Response(status_code=204)

    except Exception:
        raise HTTPException(
            status_code=401,
            detail="Unable to logout"
        )