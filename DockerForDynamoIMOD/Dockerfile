FROM ubuntu:latest

ENV DEBIAN_FRONTEND noninteractive
ENV TZ Asia/Seoul
RUN ln -snf /usr/share/zoneinfo/$TZ /etc/localtime && echo $TZ > /etc/timezone

RUN apt-get update && apt-get install -y \
    wget vim python3 \
    libglu1-mesa libxi-dev libxmu-dev libglu1-mesa-dev \
    libxcb-xinerama0 libxrender1 libxkbcommon-dev \
    xauth \
    fontconfig \
    mesa-utils xorg git \
    pip libxt6 \
    nvidia-cuda-toolkit

RUN wget https://download.java.net/openjdk/jdk11/ri/openjdk-11+28_linux-x64_bin.tar.gz && \
    tar -xvf openjdk-11+28_linux-x64_bin.tar.gz && \
    rm openjdk-11+28_linux-x64_bin.tar.gz

RUN ln -s /usr/bin/python3 /usr/bin/python

ENV PATH /jdk-11/bin:$PATH
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

# Install Dynamo2m [dynamo2warp, warp2dynamo, relion_star_downgrade]
RUN apt-get install -y python3-pip && pip install dynamo2m

#Dynamo
RUN pip install gdown
RUN gdown https://drive.google.com/uc?id=1Pffjfwu-EXmEzYC5DGSp8YqAPCtg7ye0
#link format is slightly different with provided form.

RUN mkdir /home/dynamoRoot/ && \
    mv dynamo-v-1.1.532_MCR-9.9.0_GLNXA64_withMCR.tar /home/dynamoRoot/dynamo.tar && \
    tar -xf /home/dynamoRoot/dynamo.tar -C /home/dynamoRoot && \
    rm /home/dynamoRoot/dynamo.tar
RUN mv /home/dynamoRoot/MCRLinux/sys/os/glnxa64/libstdc++.so.6 /home/dynamoRoot/MCRLinux/sys/os/glnxa64/libstdc++.so.6.orig

#Dynamo cuda setting
RUN cd /home/dynamoRoot/cuda && source config.sh && make clean && make all

## For autoalign_dynamo : modified for non-interactive docker install.
RUN git clone https://github.com/KJYoung/autoalign_dynamo.git && \
    cd /autoalign_dynamo && ./install.sh

RUN echo 'alias imodcfg="source $IMOD_DIR/IMOD-linux.sh"' >> ~/.bashrc

# For automated GUI connection.
COPY ./setupGUI.sh ./home/
COPY ./matlab.zip ./
RUN mkdir matlab && unzip -q matlab.zip -d matlab
ENTRYPOINT ["bash", "./home/setupGUI.sh"]
############################################################################################
