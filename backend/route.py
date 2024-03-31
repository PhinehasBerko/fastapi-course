import fastapi


app = fastapi.FastAPI()

@app.get('/')
async def home(x:int,y:int,z:int):
    if z == 0:
        pass
    value = (x +y)/z
    result = {
        'value':value
    }
    return fastapi.responses.JSONResponse(result)

def full_name(first_name,last_name):
    full_name = first_name.up