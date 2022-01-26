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

#RUN apt-get install -y xauth wine && \
#    dpkg --add-architecture i386 && apt-get update && apt-get install -y wine32

#RUN mkdir dotnetRoot && \
#    wget https://download.visualstudio.microsoft.com/download/pr/ede8a287-3d61-4988-a356-32ff9129079e/bdb47b6b510ed0c4f0b132f7f4ad9d5a/dotnet-sdk-6.0.101-linux-x64.tar.gz -O /dotnetRoot/dotnet-6.0.tar.gz && \
#    cd /dotnetRoot && \
#    tar xvfz dotnet-6.0.tar.gz

#ENV PATH $PATH:/dotnetRoot

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
#    git clone https://github.com/dtegunov/liblion.git && \
#    git clone https://github.com/KJYoung/liblion.git && \
    git clone https://github.com/dtegunov/gtom.git
#    git clone https://github.com/cramerlab/warp.git && \
#    git clone https://github.com/cramerlab/warpcraft.git

COPY ./setupGUI.sh ./home/

# Build gtom
RUN rm /warpRoot/gtom/CMakeLists.txt
COPY ./gtom_modified_CMakeLists.txt /warpRoot/gtom
RUN mv /warpRoot/gtom/gtom_modified_CMakeLists.txt /warpRoot/gtom/CMakeLists.txt && \
    mkdir /warpRoot/gtom/build && \
    cd /warpRoot/gtom/build && \
    cmake .. && \
    make

# Install Tensorflow
RUN wget "https://storage.googleapis.com/tensorflow/libtensorflow/libtensorflow-gpu-linux-x86_64-2.6.0.tar.gz" -O /warpRoot/libtf-gpu-linux.tar.gz && \
    tar -C /usr/local -xzf /warpRoot/libtf-gpu-linux.tar.gz && \
    ldconfig
ENV LIBRARY_PATH $LIBRARY_PATH:/usr/local/lib
ENV LD_LIBRARY_PATH $LD_LIBRARY_PATH:/usr/local/lib

################################################################## TIME CONSUMING BUILD ##############################################
# Install Wine
RUN apt-get install -y wine && dpkg --add-architecture i386 && apt-get update && apt-get install -y wine32

# Update git repo After time consuming jobs.
RUN cd /warpRoot && \
    git clone https://github.com/KJYoung/liblion.git && \
    git clone https://github.com/cramerlab/warp.git && \
    git clone https://github.com/cramerlab/warpcraft.git

# For relion libfftw library
RUN apt-get install -y libfftw3-dev
# About GPUAcceleration.dll
RUN rm /warpRoot/warp/GPUAcceleration/Functions.h
COPY ./Functions.h /warpRoot/warp/GPUAcceleration
COPY ./Makefile    /warpRoot/warp/build/
# About liblion
#RUN rm /warpRoot/liblion/liblion.h
#COPY ./liblion.h /warpRoot/liblion

# Build WarpLib
RUN cd /warpRoot/warp/build && \
    csc -debug -warn:0 /t:library /out:WarpLib.dll /unsafe \
    /reference:System.Drawing.dll /reference:/warpRoot/warpcraft/bin/Accord.dll /reference:/warpRoot/warpcraft/bin/Accord.Math.dll /reference:/warpRoot/warpcraft/bin/MathNet.Numerics.dll \
    /reference:/warpRoot/warpcraft/bin/BitMiracle.LibTiff.NET.dll /reference:System.Numerics.dll \
    ../WarpLib/GPUQueue.cs ../WarpLib/NMAMap.cs ../WarpLib/Tools/ByteReaderBE.cs ../WarpLib/Tools/Matrix3.cs \
    ../WarpLib/Headers/DM4.cs ../WarpLib/Tools/ClusterTrieste.cs ../WarpLib/Tools/Matrix4.cs \
    ../WarpLib/CPU.cs ../WarpLib/Headers/EM.cs ../WarpLib/Tools/FloatVectors.cs ../WarpLib/Tools/PhysicsHelper.cs \
    ../WarpLib/CTF.cs ../WarpLib/Headers/Headers.cs ../WarpLib/ProcessingOptions.cs ../WarpLib/Tools/Helper.cs ../WarpLib/Tools/Quaternion.cs \
    ../WarpLib/Cubic1D.cs ../WarpLib/Headers/MRC.cs ../WarpLib/Projector.cs ../WarpLib/Tools/ImageHelper.cs ../WarpLib/Tools/RandomNormal.cs \
    ../WarpLib/Cubic1DShort.cs ../WarpLib/Headers/Raw.cs ../WarpLib/SoftMap.cs ../WarpLib/Tools/IntVectors.cs ../WarpLib/Tools/Symmetry.cs \
    ../WarpLib/CubicGrid.cs ../WarpLib/Star.cs ../WarpLib/Tools/IOHelper.cs \
    ../WarpLib/FSC.cs ../WarpLib/Image.cs ../WarpLib/Tools/Logger.cs ../WarpLib/Tools/XMLHelper.cs \
    ../WarpLib/GPU.cs ../WarpLib/Movie.cs ../WarpLib/Tools/BenchmarkTimer.cs ../WarpLib/Tools/MathHelper.cs ../WarpLib/WarpBase.cs \
    ../WarpLib/TensorFlowSharp/Buffer.cs ../WarpLib/TensorFlowSharp/Operations.g.cs ../WarpLib/TensorFlowSharp/Tensor.cs ../WarpLib/TensorFlowSharp/Variable.cs \
    ../WarpLib/TensorFlowSharp/OperationsExtras.cs ../WarpLib/TensorFlowSharp/Queue.cs ../WarpLib/TensorFlowSharp/Tensorflow.cs \
    ../WarpLib/NoiseNet3D.cs ../WarpLib/BoxNet2.cs ../WarpLib/BoxNet.cs ../WarpLib/Tools/TFHelper.cs ../WarpLib/Headers/Tiff.cs \
    ../WarpLib/NoiseNet2D.cs \
    ../WarpLib/Sociology/DataSource.cs ../WarpLib/Sociology/Species.cs ../WarpLib/Sociology/Particle.cs ../WarpLib/Tools/DefectModel.cs \
    ../WarpLib/Headers/EER.cs ../WarpLib/TiltSeries.cs ../WarpLib/LinearGrid4D.cs \
    ../WarpLib/Tools/EERNative.cs ../WarpLib/Tools/Zernike.cs ../WarpLib/Tools/Timing.cs ../WarpLib/Tools/TiffNative.cs

RUN wget "https://dl.winehq.org/wine/wine-mono/7.0.0/wine-mono-7.0.0-x86.msi" -O "/warpRoot/wine-mono.msi" && \
    wine msiexec /i /warpRoot/wine-mono.msi && \
    echo 'alias warpcli="wine /warpRoot/warpcraft/bin/warpcraft.exe"' >> ~/.bashrc
ENTRYPOINT ["bash", "./home/setupGUI.sh"]
