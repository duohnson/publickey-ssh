from dotenv import load_dotenv
import os

import subprocess # To execute the command as if it were written

load_dotenv()

def ssh_connect():
    
    USER = os.getenv("USER")
    HOST = os.getenv("HOST")

    subprocess.run(["ssh", f"{USER}@{HOST}"])
