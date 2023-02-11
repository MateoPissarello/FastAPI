from fastapi import FastAPI
app = FastAPI()
@app.get("/") #Con el @app accedemos al contexto de fastAPI y usamos el get (peticion HTTP) con una barra que indica que es la raiz de nuestra pagina
async def root(): #el async indica que la funcion es asincrona, siempre al llamar a un servidor la funcion debe ser asincrona
    return "Hola FastAPI"
@app.get("/mensaje")
async def enviar_mensaje():
    return {"mensaje" : "Hola"}