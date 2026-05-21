from dotenv import load_dotenv
import os

import subprocess # Para ejecutar el comando como si se escribiera

load_dotenv()

def ssh_conexion():
    
    USER = os.getenv("USER")
    HOST = os.getenv("HOST")

    subprocess.run(["ssh", f"{USER}@{HOST}"])
