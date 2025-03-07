import os
import json
class LocalHandler:
    def __init__(self,config_path = os.path.join(os.path.expanduser('~'), 'Documents', 'modo_config.json')):
        self.config_path = config_path
        self.config = {}
        if not os.path.exists(self.config_path):
            with open(self.config_path, 'w') as f:
                f.write(json.dumps({"login":False}))
    
    def get_modo_config(self):
        if os.path.exists(self.config_path):
            with open(self.config_path, 'r') as f:
                self.config = json.loads(f.read())
        return self.config
    def save_modo_config(self,config):
        if os.path.exists(self.config_path):
            with open(self.config_path, 'w+') as f:
                f.write(json.dumps(config))
        return self.config_path