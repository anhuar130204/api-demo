import csv
import json
from fastapi import FastAPI, status
from fastapi.responses import JSONResponse
from pydantic import BaseModel
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

class ContactoCreate(BaseModel):
    nombre: str
    primer_apellido: str
    segundo_apellido: str
    email: str
    telefono: int

# Almacenar los contactos en una lista en memoria
contactos_agregar = []
@app.get(
    "/", 
    status_code=status.HTTP_200_OK, 
    description="endpoint raiz", 
    summary="raiz")
async def root():
    """
    #endpoint raiz
    ##334 status prueba
    ##CO
    """
    return {"message": "¡Hola, mundo!"}
@app.get("/v1/contactos", status_code=status.HTTP_201_CREATED)

async def get_contactos():
    contacto = Contactos()
    contactos_list = contacto.leerContactos()
    return JSONResponse(content=contactos_list)

@app.put("/v1/contactos/actualizar", status_code=status.HTTP_204_NO_CONTENT)
async def actualizar_contacto(id_contacto: int, contacto_actualizado: dict):
    """
    Actualiza un contacto por su ID.
    :param id_contacto: El ID del contacto a actualizar.
    :param contacto_actualizado: Los nuevos datos del contacto en formato JSON.
    :return: Respuesta 204  si se actualiza correctamente.
    """
    # Implementa la lógica para actualizar el contacto aquí
    # Debes leer el CSV, encontrar y actualizar el contacto, y luego guardar el CSV nuevamente
    return JSONResponse(content={"message": "Contacto actualizado"})


@app.post("/v1/contactos/agregar", status_code=status.HTTP_201_CREATED)
async def crear_contacto(contacto: ContactoCreate):
    """
    Crea un nuevo contacto.
    :param contacto: Datos del nuevo contacto en formato JSON.
    :return: Respuesta 201 Created con los datos del contacto creado.
    """
    # Puedes validar los datos del contacto aquí si es necesario
    # Por ejemplo, verificar si el email es único

    # Generar un nuevo ID para el contacto (puede ser simplemente el índice en la lista + 1)
    nuevo_id = len(contactos_agregar) + 1

    # Crear un diccionario con los datos del nuevo contacto
    nuevo_contacto = {
        "id_contacto": nuevo_id,
        **contacto.dict()
    }

    # Agregar el nuevo contacto a la lista de contactos
    contactos_agregar.append(nuevo_contacto)

    # Devolver una respuesta con el nuevo contacto
    return JSONResponse(content=nuevo_contacto, status_code=status.HTTP_201_CREATED)