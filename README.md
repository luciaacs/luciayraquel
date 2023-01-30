# Practica Creativa 2 CDPS
Para empezar sera necesario sopiar el link de acceso a este repositorio de codigo:
```
git clone "https://github.com/luciaacs/luciayraquel.git"
cd luciayraquel
```
Dentro encontraremos diferentes carpetas que pertenecen a cada una de las partes del proyecto

-------------------------------------------------------------------------------------------------------------------------------------------------------------------------
PARTE 1: Despliegue de la aplicación en máquina virtual pesada
------------------------------------------------------------------------------------------------------------------------------------------------------------------------- 
```
cd parte1
```

Lo unico que tendremos que hacer es ejecutar el archivo python en nuestro ordenador donde:
- instalaremos las dependencias necesarias del archivo requirements.txt
- modificaremos la pagina productpage.html para poner de titulo el numero de nuestro grupo: 34
- asignaremos el puerto 9080 como puerto externo para acceder a la pagina desde el exterior

```
python3 parte1.py
```
![Captura de pantalla (172)](https://user-images.githubusercontent.com/106026951/215514953-ec51ee02-ef5e-4e46-9106-d9480f4fbdc0.png)

-------------------------------------------------------------------------------------------------------------------------------------------------------------------------
PARTE 2: Despliegue de una aplicación monolítica usando docker
------------------------------------------------------------------------------------------------------------------------------------------------------------------------- 

```
cd parte2
sudo docker build -t 34-product-page .
sudo docker run -p 9080:9080 34-product-page
```
Dentro de esta carpeta encontramos el fichero Dockerfile donde hemos definido:
- La aplicación web se ejecutara en el puerto 9080
- el script de python donde instalamos las dependecias necesarias
- la imagen de docker: 34/productpage
- el nombre del contenedor: 34-productpage

-------------------------------------------------------------------------------------------------------------------------------------------------------------------------
PARTE 3: Segmentación de una aplicación monolítica en microservicios utilizando dockercompose
------------------------------------------------------------------------------------------------------------------------------------------------------------------------- 
```
cd parte3
python3 parte3.py
```
En esta carpeta tenemos definidos cada uno de los Dockerfile necesarios para ejecutar cada uno de los servicios,incluyendo el docker-compose.yml
El contenedor del servicio de reviews se crea llamando al script de python

```
python3 parte3.py
```
Y el resto de contenedores los creamos y ejecutamos a mano

```
sudo docker-compose build
sudo docker-compose up
```
![Captura de pantalla (171)](https://user-images.githubusercontent.com/106026951/215477181-f1c24ddf-dd3a-4872-9a7d-e9ddd4ef7243.png)


-------------------------------------------------------------------------------------------------------------------------------------------------------------------------
PARTE 4: Despliegue de una aplicación basada en microservicios utilizando Kubernetes
------------------------------------------------------------------------------------------------------------------------------------------------------------------------- 
```
cd parte4
python3 parte4.py
```






