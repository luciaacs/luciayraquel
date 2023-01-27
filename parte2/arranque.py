#!/usr/bin/python3

from subprocess import call
import sys
import os 

#Instalación docker
os.system('sudo apt-get remove docker docker-engine docker.io containerd runc')
os.system('sudo apt-get update')
os.system('sudo apt install apt-transport-https ca-certificates curl software-properties-common')
os.system('curl -fsSL https://download.docker.com/linux/ubuntu/gpg | sudo apt-key add -')
os.system('sudo add-apt-repository "deb [arch=amd64] https://download.docker.com/linux/ubuntu focal stable"')
os.system('sudo apt update')
os.system('apt-cache policy docker-ce')
os.system('sudo apt install docker-ce')

#Dockerfile
call(['sudo', 'docker', 'build', '-t', '34/product-page', '.'])
os.system('sudo docker run -it --name 34-productpage -p 9080:9080 --env GROUP_NUMBER=34 34/product-page')
