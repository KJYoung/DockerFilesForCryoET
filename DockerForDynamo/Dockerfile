FROM ubuntu:latest
  
RUN apt-get update && apt-get install -y \
        wget pip libxt6
RUN pip install gdown

RUN gdown https://drive.google.com/uc?id=1Pffjfwu-EXmEzYC5DGSp8YqAPCtg7ye0
#link format is slightly different with provided form.

RUN mkdir /home/dynamoRoot/ && \
    mv dynamo-v-1.1.532_MCR-9.9.0_GLNXA64_withMCR.tar /home/dynamoRoot/dynamo.tar && \
    tar -xf /home/dynamoRoot/dynamo.tar -C /home/dynamoRoot && \
    rm /home/dynamoRoot/dynamo.tar

RUN mv /home/dynamoRoot/MCRLinux/sys/os/glnxa64/libstdc++.so.6 /home/dynamoRoot/MCRLinux/sys/os/glnxa64/libstdc++.so.6.orig
RUN echo 'alias dynamocfg="source /home/dynamoRoot/dynamo_activate_linux_shipped_MCR.sh"' >> ~/.bashrc