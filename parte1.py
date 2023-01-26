#!/usr/bin/python3

from subprocess import call
import os 


#Clonamos aplicacion
#En algunas maquinas virtuales hay que instalar los comandos
#call(['sudo', 'apt-get', 'update'])
#call(['sudo', 'apt-get', 'install', 'git'])
#call(['sudo', 'apt-get', 'install', 'python3-pip'])
call(['git', 'clone', 'https://github.com/CDPS-ETSIT/practica_creativa2.git']) 


#Instalamos PIP
call(['sudo', 'apt-get', 'install', '-y', 'python3-pip'])

#Variable del entorno group number
os.environ['GROUP_NUMBER'] = '34'

#Modificamos el fichero requirements.txt para quitar las versiones
#de esta forma se guarda la máquina automaticamente
#call(['mv', '-f', './practica_creativa2/bookinfo/src/productpage/requirements.txt', 'in.py'])
#fin = open('in.py', 'r')
#fout = open('./practica_creativa2/bookinfo/src/productpage/requirements.txt', 'w')
#for line in fin:
#	if 'urllib3==1.26.5' in line :
#		fout.write('urllib3')
#	elif 'chardet==3.0.4' in line :
#		fout.write('chardet')
#	elif 'gevent==1.4.0' in line :
#		fout.write('gevent')
#	elif 'greenlet==0.4.15' in line :
#		fout.write('greenlet')
#	else :
#		fout.write(line)
#fin.close()
#fout.close()
#call(['rm', '-f', 'in.py'])

#Instalamos requirements.txt
os.chdir('practica_creativa2/bookinfo/src/productpage') #cd
call(['pip3', 'install', '-r', 'requirements.txt'])

#Modificamos productpage_monolith.py
call(['mv', '-f', 'productpage_monolith.py', 'in.py'])
fin = open('in.py', 'r')
fout = open('productpage_monolith.py', 'w')
for line in fin:
	# Creamos variable igual que flood_factor
	if 'flood_factor = 0 if (os.environ.get("FLOOD_FACTOR") is None) else int(os.environ.get("FLOOD_FACTOR"))' in line :
		fout.write(line)
		fout.write('numeroGrupo = 0 if (os.environ.get("GROUP_NUMBER") is None) else int(os.environ.get("GROUP_NUMBER"))'+ os.linesep)
	elif "product = getProduct(product_id)" in line :
		fout.write(line)
		fout.write('    grupo = numeroGrupo') #definimos var
		fout.write(os.linesep)
	elif "\'productpage.html\'," in line :
		fout.write(line)
		fout.write('	grupo=grupo,')
		fout.write(os.linesep)
	else :
		fout.write(line)
fin.close()
fout.close()
call(['rm', '-f', 'in.py'])


#Titulo de la aplicación es el nombre del grupo (productpage.html)
call(['mv', '-f', 'templates/productpage.html', 'templates/in.html'])
fin = open('templates/in.html', 'r')
fout = open('templates/productpage.html', 'w')
for line in fin:
	if "{% block title %}Simple Bookstore App{% endblock %}" in line :
		fout.write('{% block title %}GRUPO: {{ group }}{% endblock %}')
	else:
		fout.write(line)
fin.close()
fout.close()
call(['rm', '-f', 'templates/in.html'])

#Ejecutamos la aplicación en el puerto correspondiente
call(['python3', 'productpage_monolith.py', '9080'])

#sudo rm/rmdir -rf 

