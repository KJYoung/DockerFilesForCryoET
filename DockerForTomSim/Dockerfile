# Dockerfile for my TomSim - dependencies : PyTom, EMAN2 ( without GUI, without IMOD ).
FROM nvidia/cuda:11.4.0-devel-ubuntu20.04

ENV TZ=Asia/Seoul \
    DEBIAN_FRONTEND=noninteractive
RUN ln -snf /usr/share/zoneinfo/$TZ /etc/localtime && echo $TZ > /etc/timezone

#################### For prerequisite of PyTom #################
# For general setup + python&pip 3.7 + install stuffs.
RUN apt-get update && apt-get install -y git vim wget software-properties-common nvidia-cuda-toolkit \
    fftw3 gcc-7 libxslt-dev swig libfftw3-dev libboost-all-dev csh && \
    update-alternatives --install /usr/bin/gcc gcc /usr/bin/gcc-7 60 && \
    add-apt-repository -y ppa:deadsnakes/ppa && apt-get install -y python3.7 python3-distutils && \
    ln -s /usr/bin/python3.7 /usr/bin/python && \
    wget https://bootstrap.pypa.io/get-pip.py -O get-pip.py && \
    python3.7 get-pip.py && apt-get install -y libpython3.7-dev && ln -sf /usr/bin/python3.7 /usr/bin/python3 && \
    pip install numpy lxml PyQt5 pyqtgraph mrcfile scipy wget periodictable && \
    apt-get install -y libcudnn8
    # for NT2C
# pip install wget is for me
# pip install periodictable is for volume building.

# wget stuffs + install them. (Not required..?)
RUN wget https://download.open-mpi.org/release/open-mpi/v4.1/openmpi-4.1.1.tar.gz && \
    tar -xvf openmpi-4.1.1.tar.gz && rm openmpi-4.1.1.tar.gz && \
    mkdir /tmp/runtime-root && \
    chmod 0700 /tmp/runtime-root && \
    cd openmpi-4.1.1 && ./configure --prefix=/usr/local && make all install && ldconfig

# # ENV LD_LIBRARY_PATH=/usr/local/nvidia/lib:/usr/local/nvidia/lib64:/usr/local/lib:/usr/lib/python3.7/config-3.7m-x86_64-linux-gnu:/usr/lib/x86_64-linux-gnu/
ENV LD_LIBRARY_PATH=$LD_LIBRARY_PATH:/pytom/pytomc/sh_alignment/SpharmonicKit27/:/pytom/pytomc/sh_alignment/frm/swig/:/pytom/external/lib/:/pytom/pytomc/nufft/:/pytom/pytomc/libs/libtomc/libs:/usr/local/nvidia/lib:/usr/local/nvidia/lib64:/usr/local/lib:/usr/lib/python3.7/config-3.7m-x86_64-linux-gnu:/usr/lib/x86_64-linux-gnu/ \
    PATH=$PATH:/root/eman2-sphire-sparx/bin:/jdk-11/bin:/usr/local/nvidia/bin:/usr/local/cuda/bin:/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:/pytom/convert/ \
    PYTHONPATH=:$PYTHONPATH:/root/eman2-sphire-sparx/lib/python3.7/site-packages:/pytom/pytomc:/pytom/pytomc/sh_alignment/frm/swig/:/pytom/external/lib/:/pytom/external/lib/python3.7/site-packages/:/pytom/pytomc/nufft/:/:/pytom/pytomc/swigModules

# # Install PyTom
RUN git clone --recursive https://github.com/FridoF/PyTom.git pytom && cd pytom/pytomc && \
    python3.7 compile.py --pythonVersion 3.7 --target all --includeDir /usr/include/python3.7m /usr/include /usr/local/lib/python3.7/dist-packages/numpy/core/include/numpy/

# # Install EMAN2
RUN wget https://cryoem.bcm.edu/cryoem/static/software/release-2.91/eman2.91_sphire1.4_sparx.linux64.sh -O /home/eman2.91.sh && \
    bash ./home/eman2.91.sh
RUN conda install eman-deps=25 -c cryoem -c defaults -c conda-forge -y


################# Working... #######################
RUN mkdir /NT2C_util && cd NT2C_util && git clone https://github.com/Lihongjia-ict/NoiseTransfer2clean.git && \
    cd NoiseTransfer2clean/noise_synthesizer/pytorch-wgan-master && pip install -r requirements.txt

# RUN echo 'alias pytomcfg="  export LD_LIBRARY_PATH=/usr/local/lib:/usr/lib/x86_64-linux-gnu/:/usr/lib/python3.7/config-3.7m-x86_64-linux-gnu:/usr/lib/x86_64-linux-gnu/:/pytom/pytomc/sh_alignment/SpharmonicKit27/:/pytom/pytomc/sh_alignment/frm/swig/:/pytom/external/lib/:/pytom/pytomc/nufft/:/pytom/pytomc/libs/libtomc/libs:$LD_LIBRARY_PATH && \
#                             export PATH=/jdk-11/bin:/usr/local/nvidia/bin:/usr/local/cuda/bin:/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:/pytom/convert/:$PATH && \
#                             export PYTHONPATH=/root/eman2-sphire-sparx/lib/python3.7/site-packages:/pytom/pytomc:/pytom/pytomc/sh_alignment/frm/swig/:/pytom/external/lib/:/pytom/external/lib/python3.7/site-packages/:/pytom/pytomc/nufft/:/:/pytom/pytomc/swigModules:$PYTHONPATH"' >> ~/.bashrc