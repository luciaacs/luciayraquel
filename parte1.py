#!/usr/bin/python3

from subprocess import call
import sys
import os 


#Clonamos aplicacion
#En algunas maquinas virtuales hay que instalar los comandos
call(['sudo', 'apt-get', 'update'])
call(['sudo', 'apt-get', 'install', 'git'])
call(['sudo', 'apt-get', 'install', 'python3-pip'])
call(['git', 'clone', 'https://github.com/CDPS-ETSIT/practica_creativa2.git']) 

#Variable del entorno group number
os.environ['GROUP_NUMBER'] = '34'

#Modificamos el fichero requirements.txt para quitar las versiones
#de esta forma se guarda la máquina automaticamente
#call(['cp', '-f', './practica_creativa2/bookinfo/src/productpage/requirements.txt', 'in.txt'])
#fin = open('./practica_creativa2/bookinfo/src/productpage/requirements.txt', 'r')
#with fin as file:
#	nuevo=file.read()
#fin.close()
fin = open('./practica_creativa2/bookinfo/src/productpage/requirements.txt', 'w')
fin.write("urllib3\n chardet\n gevent\n greenlet")
fin.close()

#Instalamos requirements.txt
os.chdir('practica_creativa2/bookinfo/src/productpage') #cd
call(['pip3', 'install', '-r', 'requirements.txt'])


#Titulo de la aplicación es el nombre del grupo (productpage.html)
call(['mv', '-f', 'templates/productpage.html', 'templates/in.html'])
fin = open('templates/in.html', 'r')
fout = open('templates/productpage.html', 'w')
for line in fin:
	if "{% block title %}Simple Bookstore App{% endblock %}" in line :
		fout.write('{% block title %}GRUPO: {{ GROUP_NUMBER }}{% endblock %}')
	else:
		fout.write(line)
fin.close()
fout.close()
call(['rm', '-f', 'templates/in.html'])


#Ejecutamos la aplicación en el puerto correspondiente
call(['python3', 'productpage_monolith.py', '8080'])


