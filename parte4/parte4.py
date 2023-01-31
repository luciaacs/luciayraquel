#! /usr/bin/python
from subprocess import call
import sys
import os
import subprocess

os.system("sudo apt-get update")
os.systme("sudo apt-get install kubectl")

os.system("sudo gcloud container clusters create cluster4 --num-nodes=5 --zone=us-central1-a")

os.system("sudo kubectl apply -f details.yaml")
os.system("sudo kubectl apply -f productpage.yaml")
os.system("sudo kubectl apply -f ratings.yaml")
os.system("sudo kubectl apply -f reviews-svc.yaml")

os.system("sudo kubectl apply -f review-v1-deployment.yaml")
os.system("sudo kubectl apply -f review-v2-deployment.yaml")
os.system("sudo kubectl apply -f review-v3-deployment.yaml")

os.system('sudo kubectl expose deployment productpage --type=LoadBalancer --port=9080')
