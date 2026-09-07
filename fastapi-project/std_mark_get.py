from fastapi import FastAPI

app = FastAPI()

students = {
    "S001":{"name":"Ravi","marks":85,"grade":"A"},
    "S002":{"name":"Priya","marks":72,"grade":"B"},
    "S003":{"name":"Arjun","marks":91,"grade":"A+"}
}

@app.get("/student/{student_id}")
def get_student(student_id: str):
    return students[student_id]

#Internal server error if student_id does not exist ex: S004