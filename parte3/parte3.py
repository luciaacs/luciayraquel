#! /usr/bin/python
from subprocess import call
import sys
import os
import subprocess

os.system('git clone https://github.com/CDPS-ETSIT/practica_creativa2.git')

#creamos contenedror de reviews
os.chdir('./practica_creativa2/bookinfo/src/reviews')
#Necesidades
call(['sudo docker run --rm -u root -v "$(pwd)":/home/gradle/project -w /home/gradle/project gradle:4.8.1 gradle clean build'], shell=True)

