# print("Saad Bin Riaz")
# python -m venv venv
from fastapi import FastAPI , HTTPException

app = FastAPI()
students = [
    {"id": 1, "name": "Ali", "age": 20},
    {"id": 2, "name": "Ahmed", "age": 22},
    {"id": 3, "name": "Sara", "age": 19}
]

@app.get("/")
async def main():
    return {"message": "Hello, Backend Engineer!"}


@app.get("/hello")
async def main():
    return {"message": "Hello, Backend Engineer Saad Bin Riaz!"}