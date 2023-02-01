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
En la segunda parte desplegamos una aplicación monolítica con el uso de contenedores Docker. 

<img width="418" alt="Captura de Pantalla 2023-01-31 a las 0 11 55" src="https://user-images.githubusercontent.com/106026951/215617581-35a4a60d-4a04-4e84-9126-fbd71fec0550.png">

Antes de la ejecución debemos asegurarnos de tener instalado docker, si no lo tenemos, ejecutamos:
```
apt-get update
apt-get install docker.io
```
Para esta parte necesitamos:
- Un fichero Dockerfile donde definimos el puerto 9080 para la ejecución de la aplicación web, ejecución del script de python parte2.py y ejecución de la aplicación.
- Ejecutar un script de python, parte2.py, donde instalamos las dependecias necesarias.
  ```
  cd parte2
  sudo docker build -t 34-product-page .
  sudo docker run -p 9080:9080 34-product-page
  ```
Accedemos a la aplicación con http://Ip_maquina_vitual:9080/productpage.

![Captura de pantalla (185)](https://user-images.githubusercontent.com/106026951/215516853-8649932f-8e4a-4040-ba34-4dac7e68b315.png)

-------------------------------------------------------------------------------------------------------------------------------------------------------------------------
PARTE 3: Segmentación de una aplicación monolítica en microservicios utilizando dockercompose
------------------------------------------------------------------------------------------------------------------------------------------------------------------------- 
La tercera parte descompone la aplicación en cuatro microservicios con el uso de dockercompose. 

<img width="667" alt="Captura de Pantalla 2023-01-31 a las 0 12 19" src="https://user-images.githubusercontent.com/106026951/215617654-cdcfe645-c3a1-4fc1-8445-de3d156ce52d.png">

Laa ejecución de la parte 3 requiere:
- Un Docker file por cada servicio, excepto reviews, cuyo contenedor se crea directamente llamando al script de python parte3.py.
- El docker-compose.yaml donde declaramos los cuatro microservicios.
- Un script requirements.py que se ejecuta por el Docker-productpages para modificar el fichero requirements.txt.
- Ejecutar el script parte3.py donde creamos los contenedores necesarios.
  ```
  cd parte3
  python3 parte3.py
  ```

Accedemos a la aplicación con http://Ip_maquina_vitual:9080/productpage.

![Captura de pantalla (171)](https://user-images.githubusercontent.com/106026951/215477181-f1c24ddf-dd3a-4872-9a7d-e9ddd4ef7243.png)


-------------------------------------------------------------------------------------------------------------------------------------------------------------------------
PARTE 4: Despliegue de una aplicación basada en microservicios utilizando Kubernetes
------------------------------------------------------------------------------------------------------------------------------------------------------------------------- 
En la última parte desplegamos la aplicación utilizando kubernetes. Para ello:
- Subimos las imágenes creadas en el apartado anterior correspondientes a cada servicio a un repositorio de Docker hub.
  ```
  docker login
  sudo docker tag nombreImagen luciaacs/34-servicio:version
  sudo docker push luciaacs/34-servicio:version
  ```
- Creamos ficheros (.yaml) individuales para cada microservicio, en el caso de reviews, al tener tres versiones, creamos tres deployments.yamls distintos.
- Creamos un cluster de kubernetes en GKE con 5 nodos sin autoescalado.
- Ejecutamos inciar.py creando los servicios y deployments a partir de los ficheros .yaml.
  ```
  cd parte4
  python3 iniciar.py
  ```
- Comprobamos con los siguientes comandos:
  ```
  kubectl get services
  kubectl get deployments
  ```
  
Accedemos a la aplicación con http://servicio-productpage_EXTERNAL_IP:9080/productpage.
<img width="1176" alt="Captura de Pantalla 2023-02-01 a las 2 41 44" src="https://user-images.githubusercontent.com/106026951/215924264-49850ca6-9405-4665-a83c-69c596365fc1.png">

-------------------------------------------------------------------------------------------------------------------------------------------------------------------------
PREGUNTAS Y COMPARACIÓN
------------------------------------------------------------------------------------------------------------------------------------------------------------------------- 
**PREGUNTAS**

**Incluya en la memoria de la práctica las diferencias con la versión de un único contenedor.**

Docker es una tecnología de contenedores que permite empaquetar y ejecutar aplicaciones en entornos aislados, aportando fiabilidad al no verse afectados por otros procesos. Se ejecuta con el comando "docker run" especificando las configuraciones en la línea de comandos. Por otro lado, Docker Compose se enfoca en la gestión y despliegue de aplicaciones compuestas por múltiples contenedores, son muy faciles de escalar mediante la creación de múltiples réplicas de contenedores balanceando la carga de trabajo. Además, está segunda opción proporciona una forma más fácil y clara de descibir la configuración y las relaciones entre contenedores con el archivo docker-compose.yml.

**Incluya en la memoria de la práctica las diferencias que encuentra al crear los pods, así mismo la diferencia que ve para escalar esta última solución.**

Docker Compose es adecuado para pequeños proyectos de desarrollo y pruebas, pero puede tener limitaciones en entornos de producción a gran escala.
Kubernetes, por otro lado, está diseñado para proporcionar alta disponibilidad y tolerancia a fallos en entornos de producción a gran escala.

Respecto a la escalabilidad, esta opción permite automatizar la escalabilidad de los recursos de los ccontenedores, a diferencia de Docker-compose, en el cual la escalabilidad se realiza de forma manual para cada contenedor individualmente.

**COMPARACIÓN**
- Maquina Virtual: La solución más simple. Al ser una aplicación monolítica no tiene buena fiabilidad y es más compleja de escalar, solo es posible escalabilidad horizontal. Además, escalar horizontalmente no solucionara la poca fiabilidad al tener un único punto de fallo.
- Docker: Se trata de una solución también simple, pero más fiable que la anterior debido al uso de una imagen base fija. Sin embargo, la escalabilidad seguiría siendo horizontal, lo cual supone problemas parecidos.
- Docker-compose: Es una solución más compleja. Mucho más fiable debido al uso de microservicios, permitiendo así fallos sin que se caiga la aplicación al completo. Además, se podrían escalar individualmente los servicios que se requieran en función de la demanda.
- Kubernetes: También es una solución compleja. El uso de pods incrementa la escalabilidad. Además, la división en microservicios y utilizar redundancia de pods,permitiendo distribuir la carga, aporta fiabilidad. 




