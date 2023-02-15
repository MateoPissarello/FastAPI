from fastapi import FastAPI, HTTPException
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
#PARAMETROS DE PATH (En el codigo de abajo vamos a pasar el id como parametro de path para recuperar un usuario), es una buena practica colocar como parametros por path aquellos que son obligatorios
@app_usuarios.get("/user/{id}")
async def getUserWithId(id:int):
    return search_user(id)
## PARAMETROS POR QUERY, es una buena practica utilizar los parametros por query cuando algunos parametros puedens ser opcionales 
@app_usuarios.get("/userquery/")
async def getUserWithId(id:int):
    return search_user(id)



#POSTS
@app_usuarios.post("/user/", status_code=201)
async def user(user: Usuario):
    if type(search_user(user.id)) == Usuario:
        raise HTTPException(status_code=204,detail="El usuario ya existe")
    usuarios_fakedb.append(user)
    return user

#PUT
@app_usuarios.put("/user/")
async def user(user:Usuario):
    for index, saved_user in enumerate(usuarios_fakedb):
        found = False
        if saved_user.id == user.id:
            usuarios_fakedb[index] = user
            found = True
    if not found:
        return {"error": "El usuario no ha sido actualizado"}
    else:
        return user



def search_user(id: int):
    users = filter(lambda user: user.id == id, usuarios_fakedb )
    try:   
        return list(users)[0] 
    except:
        return {"error":"No se ha encontrado el usuario"}

@app_usuarios.delete("/user/{id}")
async def user(id:int):
    found = False
    for index, saved_user in enumerate(usuarios_fakedb):
        if saved_user.id == id:
            del usuarios_fakedb[index]
            found = True
    if not found:
        return {"error":"No se ha encontrado el usuario"}
    return {"mensaje":"Se ha eliminado exitosamente"}
