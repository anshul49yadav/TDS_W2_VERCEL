from fastapi import FastAPI
from fastapi.responses import JSONResponse
import os
from fastapi.middleware.cors import CORSMiddleware

# Dummy data - marks of 100 students (for example)
student_marks = {
    "Alice": 10,
    "Bob": 20,
    "Charlie": 30,
    "David": 40,
    "Eve": 50,
    # Add more students as needed.
}

app = FastAPI()

@app.get("/api")
async def get_marks(name: list[str]):
    marks = []
    for n in name:
        marks.append(student_marks.get(n, None))  # Get marks or None if not found.
    return JSONResponse(content={"marks": marks})


app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # Allows all origins
    allow_credentials=True,
    allow_methods=["*"],  # Allows all methods
    allow_headers=["*"],  # Allows all headers
)
