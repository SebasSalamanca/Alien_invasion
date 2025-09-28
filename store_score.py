import json 
import os
from pathlib import Path
import base64

class StoreScore:
    """Classs to store high score """
    def __init__(self):
        """Initialize paths and encrypted key"""
        self.home_dir = Path.home()
        self.key = 42
        self.os_name = os.name
        self.file_name = self.file_path()
    
    def file_path(self):

        # Cross-platform user documents directory
        if self.os_name == 'nt':  # Windows
            self.docs_path = Path(os.path.expandvars('%USERPROFILE%/Documents')) / 'alien_invasion'
        else:
            self.docs_path = Path.home() / 'alien_invasion'
        
        # Create folder if doesn't exist
        self.docs_path.mkdir(exist_ok=True)  

        return self.docs_path / 'highscore.json'
    


    def save_new_score(self, high_score):
        #Write the file highscore.json with a new higscore and encrypt it.
        data = {'score': high_score}

        score_str = json.dumps(data)

        data_bytes = score_str.encode('utf-8')
        encrypted_bytes = bytes((b + self.key) % 256 for b in data_bytes)
        encoded = base64.b64encode(encrypted_bytes).decode('ascii')

        with open(self.file_name, 'w') as f_obj:
            f_obj.write(encoded)

    
    def get_stored_score(self):
        #Get the highscore from highscore.json and decrypte it. If the file doesn't exist return 0
        try:
            with open(self.file_name) as f_obj:
                encoded = f_obj.read().strip()
            
            encrypted_bytes = base64.b64decode(encoded.encode('ascii'))
            decrypted_bytes = bytes((b - self.key) % 256 for b in encrypted_bytes)
            data = decrypted_bytes.decode('utf-8')
            data = json.loads(data)

            score = data.get('score', 0)
            return score


        except FileNotFoundError:
            return  0





