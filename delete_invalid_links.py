from link_shortner import LinkShortner
from json_manager import JsonManager
import requests


payload = {}
headers = {}


entities=LinkShortner.get_all()
#create a new file
for entity in entities:
    print(entity["url"])
    url=entity["url"]
    try:
        response = requests.request("GET", url, headers=headers, data=payload)
        if response.status_code in [200, 201]:
            print("OK")
            # add into a new file
    except:
        pass
            
#save new file as links.json