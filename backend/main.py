from fastapi import FastAPI, HTTPException, status
from fastapi.security import OAuth2PasswordBearer, OAuth2PasswordRequestForm
from fastapi.middleware.cors import CORSMiddleware
from jose import JWTError, jwt
from passlib.context import CryptContext
from pydantic import BaseModel
from datetime import datetime, timedelta
from typing import Optional, List, Dict
import os

SECRET_KEY = os.environ.get("SECRET_KEY", "secret-key-change-in-production")
ALGORITHM = "HS256"
ACCESS_TOKEN_EXPIRE_MINUTES = 30

pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")
oauth2_scheme = OAuth2PasswordBearer(tokenUrl="api/auth/login")

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

users_db = {}
tasks_db = []
next_user_id = 1
next_task_id = 1

def verify_password(plain_password, hashed_password):
    return pwd_context.verify(plain_password, hashed_password)

def get_password_hash(password):
    return pwd_context.hash(password)

def create_access_token(data: dict, expires_delta: Optional[timedelta] = None):
    to_encode = data.copy()
    if expires_delta:
        expire = datetime.utcnow() + expires_delta
    else:
        expire = datetime.utcnow() + timedelta(minutes=15)
    to_encode.update({"exp": expire})
    encoded_jwt = jwt.encode(to_encode, SECRET_KEY, algorithm=ALGORITHM)
    return encoded_jwt

async def get_current_user(token: str = Depends(oauth2_scheme)):
    credentials_exception = HTTPException(
        status_code=status.HTTP_401_UNAUTHORIZED,
        detail="Could not validate credentials",
        headers={"WWW-Authenticate": "Bearer"},
    )
    try:
        payload = jwt.decode(token, SECRET_KEY, algorithms=[ALGORITHM])
        username: str = payload.get("sub")
        if username is None:
            raise credentials_exception
    except JWTError:
        raise credentials_exception
    user = users_db.get(username)
    if user is None:
        raise credentials_exception
    return user

from fastapi import Depends

class UserCreate(BaseModel):
    username: str
    password: str
    email: str
    role: str = "student"

class UserResponse(BaseModel):
    id: int
    username: str
    email: str
    role: str

class TaskCreate(BaseModel):
    title: str
    description: str
    deadline: Optional[datetime] = None

class TaskResponse(BaseModel):
    id: int
    title: str
    description: str
    status: str
    deadline: Optional[datetime]

@app.post("/api/auth/login")
async def login(form_data: OAuth2PasswordRequestForm = Depends()):
    user = users_db.get(form_data.username)
    if not user or not verify_password(form_data.password, user["hashed_password"]):
        raise HTTPException(status_code=400, detail="Incorrect username or password")
    access_token_expires = timedelta(minutes=ACCESS_TOKEN_EXPIRE_MINUTES)
    access_token = create_access_token(data={"sub": user["username"]}, expires_delta=access_token_expires)
    return {"access_token": access_token, "token_type": "bearer", "role": user["role"]}

@app.post("/api/auth/register", response_model=UserResponse)
async def register(user: UserCreate):
    if user.username in users_db:
        raise HTTPException(status_code=400, detail="Username already registered")
    global next_user_id
    hashed_password = get_password_hash(user.password)
    users_db[user.username] = {
        "id": next_user_id,
        "username": user.username,
        "email": user.email,
        "hashed_password": hashed_password,
        "role": user.role
    }
    next_user_id += 1
    return users_db[user.username]

@app.get("/api/users/me", response_model=UserResponse)
async def read_users_me(current_user: dict = Depends(get_current_user)):
    return current_user

@app.post("/api/text/generate")
async def generate_text(prompt: str, length: str = "medium"):
    return {"content": f"这是根据您的提示生成的{length}文本：\n\n{prompt}\n\n---\n\n以上内容是基于您的输入自动生成的示例文本。实际应用中会调用真实的AI模型进行内容创作。"}

@app.post("/api/image/generate")
async def generate_image(prompt: str, resolution: str = "1024x1024"):
    import urllib.parse
    encoded_prompt = urllib.parse.quote(prompt)
    return {"url": f"https://neeko-copilot.bytedance.net/api/text_to_image?prompt={encoded_prompt}&image_size=square"}

@app.post("/api/video/generate")
async def generate_video(prompt: str, duration: int = 5):
    return {"url": "", "message": f"视频生成请求已接收，预计时长{duration}秒。实际应用中会调用AI视频生成模型。"}

@app.post("/api/audio/generate")
async def generate_audio(text: str, voice: str = "female"):
    return {"url": "", "message": f"音频生成请求已接收，使用{voice}声音类型。实际应用中会调用TTS语音合成服务。"}

@app.get("/api/tasks", response_model=List[TaskResponse])
async def get_tasks():
    return tasks_db

@app.post("/api/tasks", response_model=TaskResponse)
async def create_task(task: TaskCreate):
    global next_task_id
    new_task = {
        "id": next_task_id,
        "title": task.title,
        "description": task.description,
        "status": "未开始",
        "deadline": task.deadline
    }
    tasks_db.append(new_task)
    next_task_id += 1
    return new_task

@app.put("/api/tasks/{task_id}", response_model=TaskResponse)
async def update_task(task_id: int, task: TaskCreate):
    for t in tasks_db:
        if t["id"] == task_id:
            t["title"] = task.title
            t["description"] = task.description
            t["deadline"] = task.deadline
            return t
    raise HTTPException(status_code=404, detail="Task not found")

@app.delete("/api/tasks/{task_id}")
async def delete_task(task_id: int):
    global tasks_db
    for i, t in enumerate(tasks_db):
        if t["id"] == task_id:
            del tasks_db[i]
            return {"message": "Task deleted"}
    raise HTTPException(status_code=404, detail="Task not found")

@app.get("/api/resources")
async def get_resources(category: Optional[str] = None):
    resources = [
        {"id": 1, "title": "文本生成入门", "description": "学习如何使用文本生成功能", "category": "docs"},
        {"id": 2, "title": "图片生成指南", "description": "掌握图片生成技巧", "category": "docs"},
        {"id": 3, "title": "视频生成教程", "description": "学习视频生成方法", "category": "docs"}
    ]
    if category:
        return [r for r in resources if r["category"] == category]
    return resources

@app.get("/api/statistics/overview")
async def get_statistics():
    return {
        "total_users": len(users_db),
        "total_tasks": len(tasks_db),
        "total_generations": 500,
        "active_users": 20
    }

@app.post("/api/admin/users", response_model=UserResponse)
async def create_admin_user(user: UserCreate):
    if user.username in users_db:
        raise HTTPException(status_code=400, detail="Username already registered")
    global next_user_id
    hashed_password = get_password_hash(user.password)
    users_db[user.username] = {
        "id": next_user_id,
        "username": user.username,
        "email": user.email,
        "hashed_password": hashed_password,
        "role": user.role
    }
    next_user_id += 1
    return users_db[user.username]

@app.delete("/api/admin/users/{user_id}")
async def delete_admin_user(user_id: int):
    global users_db
    to_delete = None
    for username, user in users_db.items():
        if user["id"] == user_id:
            to_delete = username
            break
    if to_delete:
        del users_db[to_delete]
        return {"message": "User deleted"}
    raise HTTPException(status_code=404, detail="User not found")

@app.get("/api/admin/users")
async def get_admin_users():
    return list(users_db.values())

@app.get("/")
async def root():
    return {"message": "AIGC Training Platform API is running"}

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)