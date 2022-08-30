FROM nvidia/cuda:11.6.0-devel-ubuntu20.04

ENV TZ=Asia/Seoul \
    DEBIAN_FRONTEND=noninteractive
RUN ln -snf /usr/share/zoneinfo/$TZ /etc/localtime && echo $TZ > /etc/timezone

RUN apt-get update && apt-get install -y cmake g++ nvidia-cuda-toolkit


# install mono-complete
RUN apt-get install -y gnupg ca-certificates && \
    apt-key adv --keyserver hkp://keyserver.ubuntu.com:80 --recv-keys 3FA7E0328081BFF6A14DA29AA6A19B38D3D831EF && \
    echo "deb https://download.mono-project.com/repo/ubuntu stable-focal main" | tee /etc/apt/sources.list.d/mono-official-stable.list && \
    apt-get update && \
    apt-get install -y mono-complete

RUN apt-get install -y libfftw3-dev libcudnn8 wget libtiff-dev
ENV LD_LIBRARY_PATH=$LD_LIBRARY_PATH:/usr/lib/x86_64-linux-gnu/

# install tensorflow
# RUN wget https://storage.googleapis.com/tensorflow/libtensorflow/libtensorflow-gpu-linux-x86_64-1.10.0.tar.gz && \
#     tar -C /usr/local -xzf libtensorflow-gpu-linux-x86_64-1.10.0.tar.gz && \
#     rm libtensorflow-gpu-linux-x86_64-1.10.0.tar.gz && ldconfig
RUN wget https://storage.googleapis.com/tensorflow/libtensorflow/libtensorflow-gpu-linux-x86_64-2.5.0.tar.gz && \
    tar -C /usr/local -xzf libtensorflow-gpu-linux-x86_64-2.5.0.tar.gz && \
    rm libtensorflow-gpu-linux-x86_64-2.5.0.tar.gz && ldconfig

RUN echo "alias cwp='cd /cdata/warp/build && csc -debug -warn:0 /t:library /out:WarpLib.dll /unsafe /reference:System.Drawing.dll /reference:/cdata/dlls/Accord.dll /reference:/cdata/dlls/Accord.Math.dll /reference:/cdata/dlls/Accord.Math.Core.dll /reference:/cdata/dlls/MathNet.Numerics.dll /reference:/cdata/dlls/BitMiracle.LibTiff.NET.dll /reference:System.Numerics.dll ../WarpLib/GPUQueue.cs ../WarpLib/NMAMap.cs ../WarpLib/Tools/ByteReaderBE.cs ../WarpLib/Tools/Matrix3.cs ../WarpLib/Headers/DM4.cs ../WarpLib/Tools/ClusterTrieste.cs ../WarpLib/Tools/Matrix4.cs ../WarpLib/CPU.cs ../WarpLib/Headers/EM.cs ../WarpLib/Tools/FloatVectors.cs ../WarpLib/Tools/PhysicsHelper.cs ../WarpLib/CTF.cs ../WarpLib/Headers/Headers.cs ../WarpLib/ProcessingOptions.cs ../WarpLib/Tools/Helper.cs ../WarpLib/Tools/Quaternion.cs ../WarpLib/Cubic1D.cs ../WarpLib/Headers/MRC.cs ../WarpLib/Projector.cs ../WarpLib/Tools/ImageHelper.cs ../WarpLib/Tools/RandomNormal.cs ../WarpLib/Cubic1DShort.cs ../WarpLib/Headers/Raw.cs ../WarpLib/SoftMap.cs ../WarpLib/Tools/IntVectors.cs ../WarpLib/Tools/Symmetry.cs ../WarpLib/CubicGrid.cs ../WarpLib/Star.cs ../WarpLib/Tools/IOHelper.cs ../WarpLib/FSC.cs ../WarpLib/Image.cs ../WarpLib/Tools/Logger.cs ../WarpLib/Tools/XMLHelper.cs ../WarpLib/GPU.cs ../WarpLib/Movie.cs ../WarpLib/Tools/BenchmarkTimer.cs ../WarpLib/Tools/MathHelper.cs ../WarpLib/WarpBase.cs ../WarpLib/TensorFlowSharp/Buffer.cs ../WarpLib/TensorFlowSharp/Operations.g.cs ../WarpLib/TensorFlowSharp/Tensor.cs ../WarpLib/TensorFlowSharp/Variable.cs ../WarpLib/TensorFlowSharp/OperationsExtras.cs ../WarpLib/TensorFlowSharp/Queue.cs ../WarpLib/TensorFlowSharp/Tensorflow.cs ../WarpLib/NoiseNet3D.cs ../WarpLib/BoxNet2.cs ../WarpLib/BoxNet.cs ../WarpLib/Tools/TFHelper.cs ../WarpLib/Headers/Tiff.cs ../WarpLib/NoiseNet2D.cs ../WarpLib/Sociology/DataSource.cs ../WarpLib/Sociology/Species.cs ../WarpLib/Sociology/Particle.cs ../WarpLib/Tools/DefectModel.cs ../WarpLib/Headers/EER.cs ../WarpLib/TiltSeries.cs ../WarpLib/LinearGrid4D.cs ../WarpLib/Tools/EERNative.cs ../WarpLib/Tools/Zernike.cs ../WarpLib/Tools/Timing.cs ../WarpLib/Tools/TiffNative.cs ../WarpLib/Tools/NamedSerializableObject.cs ../WarpLib/WorkerWrapper.cs ../WarpLib/Tools/ImodHelper.cs && cp /cdata/warp/build/WarpLib.dll /cdata/dlls/runtime/ && cd -'" >> ~/.bashrc
RUN echo "alias rec='cd /cdata/dlls/runtime && csc /warn:0 /out:pp.exe /unsafe /reference:/cdata/warp/build/WarpLib.dll /reference:System.Drawing.dll /reference:/cdata/dlls/Accord.dll /reference:/cdata/dlls/Accord.Math.dll /reference:/cdata/dlls/Accord.Math.Core.dll /reference:/cdata/dlls/MathNet.Numerics.dll /reference:/cdata/dlls/BitMiracle.LibTiff.NET.dll /reference:System.Numerics.dll /reference:/cdata/dlls/CommandLine.dll /reference:/cdata/dlls/Newtonsoft.Json.dll /cdata/warpCLI/Options.cs /cdata/warpCLI/FileDiscoverer.cs /cdata/warpCLI/GlobalOptions.cs /cdata/warpCLI/StackGeneration.cs /cdata/warpCLI/TomoReconstruction.cs /cdata/warpCLI/Program.cs'" >> ~/.bashrc

# export LD_LIBRARY_PATH=/home/kimv/tf1_15/lib
# export LIBRARY_PATH=/home/kimv/tf1_15/lib
# export LD_LIBRARY_PATH=/home/kimv/tensorflow/lib
# export LIBRARY_PATH=/home/kimv/tensorflow/lib