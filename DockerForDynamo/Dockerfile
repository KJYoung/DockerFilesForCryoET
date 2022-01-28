FROM ubuntu:latest

# For Non-interactive docker install.
ENV TZ Asia/Seoul
RUN ln -snf /usr/share/zoneinfo/$TZ /etc/localtime && echo $TZ > /etc/timezone
ENV DEBIAN_FRONTEND noninteractive

# Install..
RUN apt-get update && apt-get install -y \
    wget pip libxt6 octave git xauth
RUN pip install gdown

RUN gdown https://drive.google.com/uc?id=1Pffjfwu-EXmEzYC5DGSp8YqAPCtg7ye0
#link format is slightly different with provided form.

RUN mkdir /home/dynamoRoot/ && \
    mv dynamo-v-1.1.532_MCR-9.9.0_GLNXA64_withMCR.tar /home/dynamoRoot/dynamo.tar && \
    tar -xf /home/dynamoRoot/dynamo.tar -C /home/dynamoRoot && \
    rm /home/dynamoRoot/dynamo.tar

RUN mv /home/dynamoRoot/MCRLinux/sys/os/glnxa64/libstdc++.so.6 /home/dynamoRoot/MCRLinux/sys/os/glnxa64/libstdc++.so.6.orig

# For autoalign_dynamo : modified for non-interactive docker install.
RUN git clone https://github.com/KJYoung/autoalign_dynamo.git && \
    cd /autoalign_dynamo && \
    ./install.sh

ENV LIBGL_ALWAYS_INDIRECT 1
RUN echo 'alias dynamocfg="source /home/dynamoRoot/dynamo_activate_linux_shipped_MCR.sh"' >> ~/.bashrc
RUN echo 'alias autoalign="octave --persist /opt/autoalign_dynamo/autoalign_activate.m"' >> ~/.bashrc

# For automated GUI connection.
COPY ./setupGUI.sh ./home/
ENTRYPOINT ["bash", "./home/setupGUI.sh"]
