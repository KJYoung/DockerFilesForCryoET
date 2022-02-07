#FROM ubuntu:latest
FROM nvidia/cuda:11.0-base

ENV DEBIAN_FRONTEND noninteractive
ENV TZ Asia/Seoul
RUN ln -snf /usr/share/zoneinfo/$TZ /etc/localtime && echo $TZ > /etc/timezone

RUN apt-get update && apt-get install -y \
    wget vim python3 \
    libglu1-mesa libxi-dev libxmu-dev libglu1-mesa-dev \
    libxcb-xinerama0 libxrender1 libxkbcommon-dev \
    xauth \
    fontconfig \
    mesa-utils xorg \ 
    git g++ cmake nvidia-cuda-toolkit \
    build-essential \
    mpi-default-bin \
    mpi-default-dev \
    libfftw3-dev \
    libtiff-dev \
    pip libxt6 octave

#mesa-utils for glxgears
RUN wget https://download.java.net/openjdk/jdk11/ri/openjdk-11+28_linux-x64_bin.tar.gz && \
    tar -xvf openjdk-11+28_linux-x64_bin.tar.gz && \
    rm openjdk-11+28_linux-x64_bin.tar.gz

RUN apt-get update && apt-get install -y gnupg ca-certificates && \
    apt-key adv --keyserver hkp://keyserver.ubuntu.com:80 --recv-keys 3FA7E0328081BFF6A14DA29AA6A19B38D3D831EF && \
    echo "deb https://download.mono-project.com/repo/ubuntu stable-focal main" | tee /etc/apt/sources.list.d/mono-official-stable.list && \
    apt-get update && \
    apt-get install -y mono-complete
# above is for the installation of mono-complete for ubuntu 20.04

RUN apt-get install -y software-properties-common && \
    wget https://developer.download.nvidia.com/compute/cuda/repos/ubuntu1804/x86_64/cuda-ubuntu1804.pin && \
    mv cuda-ubuntu1804.pin /etc/apt/preferences.d/cuda-repository-pin-600 && \
    apt-key adv --fetch-keys https://developer.download.nvidia.com/compute/cuda/repos/ubuntu1804/x86_64/7fa2af80.pub && \
    add-apt-repository "deb https://developer.download.nvidia.com/compute/cuda/repos/ubuntu1804/x86_64/ /" && \
    apt-get update && apt-get -y install cuda

# Install Wine
RUN apt-get install -y wine && dpkg --add-architecture i386 && apt-get update && apt-get install -y wine32

RUN wget "https://dl.winehq.org/wine/wine-mono/7.0.0/wine-mono-7.0.0-x86.msi" -O "/warpRoot/wine-mono.msi" && \
    wine msiexec /i /warpRoot/wine-mono.msi && \
    echo 'alias warpcli="wine /warpRoot/warpcraft/bin/warpcraft.exe"' >> ~/.bashrc

RUN ln -s /usr/bin/python3 /usr/bin/python

ENV PATH $PATH:/usr/local/cuda-11.6/bin:/jdk-11/bin
ENV CUDA_PATH /usr/local/cuda-11.6/bin
ENV IMOD_DIR /usr/local/IMOD
ENV LIBGL_ALWAYS_INDIRECT 1
ENV QT_XKB_CONFIG_ROOT /usr/share/X11/xkb
ENV XDG_RUNTIME_DIR /tmp/runtime-root
ENV FONTCONFIG_PATH /etc/fonts

#IMOD
RUN wget https://bio3d.colorado.edu/imod/AMD64-RHEL5/imod_4.11.12_RHEL7-64_CUDA10.1.sh && \
    sh imod_4.11.12_RHEL7-64_CUDA10.1.sh -y && \
    rm imod_4.11.12_RHEL7-64_CUDA10.1.sh && \
    mkdir /tmp/runtime-root && \
    chmod 0700 /tmp/runtime-root

#Warpcli
RUN mkdir warpRoot && cd /warpRoot/ && \
    git clone https://github.com/cramerlab/warpcraft.git

# Install Dynamo2m [dynamo2warp, warp2dynamo, relion_star_downgrade]
RUN apt-get install -y python3-pip && pip install dynamo2m

#Relion 
RUN git clone https://github.com/3dem/relion.git && \
    cd relion && \
    git checkout master && \
    mkdir build && \
    cd build && \
    cmake .. -DGUI=OFF && \
    make && \
    make install

#Dynamo
RUN pip install gdown
RUN gdown https://drive.google.com/uc?id=1Pffjfwu-EXmEzYC5DGSp8YqAPCtg7ye0
#link format is slightly different with provided form.

RUN mkdir /home/dynamoRoot/ && \
    mv dynamo-v-1.1.532_MCR-9.9.0_GLNXA64_withMCR.tar /home/dynamoRoot/dynamo.tar && \
    tar -xf /home/dynamoRoot/dynamo.tar -C /home/dynamoRoot && \
    rm /home/dynamoRoot/dynamo.tar

RUN mv /home/dynamoRoot/MCRLinux/sys/os/glnxa64/libstdc++.so.6 /home/dynamoRoot/MCRLinux/sys/os/glnxa64/libstdc++.so.6.orig

# For autoalign_dynamo : modified for non-interactive docker install.
RUN git clone https://github.com/KJYoung/autoalign_dynamo.git && \
    cd /autoalign_dynamo && \
    ./install.sh

RUN echo 'alias imodynamo="source $IMOD_DIR/IMOD-linux.sh && source /home/dynamoRoot/dynamo_activate_linux_shipped_MCR.sh"' >> ~/.bashrc
RUN echo 'alias imodcfg="source $IMOD_DIR/IMOD-linux.sh"' >> ~/.bashrc
RUN echo 'alias dynamocfg="source /home/dynamoRoot/dynamo_activate_linux_shipped_MCR.sh"' >> ~/.bashrc
RUN echo 'alias autoalign="octave --persist /opt/autoalign_dynamo/autoalign_activate.m"' >> ~/.bashrc

# For automated GUI connection.
COPY ./setupGUI.sh ./home/
ENTRYPOINT ["bash", "./home/setupGUI.sh"]
############################################################################################