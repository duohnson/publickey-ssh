# SSH Automation Script (.BAT) for Windows

## Descripción

Pequeño script basico que permite conectar a un servidor utilizando autenticación por clave pública SSH. Este script es útil para automatizar tareas de conexión a servidores remotos sin necesidad de ingresar la contraseña cada vez.

De momento como solo cuento con un servidor, esta orientado a una sola conexión, pero se pueden agregar más servidores y opciones de conexión en el futuro.

## Requisitos

python3
pip install python-dotenv

## Uso

Configura tu archivo .env con las siguientes variables:

```
USER = tu_usuario
HOST = ip_del_servidor
```

Luego, ejecuta el script, para esto yo suelo utilizar un .BAT que genero, y este me abre un PowerShell:

```
@echo off
start powershell -Command "python main.py"
```

Nota: También funciona sin el publickey, te tira para escribir la contraseña, pero el objetivo es usar la autenticación por clave pública.

¿Porqué usar autenticación por clave pública SSH?

Mejor seguridad: Las claves públicas SSH son más seguras que las contraseñas, ya que no pueden ser adivinadas o descifradas fácilmente.
Comodidad: No necesitas ingresar tu contraseña cada vez que te conectas a un servidor, lo que ahorra tiempo y esfuerzo, solo es un CLICK, y listo, estas conectado.

Licencia MIT | Creado por Daniel Uohnson