from typing import Optional
from jose import jwt, JWTError
from fastapi import Request, HTTPException, status
import time
import os

ALGO = "HS256"
COOKIE_NAME = "session"

def create_token(secret: str, sub: str, username: str, exp_secs: int = 3600) -> str:
    now = int(time.time())
    payload = {"sub": sub, "username": username, "iat": now, "exp": now + exp_secs}
    return jwt.encode(payload, secret, algorithm=ALGO)

def verify_token(secret: str, token: str) -> Optional[dict]:
    try:
        return jwt.decode(token, secret, algorithms=[ALGO])
    except JWTError:
        return None

def require_auth(request: Request, secret: str) -> dict:
    token = request.cookies.get(COOKIE_NAME)
    payload = verify_token(secret, token) if token else None
    if not payload:
        raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail="Unauthorized")
    return payload