import functions as f
from typing import Union
from fastapi import FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


class Semester(BaseModel):
    semester: int
    code: str
    name: str
    ects: float


@app.get("/")
def read_root():
    return {"Hello": "World"}


@app.get("/items/{item_id}")
def read_item(item_id: int, q: Union[str, None] = None):
    return {"item_id": item_id, "q": q}


@app.get("/semesters")
async def read_semesters():
    semesters = f.read_semesters()
    return {"semesters": semesters}


@app.post("/semesters/submit")
async def write_semesters(semester: Semester):
    try:
        print(semester)
        f.write_semester(semester.semester, semester.code,
                         semester.name, semester.ects)
        return "success"
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))


@app.get("/courses")
async def read_courses():
    courses = f.read_courses()
    return {"courses": courses}
