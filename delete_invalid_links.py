from link_shortner import LinkShortner
from json_manager import JsonManager
import requests


payload = {}
headers = {}

new_url_entities=[]
entities=LinkShortner.get_all()
#create a new file
for entity in entities:
    print(entity["url"])
    url=entity["url"]
    try:
        response = requests.request("GET", url, headers=headers, data=payload)
        if response.status_code in [200, 201]:
            new_url_entities.append(entity)
            print("OK")
            break

    except:
        pass
            
#save new file as links.json
JsonManager.write(new_url_entities,)