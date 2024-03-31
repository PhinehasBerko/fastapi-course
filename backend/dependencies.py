from fastapi import FastAPI, HTTPException, File, UploadFile,Form
from datetime import date
from typing import Optional

app = FastAPI()

events_db = [
    {"event_id":1, 'name':'Tech Confence','date':'2023-12-12'},
    {"event_id":2, 'name':'Music  Fest','date':'2023-18-12'},
    {"event_id":3, 'name':'Tech Dev','date':'2023-12-07'}
]

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
