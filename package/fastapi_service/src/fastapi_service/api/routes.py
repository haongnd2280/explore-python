from fastapi import APIRouter


router = APIRouter()

@router.get("/")
def home():
    return {"message": "Welcome to my FastAPI Service!"}

@router.get("/hello/{name}")
def say_hello(name: str):
    return {"message": f"Hello, {name}!"}
