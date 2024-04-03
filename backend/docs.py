from fastapi import FastAPI,Query,File,UploadFile,Form
from pydantic import BaseModel, Field
from typing import Optional
import fastapi

app = fastapi.FastAPI()


# ********** schema**********
class User(BaseModel):
    id: str
    user: str = Field(min_length =5, max_length = 10, pattern = r'^[a-zA-Z0-9]+$')
    

@app.post("/user")
async def create_user(user:User):
    return {"username":user}

@app.get("/books")
async def read_book(title:str,author:str = None, genre:str = None):
    return {"title":title, "author":author, "genre":genre}

@app.get("/restaurants")
async def find_restaurants(cuisine: str = Query(None), vegetarian: bool = Query(False)):
    return {"cuisine":cuisine, "vegetarian":vegetarian}

@app.post('/events/{event_id}')
async def handle_form_upload(file: UploadFile = File(...), notes: str = Form(...)):
    content = await file.read()

    num_lines = content.decode("utf-8").count("\n")+1

    file_size = len(content)

    await file.seek(0)
    return {
        "file_name": file.filename,
        "file_size":file_size,
        "number_of_lines":num_lines,
        "notes":notes
    }
