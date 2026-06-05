# SSH Automation Script (.BAT) for Windows

## Description

Small basic script that allows connecting to a server using SSH public key authentication. This script is useful for automating connection tasks to remote servers without needing to enter the password every time.

Currently, since I only have one server, it is oriented to a single connection, but more servers and connection options can be added in the future.

## Requirements

python3
pip install python-dotenv

## Usage

Configure your .env file with the following variables:

```
USER = your_user
HOST = server_ip
```

Then, execute the script. For this, I usually use a .BAT that I generate, and it opens a PowerShell for me:

```
@echo off
start powershell -Command "python main.py"
```

Note: It also works without the public key, it prompts you to enter the password, but the goal is to use public key authentication.

Why use SSH public key authentication?

Better security: SSH public keys are more secure than passwords, as they cannot be easily guessed or decrypted.
Convenience: You don't need to enter your password every time you connect to a server, which saves time and effort, it's just a CLICK, and you're connected.

MIT License | Created by Daniel Uohnson