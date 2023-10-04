import requests
URI = "http://localhost:8000/v1/contactos"
response = requests.get(URI)
print(f"GET : {response.text}")
print(f"GET : {response.status_code}")

data = {
  "id_contacto": 2,
  "nombre": "fernandos",
  "primer_apellido": "lopez",
  "segundo_apellido": "solis",
  "email": "anhaur@gmail.com",
  "telefono": 1234567890
}
response = requests.post(URI, json=data)
print(f"POST :{response.text}")
print(f"POST :{response.status_code}")