FROM ubuntu:latest

RUN apt-get update && apt-get install -y \
    wget \
    libglu1-mesa libxi-dev libxmu-dev libglu1-mesa-dev \
    xauth \
    mesa-utils libgl1-mesa-glx   

RUN wget https://cryoem.bcm.edu/cryoem/static/software/release-2.91/eman2.91_sphire1.4_sparx.linux64.sh -O /home/eman2.91.sh

RUN bash ./home/eman2.91.sh

ENV PATH /root/eman2-sphire-sparx/bin:$PATH
ENV LIBGL_ALWAYS_INDIRECT 1
ENV QT_XKB_CONFIG_ROOT /usr/share/X11/xkb
# Should be next to the ENV
RUN conda install eman-deps=25 -c cryoem -c defaults -c conda-forge -y

COPY ./setupGUI.sh ./home/
ENTRYPOINT ["bash", "./home/setupGUI.sh"]
