

from fastapi import FastAPI

app = FastAPI()


@app.get("/")
def read_root():
    return {"Hello": "World"}

@app.get("/v1/contactos")
async def get_contactos():
    
#TODO READ contactos.CSV
 def leerContactos(self) -> bool: # Metodo para listar los despensa registrados
        try: # Prueba el codigo y si ocurre una Excepcion la atrapa
            with open("contactos.csv", "r") as file: # Abre el archivo para tener acceso a los registros
                reader = csv.DictReader(file, delimiter=",") # Crer un objeto reader para leer los registros separandolos por el delimitador ,
                for row in reader: # Recorre todos los registros encontrados y almacena temporalmente cada uno en row
                    print(f"Registro: {row}") # imprime los datos del registro como un diccionario
            return True # Regresa True si el metodo se ejecuto correctamente
        except Exception as e: # Atrapa cualquier excepcion
            print(f"Error leerContactos() :{e.args}") # Muestra en consola el error que ocurrio
            return False # Regresa False si ocurrio un error en el metodo
            #
#TODO COMVERTIR CONTACTOS JSON ENCODE
# TODO SAVE IN RESPONSE Y MOSTRAR CON LA URI
#response = []
#return response