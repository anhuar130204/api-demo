import requests

# URL base de la API
BASE_URL = "https://www.dnd5eapi.co"

# Realizar una solicitud GET a la API para obtener la lista de clases
response = requests.get(f"{BASE_URL}/api/classes")

# Comprobar si la solicitud fue exitosa
if response.status_code == 200:
    classes_data = response.json()['results']
    
    # Iterar a través de las clases
    for class_info in classes_data:
        class_url = class_info['url']
        
        # Realizar una solicitud GET a la URL de la clase completa
        response_class = requests.get(f"{BASE_URL}{class_url}")
        
        # Comprobar si la solicitud fue exitosa
        if response_class.status_code == 200:
            class_data = response_class.json()
            
            # Obtener las proficiencias de la clase
            proficiencies = class_data.get("proficiencies", [])
            
            if proficiencies:
                class_name = class_data['name']
                print(f"Proficiencias de la Clase {class_name}:")
                for proficiencia in proficiencies:
                    print(f"- {proficiencia['name']}")
                    
                    # Acceder a /api/proficiencies/skill-stealth
                    if "/api/proficiencies/skill-stealth" in proficiencia['url']:
                        proficiency_url = f"{BASE_URL}{proficiencia['url']}"
                        proficiency_response = requests.get(proficiency_url)
                        
                        # Comprobar si la solicitud fue exitosa
                        if proficiency_response.status_code == 200:
                            proficiency_data = proficiency_response.json()
                            print("\nDetalles de la Proficiencia 'skill-stealth':")
                            print(f"Nombre: {proficiency_data['name']}")
                            print(f"Tipo: {proficiency_data['type']}")
                        else:
                            print("No se pudieron obtener los detalles de la proficiencia 'skill-stealth'.")
        else:
            print(f"No se pudieron obtener los detalles de la clase {class_info['name']}.")
else:
    print("La solicitud a la API falló. Por favor, inténtalo más tarde.")
