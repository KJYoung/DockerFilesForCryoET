FROM ubuntu:latest

ENV TZ=Asia/Seoul
RUN ln -snf /usr/share/zoneinfo/$TZ /etc/localtime && echo $TZ > /etc/timezone

RUN apt-get update && apt-get install -y \
    cmake \
    git \
    build-essential \
    mpi-default-bin \
    mpi-default-dev \
    libfftw3-dev \
    libtiff-dev

RUN git clone https://github.com/3dem/relion.git && \
    cd relion && \
    git checkout master && \
    mkdir build && \
    cd build && \
    cmake .. -DGUI=OFF && \
    make && \
    #mkdir /home/relionRoot && \
    #cmake -DCMAKE_INSTALL_PREFIX=/home/relionRoot/ && \
    make install
