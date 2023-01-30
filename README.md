# Practica Creativa 2 CDPS
Para empezar sera necesario copiar el link de acceso a este repositorio de código:
```
git clone "https://github.com/luciaacs/luciayraquel.git"
cd luciayraquel
```
Dentro encontraremos diferentes carpetas que pertenecen a cada una de las partes del proyecto.

-------------------------------------------------------------------------------------------------------------------------------------------------------------------------
PARTE 1: Despliegue de la aplicación en máquina virtual pesada
------------------------------------------------------------------------------------------------------------------------------------------------------------------------- 
En la primera parte desplegamos una aplicación monolítica alojada en una máquina vitual. Para ello ejecutamos un script de python, este incluye: 
- Instalaremos las dependencias necesarias del archivo requirements.txt.
- Modificaremos la pagina productpage.html para poner de titulo el numero de nuestro grupo; 34.
- Ejecutar la aplicación asignando el puerto 9080.

```
cd parte1
python3 parte1.py

```
Accedemos a la aplicación con http://Ip_maquina_vitual:9080/productpage.
![Captura de pantalla (172)](https://user-images.githubusercontent.com/106026951/215514953-ec51ee02-ef5e-4e46-9106-d9480f4fbdc0.png)

-------------------------------------------------------------------------------------------------------------------------------------------------------------------------
PARTE 2: Despliegue de una aplicación monolítica usando docker
------------------------------------------------------------------------------------------------------------------------------------------------------------------------- 
En la segunda parte desplegamos una aplicación monolítica con el uso de contenedores Docker. Para realizar la ejecución necesitamos:
- Un fichero Dockerfile donde definimos el puerto 9080 para la ejecución de la aplicación web, ejecución del script de python parte2.py y ejecución de la aplicación.
- Un script de python, parte2.py, donde instalamos las dependecias necesarias.

```
cd parte2
sudo docker build -t 34-product-page .
sudo docker run -p 9080:9080 34-product-page
```

![Captura de pantalla (185)](https://user-images.githubusercontent.com/106026951/215516853-8649932f-8e4a-4040-ba34-4dac7e68b315.png)

-------------------------------------------------------------------------------------------------------------------------------------------------------------------------
PARTE 3: Segmentación de una aplicación monolítica en microservicios utilizando dockercompose
------------------------------------------------------------------------------------------------------------------------------------------------------------------------- 
La tercera parte descompone la aplicación en cuatro microservicios con el uso de dockercompose. Para poder ser ejecutada hacen falta los siguientes ficheros:
- Un Docker file por cada servicio, excepto reviews, cuyo contenedor se crea llamando al script de python parte3.py.
- El docker-compose.yaml donde declaramos los cuatro microservicios.
- Script parte3.py.
- Script requirements.py, se ejecuta por el Docker-productpages para modificar el fichero requirements.txt.

```
cd parte3
python3 parte3.py
```
Creamos los contenedores restantes y ejecutamos a mano.
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






