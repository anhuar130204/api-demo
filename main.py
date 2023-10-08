import csv
from fastapi import FastAPI, Form, Request, status
from fastapi.responses import JSONResponse
from pydantic import BaseModel
import requests
from typing import Optional
app = FastAPI()


class Contactos:
    def leerContactos(self) -> list:
        try:
            contactos_list = []
            with open("contactos.csv", "r") as file:
                reader = csv.DictReader(file, delimiter=",")
                for row in reader:
                    contactos_list.append(row)
            return contactos_list
        except Exception as e:
            print(f"Error leerContactos(): {e}")
            return []

class Contacto(BaseModel):
    id_contacto: int
    nombre: str
    primer_apellido: str
    segundo_apellido: str
    email: str
    telefono: int


contactos_agregar = []

@app.get("/", summary="Raiz")
async def root(request: Request):
    return {"message": "¡Hola, mundo!"}

@app.get("/v1/contactos")
async def get_contactos(variable_busqueda: Optional[str] = None):
    contacto = Contactos()
    contactos_list = contacto.leerContactos()
    
    if variable_busqueda:
        # Convertir la búsqueda a minúsculas para que sea insensible a mayúsculas y minúsculas
        variable_busqueda = variable_busqueda.lower()
        
        # Filtrar los contactos en función del término de búsqueda
        contactos_filtrados = [
            c for c in contactos_list if (
                (c.get("nombre") or "").lower() == variable_busqueda or
                (c.get("primer_apellido") or "").lower() == variable_busqueda or
                (c.get("segundo_apellido") or "").lower() == variable_busqueda
            )
        ]
        
        return JSONResponse(content=contactos_filtrados)
    else:
        return JSONResponse(content=contactos_list)


@app.put("/v1/contactos")
async def actualizar_contacto(id_contacto: int, contacto_actualizado: dict):
   return JSONResponse(content={"message": "Contacto actualizado"})
"""
@app.post("/v1/contactos")
 async def crear_contacto(
    nombre: str = Form(...),
    primer_apellido: str = Form(...),
    segundo_apellido: str = Form(...),
    email: str = Form(...),
    telefono: int = Form(...)
): """
"""
    #  endpoint para crear un nuevo contacto
    # el contacto nuevo se debe almacenar en un archivo csv    
"""
@app.post("/v1/contactos", status_code=status.HTTP_201_CREATED)
async def post_contacto(contacto:Contacto):
    """
    #  endpoint para crear un nuevo contacto
      
"""
    return contacto
    
    """ nuevo_id = len(contactos_agregar) + 1

    nuevo_contacto = {
        "id_contacto": nuevo_id,
        "nombre": nombre,
        "primer_apellido": primer_apellido,
        "segundo_apellido": segundo_apellido,
        "email": email,
        "telefono": telefono,
    }

  
    contactos_agregar.append(nuevo_contacto)

    with open("contactos.csv", "a", newline="") as file:
        fieldnames = ["id_contacto", "nombre", "primer_apellido", "segundo_apellido", "email", "telefono"]
        writer = csv.DictWriter(file, fieldnames=fieldnames)
        if file.tell() == 0:
            writer.writeheader()
        writer.writerow(nuevo_contacto)

    
    return JSONResponse(content=nuevo_contacto)
 """