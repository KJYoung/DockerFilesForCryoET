FROM ubuntu:latest
#FROM nvidia/cuda:11.0-base

ENV TZ Asia/Seoul
RUN ln -snf /usr/share/zoneinfo/$TZ /etc/localtime && echo $TZ > /etc/timezone

RUN apt-get update && apt-get install -y gnupg ca-certificates && \
    apt-key adv --keyserver hkp://keyserver.ubuntu.com:80 --recv-keys 3FA7E0328081BFF6A14DA29AA6A19B38D3D831EF && \
    echo "deb https://download.mono-project.com/repo/ubuntu stable-focal main" | tee /etc/apt/sources.list.d/mono-official-stable.list && \
    apt-get update && \
    apt-get install -y mono-complete
# above is for the installation of mono-complete for ubuntu 20.04

RUN apt-get install -y git vim wget
RUN apt-get install -y cmake g++ nvidia-cuda-toolkit

ENV DEBIAN_FRONTEND noninteractive

RUN apt-get install -y software-properties-common && \
    wget https://developer.download.nvidia.com/compute/cuda/repos/ubuntu1804/x86_64/cuda-ubuntu1804.pin && \
    mv cuda-ubuntu1804.pin /etc/apt/preferences.d/cuda-repository-pin-600 && \
    apt-key adv --fetch-keys https://developer.download.nvidia.com/compute/cuda/repos/ubuntu1804/x86_64/7fa2af80.pub && \
    add-apt-repository "deb https://developer.download.nvidia.com/compute/cuda/repos/ubuntu1804/x86_64/ /" && \
    apt-get update && apt-get -y install cuda

ENV PATH $PATH:/usr/local/cuda-11.6/bin
ENV CUDA_PATH /usr/local/cuda-11.6/bin

RUN mkdir warpRoot && cd /warpRoot/ && \
    git clone https://github.com/cramerlab/warpcraft.git

COPY ./setupGUI.sh ./home/

# Install Wine
RUN apt-get install -y wine && dpkg --add-architecture i386 && apt-get update && apt-get install -y wine32

RUN wget "https://dl.winehq.org/wine/wine-mono/7.0.0/wine-mono-7.0.0-x86.msi" -O "/warpRoot/wine-mono.msi" && \
    wine msiexec /i /warpRoot/wine-mono.msi && \
    echo 'alias warpcli="wine /warpRoot/warpcraft/bin/warpcraft.exe"' >> ~/.bashrc

# Install Dynamo2m [dynamo2warp, warp2dynamo, relion_star_downgrade]
RUN apt-get install -y python3-pip && pip install dynamo2m

ENTRYPOINT ["bash", "./home/setupGUI.sh"]
