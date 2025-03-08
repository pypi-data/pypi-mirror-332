import requests
import json




class Server:
    base_url = "https://api.modocode.moderndata.ir/api/v1"

    def __init__(self,base_url = base_url,token=None):
        self.base_url = base_url
        self.__token = token
    
    def login(self,username,password):
        data = {
            "username":username,
            "password":password
        }
        response = requests.post(f"{self.base_url}/auth/login",data=data)
        if response.status_code == 200:
            return True,response.json()
        else:
            if response.status_code == 400:
                return False , response.json()["message"] 
            else:
                return False , "Internal server error"
    
    def init_project(self,project_name,project_language,local_path):
        header = {
            "Authorization":f"Token {self.__token}"
        }
        response = requests.post(f"{self.base_url}/projects/all",data={"name":project_name,
                                                                   "language":project_language,
                                                                   "local_path":local_path},headers=header)
        if response.status_code in [200,201,204]:
            return True,response.json()
        else:
            if response.status_code == 400:
                print(response.json())
                return False , response.json()["message"] 
            else:
                return False , "Internal server error"
    def projects(self):
        header = {
            "Authorization":f"Token {self.__token}"
        }
        response = requests.get(f"{self.base_url}/projects/all?page_size=100",headers=header)
        if response.status_code in [200,201,204]:
            return True,response.json()
        else:
            if response.status_code == 400:
                print(response.json())
                return False , response.json()["message"] 
            else:
                return False , "Internal server error"
    def save_graph(self,relations,nodes,project_id):
        header = {
            "Authorization":f"Token {self.__token}"
        }
        data = {
            "relationships":json.dumps(relations),
            "nodes":json.dumps(nodes),
            "project":project_id
        }
        response = requests.post(f"{self.base_url}/projects/save-graph",headers=header,data=data,timeout=170)
        if response.status_code in [200,201,204]:
            return True,response.json()
        else:
            if response.status_code == 400:
                print(response.json())
                return False , response.json()["message"] 
            else:
                return False , "Internal server error"
    
    def ask_question(self,question,project_id):
        header = {
            "Authorization":f"Token {self.__token}"
        }
        data = {
            "question":question,
            "project":project_id
        }
        response = requests.post(f"{self.base_url}/projects/ask",headers=header,data=data,timeout=120)
        if response.status_code in [200,201,204]:
            return True,response.json()
        else:
            if response.status_code == 400:
                print(response.json())
                return False , response.json()["message"] 
            else:
                return False , "Internal server error"
        