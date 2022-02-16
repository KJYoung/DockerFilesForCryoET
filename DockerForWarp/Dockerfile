FROM nvidia/cuda:11.4.0-devel-ubuntu20.04

ENV TZ Asia/Seoul
ENV DEBIAN_FRONTEND noninteractive
RUN ln -snf /usr/share/zoneinfo/$TZ /etc/localtime && echo $TZ > /etc/timezone

RUN apt-get update && apt-get install -y dirmngr gnupg apt-transport-https ca-certificates && \
    apt-key adv --keyserver hkp://keyserver.ubuntu.com:80 --recv-keys 3FA7E0328081BFF6A14DA29AA6A19B38D3D831EF && \
    echo "deb https://download.mono-project.com/repo/ubuntu stable-focal main" | tee /etc/apt/sources.list.d/mono-official-stable.list && \
    apt-get update && \
    apt-get install -y mono-complete
# above is for the installation of mono-complete for ubuntu 20.04

RUN apt-get install -y git vim wget cmake g++ software-properties-common libfftw3-dev libtiff-dev nvidia-cuda-toolkit 

# Install Tensorflow
RUN wget "https://storage.googleapis.com/tensorflow/libtensorflow/libtensorflow-gpu-linux-x86_64-2.6.0.tar.gz" -O /libtf-gpu-linux.tar.gz && \
    tar -C /usr/local -xzf /libtf-gpu-linux.tar.gz && ldconfig
ENV LIBRARY_PATH $LIBRARY_PATH:/usr/local/lib
ENV LD_LIBRARY_PATH $LD_LIBRARY_PATH:/usr/local/lib

RUN mkdir /warpRoot && cd /warpRoot && \
    git clone https://github.com/KJYoung/gtom.git

#GTOM compilation
RUN cd /warpRoot/gtom/build && cmake .. && make
################################################## TIME CONSUMING BUILD ##############################################
#Liblion warp
RUN cd /warpRoot && git clone https://github.com/KJYoung/liblion.git && git clone https://github.com/KJYoung/warp.git
#GPUAcceleration.dll
RUN cd /warpRoot/warp/buildGPU && make
#WarpLib.dll
COPY ./warpDLL/*.dll /warpRoot/warp/build/
RUN cp /warpRoot/warp/buildGPU/GPUAcceleration.dll /warpRoot/warp/build && \ 
	cd /warpRoot/warp/build && \
	csc -debug -warn:0 /t:library /out:WarpLib.dll /unsafe \
	/reference:System.Drawing.dll /reference:Accord.dll /reference:Accord.Math.dll /reference:Accord.Math.Core.dll /reference:MathNet.Numerics.dll \
	/reference:BitMiracle.LibTiff.NET.dll /reference:System.Numerics.dll \
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
	../WarpLib/Sociology/*.cs ../WarpLib/Tools/DefectModel.cs \
	../WarpLib/Headers/EER.cs ../WarpLib/TiltSeries.cs ../WarpLib/LinearGrid4D.cs \
	../WarpLib/Tools/EERNative.cs ../WarpLib/Tools/Zernike.cs ../WarpLib/Tools/Timing.cs ../WarpLib/Tools/TiffNative.cs \
	../WarpLib/Tools/NamedSerializableObject.cs ../WarpLib/WorkerWrapper.cs \
	../WarpLib/*.cs ../WarpLib/Tools/*.cs ../WarpLib/Headers/*.cs && \
	csc -warn:0 /out:WarpWorker.exe /reference:WarpLib.dll ../WarpWorker/Program.cs

RUN echo 'alias cdw="cd /warpRoot/warp/build"' >> ~/.bashrc && \
    echo 'alias cr="csc /warn:0 /unsafe /out:warp.exe /reference:/warpRoot/warp/build/WarpLib.dll /reference:/warpRoot/warp/build/Newtonsoft.Json.dll /reference:/warpRoot/warp/build/CommandLine.dll Options.cs FileDiscoverer.cs TomoParticleExport.cs warpMain.cs && mono warp.exe"' >> ~/.bashrc && \
    echo 'alias wk="cd /cdata/warpCLI"' >> ~/.bashrc && \
	echo 'alias wkcfg="cp /warpRoot/warp/buildGPU/GPUAcceleration.dll /cdata/warpCLI && cp /warpRoot/warp/build/WarpLib.dll /cdata/warpCLI "' >> ~/.bashrc
	# Caution : execution of main.exe requires a WarpLib.dll in the same directory!!!

#Wine 7.0
# wine 7.0 install https://wiki.winehq.org/Ubuntu
#RUN dpkg --add-architecture i386 && wget -nc https://dl.winehq.org/wine-builds/winehq.key && apt-key add winehq.key && \
#    add-apt-repository 'deb https://dl.winehq.org/wine-builds/ubuntu/ focal main' && apt-get update && \
#    apt-get install -y --install-recommends winehq-stable

#GPU
#COPY ./setupGUI.sh ./home/
#ENTRYPOINT ["bash", "./home/setupGUI.sh"]
