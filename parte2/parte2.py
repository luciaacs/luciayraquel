#! /usr/bin/python
from subprocess import call
import sys
import os

#Variable del entorno group number
#os.environ['GROUP_NUMBER'] = '34'

#Modificamos requirement.txt
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
		fout.write("{% block title %}GRUPO: "+ os.environ.get['GROUP_NUMBER'] + "{% endblock %}")
	else:
		fout.write(line)
fin.close()
fout.close()
call(['rm', '-f', 'templates/in.html'])

#Contenedor
#call(['sudo', 'docker', 'build', '-t', '34/product-page', '.'])
#os.system('sudo docker run -it --name 34-productpage -p 9080:9080 --env GROUP_NUMBER=34 34/product-page')
