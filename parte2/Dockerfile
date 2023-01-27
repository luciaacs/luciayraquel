FROM python:3.9.2

ENV GROUP_NUMBER=34

RUN apt-get update
RUN apt-get install git
#RUN apt-get install python3-pip
RUN git clone 'https://github.com/CDPS-ETSIT/practica_creativa2.git'

#Dentro de parte2 instalamos requirements, modificamos productpage.html
COPY parte2.py .
RUN python3 parte2.py

EXPOSE 9080

WORKDIR practica_creativa2/bookinfo/src/productpage
CMD python3 productpage_monolith.py 9080




