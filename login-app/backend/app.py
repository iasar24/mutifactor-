from fastapi import FastAPI, Response, Depends, Request, HTTPException, status
from fastapi.middleware.cors import CORSMiddleware
from dotenv import load_dotenv
import os
from models import LoginRequest, LoginResponse, Message
from storage import seed_demo_user, find_user_by_username
from auth import create_token, require_auth
from passlib.hash import bcrypt

load_dotenv()
JWT_SECRET = os.getenv("JWT_SECRET", "dev_secret_change_me")
ENV = os.getenv("ENV", "dev")
SECURE_COOKIE = ENV == "prod"

app = FastAPI(title="Login API")

# Allow React dev server during development
app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:5173", "http://127.0.0.1:5173"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

seed_demo_user()

@app.post("/api/login", response_model=LoginResponse)
def login(body: LoginRequest, response: Response):
    user = find_user_by_username(body.username)
    if not user or not bcrypt.verify(body.password, user.password_hash):
        raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail="Invalid username or password")

    token = create_token(JWT_SECRET, sub=user.id, username=user.username, exp_secs=3600)
    response.set_cookie(
        key="session",
        value=token,
        httponly=True,
        secure=SECURE_COOKIE,
        samesite="lax",
        max_age=3600,
        path="/",
    )
    return {"ok": True}

@app.post("/api/logout", response_model=Message)
def logout(response: Response):
    response.delete_cookie("session", path="/")
    return {"message": "Logged out"}

@app.get("/api/welcome", response_model=Message)
def welcome(request: Request):
    payload = require_auth(request, JWT_SECRET)
    return {"message": f"Welcome, {payload.get('username')}"}