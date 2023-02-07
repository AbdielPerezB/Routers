#Importamos nuestro framwork
from fastapi import FastAPI
#Importamos nuestros 10 routers
from allRouters import router1

#Levantamos nuestra instancia de fastAPI
app = FastAPI()

#Incluimos los 10 routers
app.include_router(router1.routerAutos)


#Hcaemos un path del main (opcional)
@app.get("/")
async def imprimir():
    return "Hola mundo"