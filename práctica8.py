import ftplib
from ftplib import FTP, FTP_PORT

print("Por favor introduce los datos necesarios para acceder al servidor FTP.\n")
server = input('host: ')
user = input('user: ')
password = input('password: ')

host = FTP(server, user, password)
information = host.nlst()
name = input("Por favor introduce el nombre con el que vas a guardar el archivo. \n\n")
with open(name +".txt",'w+' ) as txt :
        for file in information:
                txt.writelines(f'{file}\n')
print("Se ha creado de manera exitosa el archivo " + name +".txt")