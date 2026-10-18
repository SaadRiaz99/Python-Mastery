from pathlib import Path

from fastapi import FastAPI, HTTPException
from fastapi.responses import FileResponse
from model import Student

app = FastAPI()
students = [
    {"id": 1, "name": "Ali", "age": 20},
    {"id": 2, "name": "Ahmed", "age": 22},
    {"id": 3, "name": "Sara", "age": 19},
    {"id": 5, "name": "Muskan", "age": 21}
]

# @app.get("/")
# async def main():
#     return {"message": "Hello, Backend Engineer!"}


# @app.get("/hello")
# async def main():
#     return {"message": "Hello, Backend Engineer Saad Bin Riaz!"}



@app.get("/", include_in_schema=False)
async def student_dashboard():
    return FileResponse(Path(__file__).with_name("index.html"))


@app.get("/students")
async def list_students():
    return students


@app.get("/students/{student_id}")
async def check_student(student_id: int):
    for student in students:
        if student["id"] == student_id:
            return student
    raise HTTPException(status_code=404, detail="Student not found")


@app.post("/students")
def add_student(student: Student):
    students.append(student.model_dump())
    return {
        "message": "Student added successfully",
        "student": student
    }
