FROM ubuntu:latest

RUN apt-get update && apt-get install -y wget
RUN mkdir ctffind4 && wget "https://grigoriefflab.umassmed.edu/system/tdf?path=ctffind-4.1.14-linux64.tar.gz&file=1&type=node&id=26" -O /ctffind4/ctffind-4.1.14-linux64.tar.gz && \
    tar xvfz /ctffind4/ctffind-4.1.14-linux64.tar.gz
ENV PATH $PATH:/ctffind4/bin 
