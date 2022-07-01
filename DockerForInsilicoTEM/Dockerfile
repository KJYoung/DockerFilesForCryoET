# Dockerfile for my TomSim - dependencies : PyTom, EMAN2 ( without GUI, without IMOD ).
FROM ubuntu:20.04

ENV TZ=Asia/Seoul \
    DEBIAN_FRONTEND=noninteractive
RUN ln -snf /usr/share/zoneinfo/$TZ /etc/localtime && echo $TZ > /etc/timezone

COPY ./setupGUI.sh /home/
COPY ./matlab.zip /home/
COPY ./InSilicoTEMwithSRC.zip /
#################### For prerequisite of PyTom #################
# For general setup + python&pip 3.7 + install stuffs.
RUN apt-get update && apt-get install -y git vim wget software-properties-common xauth dbus-x11 unzip && \
    apt-get install -y libglu1-mesa libxi-dev libxmu-dev libglu1-mesa-dev libxcb-xinerama0 libxrender1 libxkbcommon-dev fontconfig mesa-utils xorg libxt6 && \
    cd /home/ && mkdir matlab && unzip -q matlab.zip -d matlab && \
    mkdir /InSilicoTEM && cd / && unzip -q InSilicoTEMwithSRC.zip -d InSilicoTEM

COPY ./startup.m /home/matlab
################# Working... #######################
RUN wget https://qiftp.tudelft.nl/diplib/2.9/dipimage_2.9_lin64.tbz --no-check-certificate && tar -xjf dipimage_2.9_lin64.tbz && \
    mkdir diplibDemo && wget https://qiftp.tudelft.nl/diplib/images.zip && unzip -q images.zip -d diplibDemo
ENV LD_LIBRARY_PATH=/usr/lib/x86_64-linux-gnu/:/dip/Linuxa64/lib/
ENTRYPOINT ["bash", "./home/setupGUI.sh"]