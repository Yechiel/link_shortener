import json
import os

FILE_NAME=os.environ["LINKS_PATH"]
#./data/links.json"

class JsonManager:

    @classmethod
    def read(self,filename:str =FILE_NAME):
        with open(filename,"r") as f:
            dict_list=json.load(f)
        return dict_list

    @classmethod
    def write(self,dict_list,filename:str = FILE_NAME):
        try:
            with open(filename,"w") as f:
                json.dump(dict_list,f)
                return True
        except Exception() as e:
                return False        
