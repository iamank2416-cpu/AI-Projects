from fastapi import FastAPI

app = FastAPI()

all_coustomers = [
    {"id": 101, "name": "Rashi", "city": "bengaluru", "risk":"low"},
    {"id": 102, "name": "Anshi", "city": "delhi", "risk":"high"},
    {"id": 103, "name": "Khushi", "city": "pune", "risk":"medium"},
    {"id": 104, "name": "Mishi", "city": "mumbai", "risk":"high"},
    {"id": 105, "name": "Shashi", "city": "hyderabad", "risk":"low"}
]

@app.get("/customers")
def get_customers(city:str, risk:str):
    filtered = [
        c for c in all_coustomers
        if c["city"] == city and c["risk"] == risk
    ]
    
    return {
        "city": city,
        "risk": risk,
        "count": len(filtered),
        "results": filtered
    }