
from json_manager import JsonManager
import uuid

class LinkShortner():

    @classmethod
    def get_url_by_id(self,id):
        link_entities=JsonManager.read()
        for link_entity in link_entities:
            if link_entity["id"]==id:
                return link_entity["url"]
        raise Exception("Your ID is not found")

    @classmethod
    def shorten(self,link:str):
        
        url_entities=JasonManager.read()
        ids=[entity["id"] for enriry in url_entities]
        unique_ids=list(set(ids)))

        while unique_id in unique_ids:
            unique_id=str(uuid.uuid4())[:8]
      
        new_entity={"id":unique_id,"url":link}
        link_entities=JsonManager.read()
        link_entities.append(new_entity)
        JsonManager.write(link_entities)
        return unique_id