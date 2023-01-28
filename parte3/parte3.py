#! /usr/bin/python
from subprocess import call
import sys
import os
import subprocess

os.system('git clone https://github.com/CDPS-ETSIT/practica_creativa2.git')

#creamos contenedror de reviews
os.chdir('./practica_creativa2/bookinfo/src/reviews')
call(['sudo docker run --rm -u root -v "$(pwd)":/home/gradle/project -w /home/gradle/project gradle:4.8.1 gradle clean build'], shell=True)
#creamos el resto de contenedores
os.chdir(os.path.expanduser("~"))
os.system('sudo docker-compose build')
os.system('sudo docker-compose up')
