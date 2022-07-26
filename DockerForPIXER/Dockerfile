# Dockerfile for just NT2C - dependencies : PyTom, EMAN2 ( without GUI, without IMOD ).
# Caffe-cuda is not available in 20.04
FROM nvidia/cuda:11.6.0-devel-ubuntu18.04

ENV TZ=Asia/Seoul \
    DEBIAN_FRONTEND=noninteractive
RUN ln -snf /usr/share/zoneinfo/$TZ /etc/localtime && echo $TZ > /etc/timezone

# For general setup.
RUN apt-get update && apt-get install -y git vim wget software-properties-common nvidia-cuda-toolkit caffe-cuda

# Prepare python, pip
RUN add-apt-repository -y ppa:deadsnakes/ppa && apt-get install -y python3.7 python3-distutils && \
    ln -sf /usr/bin/python3.7 /usr/bin/python && \
    wget https://bootstrap.pypa.io/get-pip.py -O get-pip.py && \
    python3.7 get-pip.py

# Prep for pycuda
RUN apt-get install -y python-dev libxml2-dev libxslt-dev python3.7-dev libopenmpi-dev
RUN pip install mrcfile pycuda mpi4py
RUN apt-get install -y libgoogle-glog-dev libcudnn8
RUN apt-get install -y libboost-all-dev libatlas-base-dev
RUN apt-get install -y cmake g++ wget unzip && \
    # Download and unpack sources
    wget -O opencv.zip https://github.com/opencv/opencv/archive/4.x.zip && \
    wget -O opencv_contrib.zip https://github.com/opencv/opencv_contrib/archive/4.x.zip && \
    unzip opencv.zip && \
    unzip opencv_contrib.zip && \
    # Create build directory and switch into it
    mkdir -p build && cd build && \
    # Configure
    cmake -DOPENCV_EXTRA_MODULES_PATH=../opencv_contrib-4.x/modules ../opencv-4.x && \
    # Build
    cmake --build . && make install
# install hdf5
RUN apt-get install -y libhdf5-serial-dev libmatio-dev libgflags-dev libgoogle-glog-dev liblmdb-dev libleveldb-dev
RUN cd /usr/lib/x86_64-linux-gnu/ && ln -s libhdf5_serial.so.100.0.1 libhdf5.so && ln -s libhdf5_serial_hl.so.100.0.0 libhdf5_hl.so && ln -s libsnappy.so.1.1.7 libsnappy.so
RUN apt-get install -y time


RUN pip install opencv-python scikit-image mpi4py
# RUN wget https://github.com/protocolbuffers/protobuf/releases/download/v3.5.1/protobuf-all-3.5.1.zip && unzip protobuf-all-3.5.1.zip && \
#     cd protobuf-3.5.1/ && ./configure && make && make install && ldconfig
RUN wget https://github.com/protocolbuffers/protobuf/releases/download/v3.11.1/protobuf-all-3.11.1.zip && unzip protobuf-all-3.11.1.zip && \
    rm protobuf-all-3.11.1.zip && cd protobuf-3.11.1/ && ./configure && make && make install && ldconfig

# install EMAN2

# RUN apt-get update && apt-get install -y libglu1-mesa libxi-dev libxmu-dev libglu1-mesa-dev mesa-utils libgl1-mesa-glx
RUN wget https://cryoem.bcm.edu/cryoem/static/software/release-2.91/eman2.91_sphire1.4_sparx.linux64.sh -O /home/eman2.91.sh && chmod +x /home/eman2.91.sh && bash ./home/eman2.91.sh
ENV PATH $PATH:/root/eman2-sphire-sparx/bin

RUN pip install opencv-python mpi4py future scikit-image pycuda
ENV CPLUS_INCLUDE_PATH $CPLUS_INCLUDE_PATH:/usr/include/python3.7/
RUN wget https://boostorg.jfrog.io/artifactory/main/release/1.69.0/source/boost_1_69_0.tar.bz2 && \
    tar -xvf boost_1_69_0.tar.bz2 && rm boost_1_69_0.tar.bz2 && \
    cd boost_1_69_0 && ./bootstrap.sh && \
    ./b2
ENV LD_LIBRARY_PATH=/usr/local/nvidia/lib:/usr/local/nvidia/lib64:/temp/boost_1_69_0/stage/lib/
# RUN apt-get install -y libgsl-dev libjpeg9-dev && \
#     cd /usr/lib/x86_64-linux-gnu/ && ln -s libhdf5.so libhdf5.so.10
# RUN wget http://www.fftw.org/fftw-3.3.10.tar.gz && tar -zxvf fftw-3.3.10.tar.gz && \
#     rm fftw-3.3.10.tar.gz && cd fftw-3.3.10 && \
#     ./configure --prefix=/usr --enable-shared --disable-static --enable-threads --enable-sse2 --enable-avx && make && \
#     make install && \
#     make clean && ./configure --prefix=/usr --enable-shared --disable-static --enable-threads --enable-sse2 --enable-avx --enable-float && make && \
#     make install && \
#     make clean && ./configure --prefix=/usr --enable-shared --disable-static --enable-threads --enable-long-double && make && \
#     make install
# RUN apt-get install -y libdb-dev && pip install bsddb3
# ENV LIBGL_ALWAYS_INDIRECT 1
# ENV QT_XKB_CONFIG_ROOT /usr/share/X11/xkb
# Should be next to the ENV
# RUN conda install eman-deps=25 -c cryoem -c defaults -c conda-forge -y
# RUN wget https://github.com/protocolbuffers/protobuf/releases/download/v21.3/protobuf-all-21.3.tar.gz && \
#     tar -xf protobuf-all-21.3.tar.gz && cd protobuf-21.3 && ./configure && \
#     make && make check && make install && ldconfig
# For ATLAS
# RUN wget https://sourceforge.net/projects/math-atlas/files/latest/download -O atlas3.10.3.tar.bz2 && \
#     tar -xvf atlas3.10.3.tar.bz2
#     fftw3 gcc-7 libxslt-dev swig libfftw3-dev libboost-all-dev csh libgl1-mesa-glx && \
#     update-alternatives --install /usr/bin/gcc gcc /usr/bin/gcc-7 60 && \
#     add-apt-repository -y ppa:deadsnakes/ppa && apt-get install -y python3.7 python3-distutils && \
#     ln -s /usr/bin/python3.7 /usr/bin/python && \
#     wget https://bootstrap.pypa.io/get-pip.py -O get-pip.py

# RUN apt-get install -y python3.7-distutils && python3.7 get-pip.py && apt-get install -y libpython3.7-dev && ln -sf /usr/bin/python3.7 /usr/bin/python3 && \
#     pip install matplotlib scikit_learn numpy lxml PyQt5 pyqtgraph mrcfile scipy wget periodictable opencv-python mahotas scikit-image && \
#     pip install torch==1.8.1+cu111 torchvision==0.9.1+cu111 -f https://download.pytorch.org/whl/torch_stable.html && \
#     pip install tensorflow==2.5.0 && \
#     pip install numpy --upgrade --ignore-installed && \
#     pip install pandas && \
#     apt-get install -y libcudnn8