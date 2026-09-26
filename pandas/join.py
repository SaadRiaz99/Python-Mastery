import pandas as pd

students = {
    "student_id": [1, 2, 3, 4],
    "name": ["Ali", "Ayesha", "Hamza", "Sara"]
}

courses = {
    "student_id": [1, 2, 5],
    "course": ["Math", "Science", "English"]
}

fees = {
    "student_id": [1, 3, 4],
    "fee_status": ["Paid", "Pending", "Paid"]
}

attendance = {
    "student_id": [2, 3, 4, 6],
    "attendance": [90, 85, 88, 92]
}

df_students = pd.DataFrame(students)
df_courses = pd.DataFrame(courses)
df_fees = pd.DataFrame(fees)
df_attendance = pd.DataFrame(attendance)
print("Students:")
print(df_students)
print("\nCourses:")
print(df_courses)
print("\nFees:")
print(df_fees)
print("\nAttendance:")
print(df_attendance)

# print("\nInner merge on student_id:")
# result = df_students.merge(df_courses, on="student_id", how="inner")
# print(result)

print("\n Data Merged on student_id")
result = df_students.merge(df_courses , on ="student_id" ,  how='right')
result  = result.merge(df_fees, on="student_id", how="right")
result = result.merge(df_attendance, on="student_id",how="right")
print(result)