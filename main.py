import csv
import json
from fastapi import FastAPI
from fastapi.responses import JSONResponse

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

def convertir_a_json(contactos_list):
    return json.dumps(contactos_list, indent=4)

@app.get("/")
def read_root():
    return {"Hello": "World"}

@app.get("/v1/contactos")
async def get_contactos():
    contacto = Contactos()
    contactos_list = contacto.leerContactos()
    return JSONResponse(content=contactos_list)