#! /usr/bin/python
from subprocess import call
import sys
import os
import subprocess

#os.system("apt-get update")
#os.system("apt-get install kubectl")

os.system("gcloud container clusters create cluster --num-nodes=5 --zone=europe-southwest1-b")




