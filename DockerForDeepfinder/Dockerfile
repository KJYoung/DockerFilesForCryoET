FROM nvidia/cuda:11.4.0-devel-ubuntu20.04

ENV TZ Asia/Seoul
ENV DEBIAN_FRONTEND noninteractive
RUN ln -snf /usr/share/zoneinfo/$TZ /etc/localtime && echo $TZ > /etc/timezone

RUN apt-get update && apt-get install -y git vim wget software-properties-common nvidia-cuda-toolkit xauth && \
    add-apt-repository -y ppa:deadsnakes/ppa && apt-get install -y python3.7 python3-distutils && \
    ln -s /usr/bin/python3.7 /usr/bin/python && \
    wget https://bootstrap.pypa.io/get-pip.py -O get-pip.py && \
    python3.7 get-pip.py

RUN git clone https://gitlab.inria.fr/serpico/deep-finder.git

RUN cd deep-finder && pip install -r requirements_gpu.txt
ENTRYPOINT ["bash", "./home/setupGUI.sh"]