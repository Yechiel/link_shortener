import json


class JsonManager:

    @classmethod
    def read(self,filename:str ="links.json"):
        with open(filename,"r") as f:
            dict_list=json.load(f)
        return dict_list

    @classmethod
    def write(self,dict_list,filename:str = "links.json"):
        try:
            with open(filename,"w") as f:
                json.dump(dict_list,f)
                return True
        except Exception() as e:
                return False        
