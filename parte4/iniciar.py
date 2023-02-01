from subprocess import call
import sys
import os
import subprocess

os.system("kubectl delete --all deployments")
os.system("kubectl delete --all services")
os.system("kubectl delete --all pods")

os.system("kubectl apply -f details.yaml")
os.system("kubectl apply -f productpage.yaml")
os.system("kubectl apply -f ratings.yaml")
os.system("kubectl apply -f reviews-svc.yaml")

os.system("kubectl apply -f reviews-v1-deployment.yaml")
#os.system("kubectl apply -f reviews-v2-deployment.yaml")
#os.system("kubectl apply -f reviews-v3-deployment.yaml")
