from fastapi import FastAPI , HTTPException
from fastapi.middleware.cors import CORSMiddleware
from database import *
app = FastAPI()

origins = ['http://localhost:3000']

app.add_middleware(
    CORSMiddleware,
    allow_origins = origins,
    allow_credentials = True,
    allow_methods = ['*'],
    allow_headers=['*'],
)

@app.get('/')
def read():
    return {'hello':'hello'}


@app.get('/api/g')
async def get_g():
    responce = await fetch_all()
    return responce

@app.get('/api/g/{item_id}' , response_model=B)
async def get_u_v(item_id : str ):
    responce = await fetch(item_id)
    if responce:
        return responce
    raise   HTTPException(404, 'no crud')


from fastapi import HTTPException

@app.post('/api/p', response_model=str)
async def get_g_v(todo: B):
    response = await create_t(todo.dict())  # Use `create_t(todo)` directly
    if response:
        print(response)
        return "created"
    raise HTTPException(400, 'Not available CRUD')





@app.put('/api/u/{item_id}/' , response_model=B)
async def get_p_v(item_id :str , dis : str):
    responce = await up(item_id , dis)
    if responce:
        return responce
    raise HTTPException(404,'not crud')


@app.delete('/api/d/{item_id}', response_model=str)
async def get_d_v(item_id: str):
    response = await d(item_id)
    
    if response:
        return "crud deleted successfully from the database of crud of collection cu_li"
    raise HTTPException(404, "No crud found")


@app.delete('/api/d')
async def get_d():
    response = await de()
    
    if response:
        return "crud deleted successfully from the database of crud of collection cu_li"
    raise HTTPException(404, "No crud found")