#!/usr/bin/python3

import os, sys, subprocess
from subprocess import call

#Funcion arch para reemplazar dentro de un archivo
def arch(fi, rep1, rep2):
	fin = open('./practica_creativa2/bookinfo/src/productpage/' + fi, 'r')

	with fin as file:
		x= file.read()
	fin.close()

	fin = open('./practica_creativa2/bookinfo/src/productpage/' + fi, 'w')
	with fin as file:
		x= x.replace(rep1, rep2)
		fin.write(x)
	fin.close()

#Modificamos el fichero requirements.txt
arch('requirements.txt', 'urllib3==1.26.5', 'urllib3')
arch('requirements.txt', 'chardet==3.0.4', 'chardet')
arch('requirements.txt', 'gevent==1.4.0', 'gevent')
arch('requirements.txt', 'greenlet==0.4.15', 'greenlet')
#Instalamos pip sudo apt-get install python-pip
subprocess.run(["apt-get", "install", "python3-pip"])
#Instalamos dependencias de requirements.txt con pip
subprocess.run(["pip3", "install", '-r', './practica_creativa2/bookinfo/src/productpage/requirements.txt'])

#Capturamos la variable GROUP_NUMBER definida en el Dockerfile
title = os.environ.get('GROUP_NUMBER')
arch('templates/productpage.html', 'Simple Bookstore App', title)
