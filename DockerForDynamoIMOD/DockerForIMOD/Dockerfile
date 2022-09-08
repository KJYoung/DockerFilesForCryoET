# IMOD.
# This version is configured for GUI version too. You can extend this with setupGUI.sh.
FROM nvidia/cuda:11.6.0-devel-ubuntu20.04

ENV DEBIAN_FRONTEND noninteractive
ENV TZ Asia/Seoul
RUN ln -snf /usr/share/zoneinfo/$TZ /etc/localtime && echo $TZ > /etc/timezone

RUN apt-get update && apt-get install -y \
    wget vim python3 \
    libglu1-mesa libxi-dev libxmu-dev libglu1-mesa-dev \
    libxcb-xinerama0 libxrender1 libxkbcommon-dev \
    xauth fontconfig mesa-utils xorg

#mesa-utils for glxgears
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

RUN wget https://bio3d.colorado.edu/imod/AMD64-RHEL5/imod_4.11.12_RHEL7-64_CUDA10.1.sh && \
    sh imod_4.11.12_RHEL7-64_CUDA10.1.sh -y && \
    rm imod_4.11.12_RHEL7-64_CUDA10.1.sh && \
    mkdir /tmp/runtime-root && \
    chmod 0700 /tmp/runtime-root

RUN echo 'alias imodcfg="source $IMOD_DIR/IMOD-linux.sh"' >> ~/.bashrc
RUN chmod a+rwx /usr/local/IMOD/IMOD-linux.sh
