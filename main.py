import csv
from fastapi import FastAPI, Form, Request
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
    id_contacto: int
    nombre: str
    primer_apellido: str
    segundo_apellido: str
    email: str
    telefono: int

# Almacenar los contactos en una lista en memoria
contactos_agregar = []

@app.get("/", summary="Raiz")
async def root(request: Request):
    return {"message": "¡Hola, mundo!"}

@app.get("/v1/contactos")
async def get_contactos():
    contacto = Contactos()
    contactos_list = contacto.leerContactos()
    return JSONResponse(content=contactos_list)

@app.put("/v1/contactos/actualizar")
async def actualizar_contacto(id_contacto: int, contacto_actualizado: dict):
    # Implementa la lógica para actualizar el contacto aquí
    # Debes leer el CSV, encontrar y actualizar el contacto, y luego guardar el CSV nuevamente
    return JSONResponse(content={"message": "Contacto actualizado"})

@app.post("/v1/contactos/agregar")
async def crear_contacto(
    nombre: str = Form(...),
    primer_apellido: str = Form(...),
    segundo_apellido: str = Form(...),
    email: str = Form(...),
    telefono: int = Form(...)
):
    """
    #  endpoint para crear un nuevo contacto
    # el contacto nuevo se debe almacenar en un archivo csv    
 """

    # Generar un nuevo ID para el contacto (puede ser simplemente el índice en la lista + 1)
    nuevo_id = len(contactos_agregar) + 1

    # Crear un diccionario con los datos del nuevo contacto
    nuevo_contacto = {
        "id_contacto": nuevo_id,
        "nombre": nombre,
        "primer_apellido": primer_apellido,
        "segundo_apellido": segundo_apellido,
        "email": email,
        "telefono": telefono,
    }

    # Agregar el nuevo contacto a la lista de contactos
    contactos_agregar.append(nuevo_contacto)

    # Guardar el nuevo contacto en el archivo CSV
    with open("contactos.csv", "a", newline="") as file:
        fieldnames = ["id_contacto", "nombre", "primer_apellido", "segundo_apellido", "email", "telefono"]
        writer = csv.DictWriter(file, fieldnames=fieldnames)
        if file.tell() == 0:
            writer.writeheader()
        writer.writerow(nuevo_contacto)

    # Devolver una respuesta con el nuevo contacto
    return JSONResponse(content=nuevo_contacto)
