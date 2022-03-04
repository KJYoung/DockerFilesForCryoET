# This Dockerfile is for RELION 4.0
FROM nvidia/cuda:11.4.0-devel-ubuntu20.04

ENV TZ=Asia/Seoul \
    DEBIAN_FRONTEND=noninteractive
RUN ln -snf /usr/share/zoneinfo/$TZ /etc/localtime && echo $TZ > /etc/timezone

RUN apt-get update && apt-get install -y wget vim git software-properties-common nvidia-cuda-toolkit \
    ghostscript cmake build-essential mpi-default-bin mpi-default-dev libfftw3-dev libtiff-dev libpng-dev ghostscript libxft-dev \
    libglu1-mesa libxi-dev libxmu-dev libglu1-mesa-dev libxcb-xinerama0 libxrender1 libxkbcommon-dev xauth fontconfig mesa-utils xorg

RUN git clone https://github.com/3dem/relion.git && cd relion && git checkout ver4.0 && git pull && \
    mkdir build && cd build && cmake .. && make -j 8 && make install

# For CTFFIND 4.1
RUN mkdir ctffind4 && wget "https://grigoriefflab.umassmed.edu/system/tdf?path=ctffind-4.1.14-linux64.tar.gz&file=1&type=node&id=26" -O /ctffind4/ctffind-4.1.14-linux64.tar.gz && \
    tar xvfz /ctffind4/ctffind-4.1.14-linux64.tar.gz
ENV PATH $PATH:/ctffind4/bin 

COPY ./setupGUI.sh /home/
ENTRYPOINT ["bash", "./home/setupGUI.sh"]
    