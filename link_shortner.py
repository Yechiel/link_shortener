
from json_manager import JsonManager
from utils.generate_id import generate_id
from utils.is_unique import is_unique

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
        url_entities=JsonManager.read()
        ids=[entity["id"] for entity in url_entities]
        unique_ids=list(set(ids))
        unique_id=generate_id()
        while not is_unique(unique_id,unique_ids):
            unique_id=generate_id()
        new_entity={"id":unique_id,"url":link}
        link_entities=JsonManager.read()
        link_entities.append(new_entity)
        JsonManager.write(link_entities)
        return unique_id