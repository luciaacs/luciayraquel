FROM python:3.9.2

ENV GROUP_NUMBER=$GROUP_NUMBER

RUN git clone 'https://github.com/CDPS-ETSIT/practica_creativa2.git'

WORKDIR practica_creativa2/bookinfo/src/productpage
RUN pip3 install requirements.txt

EXPOSE 9080

CMD ["python3", "parte2.py"]




