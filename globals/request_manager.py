from dataclasses import dataclass
import requests

@dataclass()
class Action:
    url:str
    data:dict=None
    is_ok=None

    def post(self)->None:
        req = requests.post(self.url,data=self.data)
        self.is_ok = (req.status_code == 200)
        
    
    def get (self) : 
        req = requests.get(self.url)
        self.is_ok = (req.status_code == 200)
        return req.json()
    
    def delete(self):
        req = requests.delete(self.url,data=self.data)
        self.is_ok = (req.status_code == 200)
        return req.json()
