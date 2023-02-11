from fastapi import FastAPI
from pydantic import BaseModel
app_usuarios = FastAPI()
## Definir una entidad 
class Usuario(BaseModel):
    id: int
    usuario_name: str
    usuario_lastname: str
    usuario_age: int
    usuario_phone: str
    
usuarios_fakedb = [Usuario(id=1,usuario_name="Mateo", usuario_lastname="Pissarello", usuario_age=18, usuario_phone="3193522158"),
                   Usuario(id=2,usuario_name="Yuliana", usuario_lastname="Peña", usuario_age=16, usuario_phone="3193522158")]
#http://127.0.0.1:8000

@app_usuarios.get("/users")
async def userclass():
    return usuarios_fakedb
#PARAMETROS DE PATH (En el codigo de abajo vamos a pasar el id como parametro de path para recuperar un usuario)
@app_usuarios.get("/user/{id}")
async def getUserWithId(id:int):
    return search_user(id)
## PARAMETROS POR QUERY
@app_usuarios.get("/userquery/")
async def getUserWithId(id:int):
    return search_user(id)

def search_user(id: int):
    users = filter(lambda user: user.id == id, usuarios_fakedb )
    try:   
        return list(users)[0] 
    except:
        return {"error":"No se ha encontrado el usuario"}
