#! /usr/bin/python
from subprocess import call
import sys
import os
import subprocess
#Variable del entorno group number
#os.environ['GROUP_NUMBER'] = '34'
#Modificamos requirement.txt
fin = open('./practica_creativa2/bookinfo/src/productpage/requirements.txt', 'r')
with fin as file:
	nueva=file.read()
fin.close()
fin = open('./practica_creativa2/bookinfo/src/productpage/requirements.txt', 'w')
with fin as file:
	nueva=nueva.replace('urllib3==1.26.5', 'urllib3')
	nueva=nueva.replace('chardet==3.0.4', 'chardet')
	nueva=nueva.replace('gevent==1.4.0', 'gevent')
	nueva=nueva.replace('greenlet==0.4.15', 'greenlet')
	fin.write(nueva)
fin.close()
#Instalamos requirements.txt
os.chdir('practica_creativa2/bookinfo/src/productpage') #cd
call(['pip3', 'install', '-r', 'requirements.txt'])
