FROM ubuntu:kinetic-20220830
RUN apt-get update 
RUN apt-get install python3 --yes
COPY scan.py /

