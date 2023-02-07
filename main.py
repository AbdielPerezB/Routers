#Importamos nuestro framwork
from fastapi import FastAPI
#Importamos nuestros 10 routers
from allRouters import router1, router2, router3

#Levantamos nuestra instancia de fastAPI
app = FastAPI()

#Incluimos los 10 routers
app.include_router(router1.routerAutos)
app.include_router(router2.routerUsuario)
app.include_router(router3.routerAnimals)


#Hcaemos un path del main (opcional)
@app.get("/")
async def imprimir():
    return "Hola mundo"