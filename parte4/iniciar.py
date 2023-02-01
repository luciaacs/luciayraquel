from subprocess import call
import sys
import os
import subprocess

os.system("sudo kubectl apply -f details.yaml")
os.system("sudo kubectl apply -f productpage.yaml")
os.system("sudo kubectl apply -f ratings.yaml")
os.system("sudo kubectl apply -f reviews-svc.yaml")

os.system("sudo kubectl apply -f review-v1-deployment.yaml")
#os.system("sudo kubectl apply -f review-v2-deployment.yaml")
#os.system("sudo kubectl apply -f review-v3-deployment.yaml")
