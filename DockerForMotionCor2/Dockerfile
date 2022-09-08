#FROM ubuntu:latest
FROM nvidia/cuda:11.6.0-devel-ubuntu20.04

ENV TZ=Asia/Seoul
RUN ln -snf /usr/share/zoneinfo/$TZ /etc/localtime && echo $TZ > /etc/timezone

RUN apt-get update && apt-get install -y \
    nvidia-cuda-toolkit 

COPY ./MotionCor2 ./
RUN echo 'alias motioncor2="/MotionCor2"' >> ~/.bashrc
