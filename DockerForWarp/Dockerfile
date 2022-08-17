FROM nvidia/cuda:11.6.0-devel-ubuntu20.04

ENV TZ=Asia/Seoul \
    DEBIAN_FRONTEND=noninteractive
RUN ln -snf /usr/share/zoneinfo/$TZ /etc/localtime && echo $TZ > /etc/timezone

RUN apt-get update && apt-get install -y cmake g++ nvidia-cuda-toolkit

# install tensorflow
RUN apt-get install -y wget && \
    wget https://storage.googleapis.com/tensorflow/libtensorflow/libtensorflow-gpu-linux-x86_64-2.6.0.tar.gz && \
    tar -C /usr/local -xzf libtensorflow-gpu-linux-x86_64-2.6.0.tar.gz && \
    rm libtensorflow-gpu-linux-x86_64-2.6.0.tar.gz && ldconfig

# install mono-complete
RUN apt-get install -y gnupg ca-certificates && \
    apt-key adv --keyserver hkp://keyserver.ubuntu.com:80 --recv-keys 3FA7E0328081BFF6A14DA29AA6A19B38D3D831EF && \
    echo "deb https://download.mono-project.com/repo/ubuntu stable-focal main" | tee /etc/apt/sources.list.d/mono-official-stable.list && \
    apt-get update && \
    apt-get install -y mono-complete

RUN apt-get install -y libfftw3-dev