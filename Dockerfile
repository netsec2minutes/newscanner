FROM ubuntu
RUN apt-get update 
RUN apt-get install python3 --yes
COPY scan.py /

