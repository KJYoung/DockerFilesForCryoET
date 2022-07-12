# Dockerfile for just NT2C in devbox002.
FROM nvidia/cuda:11.6.0-devel-ubuntu20.04

ENV TZ=Asia/Seoul \
    DEBIAN_FRONTEND=noninteractive
RUN ln -snf /usr/share/zoneinfo/$TZ /etc/localtime && echo $TZ > /etc/timezone

# For general setup + python&pip 3.7 + install stuffs.
RUN apt-get update && apt-get install -y git vim wget software-properties-common nvidia-cuda-toolkit \
    fftw3 gcc-7 libxslt-dev swig libfftw3-dev libboost-all-dev csh libgl1-mesa-glx && \
    update-alternatives --install /usr/bin/gcc gcc /usr/bin/gcc-7 60 && \
    add-apt-repository -y ppa:deadsnakes/ppa && apt-get install -y python3.7 python3-distutils && \
    ln -s /usr/bin/python3.7 /usr/bin/python && \
    wget https://bootstrap.pypa.io/get-pip.py -O get-pip.py

RUN apt-get install -y python3.7-distutils && python3.7 get-pip.py && apt-get install -y libpython3.7-dev && ln -sf /usr/bin/python3.7 /usr/bin/python3 && \
    pip install matplotlib scikit_learn numpy lxml PyQt5 pyqtgraph mrcfile scipy wget periodictable opencv-python mahotas scikit-image && \
    pip install torch==1.8.1+cu111 torchvision==0.9.1+cu111 -f https://download.pytorch.org/whl/torch_stable.html && \
    pip install tensorflow==2.5.0 && \
    pip install numpy --upgrade --ignore-installed && \
    pip install pandas && \
    apt-get install -y libcudnn8