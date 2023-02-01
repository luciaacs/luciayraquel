#! /usr/bin/python
from subprocess import call
import sys
import os
import subprocess

#os.system("sudo apt-get update")
#os.system("sudo apt-get install kubectl")

os.system("sudo gcloud container clusters create cluster --num-nodes=5 --zone=europe-southwest1-b")




