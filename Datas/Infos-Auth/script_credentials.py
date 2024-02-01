import credentials as creds
import os

print(f'username: {creds.username}\npassword: {creds.password}')

print(os.getcwd())
print(os.getenv("SHELL"))
print(os.getuid())