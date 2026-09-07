from fastapi import FastAPI, HTTPException

app = FastAPI()

students = {
    "S001":{"name":"Ravi","marks":85,"grade":"A"},
    "S002":{"name":"Priya","marks":72,"grade":"B"},
    "S003":{"name":"Arjun","marks":91,"grade":"A+"}
}

@app.get("/student/{student_id}")
def get_student(student_id: str):
    if student_id not in students:
        raise HTTPException(
            status_code = 404,
            detail = f"Student with ID {student_id} does not exists"
        )
        
    return students[student_id]


#Raising exception when data not exist  