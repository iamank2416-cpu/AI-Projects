from fastapi import FastAPI, HTTPException
from pydantic import BaseModel

app = FastAPI()

students = {
    "S001":{"name":"Ravi","marks":85,"grade":"A"},
    "S002":{"name":"Priya","marks":72,"grade":"B"},
    "S003":{"name":"Arjun","marks":91,"grade":"A+"}
}

class MarksSubmission(BaseModel):
    student_id: str
    marks: int
    subject: str

@app.get("/student/{student_id}")
def get_student(student_id: str):
    if student_id not in students:
        raise HTTPException(
            status_code = 404,
            detail = f"Student with ID {student_id} does not exists"
        )
        
    return students[student_id]

@app.post("/submit-marks")
def submit_marks(submission: MarksSubmission):
    #error1 students does not exists
    if submission.student_id not in students:
        raise HTTPException(
            status_code=404,
            detail=f"student with ID {submission.student_id} does not exists"
        )
        
    #error2 Valid range marks 0-100
    if submission.marks < 0 or submission.marks > 100:
        raise HTTPException(
            status_code=400,
            detail={
                "error": "marks must be between 0 and 100",
                "marks_received": submission.marks,
                "fix": "enter a valid value between 0 and 100"
            }
        )
        
    #error3 Subject name empty
    if submission.subject.strip() == "":
        raise HTTPException(
            status_code=400,
            detail="subject name cannot be empty"
        )
        
    #If everything good
    try:
        students[submission.student_id]["marks"] = submission.marks
    
        return {
            "message":"marks submitted successfully.",
            "student":students[submission.student_id]["name"],
            "subject":submission.subject,
            "marks":submission.marks
        }

    except Exception as e:
        raise HTTPException(
            status_code = 500,
            detail=f"Something went wrong on our side: {str(e)} "
        )            