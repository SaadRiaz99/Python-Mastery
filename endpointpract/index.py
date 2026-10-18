# print("Saad Bin Riaz")
# python -m venv venv
from fastapi import FastAPI , HTTPException
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



@app.get("/")
async def student():
    return students

@app.get("/students/{student_id}")
async def check_student(students_id :int):
    for student in students:
        if student["id"] == students_id:
            return student

@app.post("/students")
def add_student(student: Student):
    students.append(student.model_dump())
    return {
        "message": "Student added successfully",
        "student": student
    }
