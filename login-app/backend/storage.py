from typing import Optional, Dict
from passlib.hash import bcrypt

class User:
    def __init__(self, user_id: str, username: str, password_hash: str):
        self.id = user_id
        self.username = username
        self.password_hash = password_hash

# In-memory user store for demo
USERS: Dict[str, User] = {}

def seed_demo_user() -> None:
    if "demo" not in USERS:
        USERS["demo"] = User("1", "demo", bcrypt.hash("P@ssw0rd!"))

def find_user_by_username(username: str) -> Optional[User]:
    key = username.lower()
    for u in USERS.values():
        if u.username.lower() == key:
            return u
    return None