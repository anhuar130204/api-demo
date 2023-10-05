import requests
import json
URI = "https://www.dnd5eapi.co/api/classes"




print(f"GET: {response.text}")

response_json = json.loads(response.text)
print("1.-" + f"{response_json['results'][0]['name']}" )
print("2.-" +f"{response_json['results'][1]['name']}")
print("3.-" +f"{response_json['results'][2]['name']}")
print("4.-" +f"{response_json['results'][3]['name']}")
print("5.-" +f"{response_json['results'][4]['name']}")
print("6.-" +f"{response_json['results'][5]['name']}")
print("7.-" +f"{response_json['results'][6]['name']}")
print("8.-" +f"{response_json['results'][7]['name']}")
print("9.-" +f"{response_json['results'][8]['name']}")
print("10.-" +f"{response_json['results'][9]['name']}")
print("11.-" +f"{response_json['results'][10]['name']}")
print("12.-" +f"{response_json['results'][11]['name']}")

numero = int(input("introdusca el numero para poder ver sus capacidades:"))

if numero == 1:
    url = URI +"/barbarian"
     print(f"{response_json['results']}")
elif numero == 2:
     url = URI +"/bard"
     print(f"{response_json['results'][numero]}")
elif numero == 3:
     url = URI +"/cleric"
     print(f"{response_json['results'][numero]}")
elif numero == 4:
     url = URI +"/druid"
     print(f"{response_json['results'][numero]}")
elif numero == 5:
     url = URI +"/fighter"
     print(f"{response_json['results'][numero]}")
elif numero == 6:
     url = URI +"/monk"
     print(f"{response_json['results'][numero]}")
elif numero == 7:
     url = URI +"/paladin"
     print(f"{response_json['results'][numero]}")
elif numero == 8:
     url = URI +"/ranger"
     print(f"{response_json['results'][numero]}")
elif numero == 9:
     url = URI +"/rogue"
     print(f"{response_json['results'][numero]}")
     



