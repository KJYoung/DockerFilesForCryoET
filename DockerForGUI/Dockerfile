FROM ubuntu:latest

RUN apt-get update && apt-get install -y nautilus xauth dbus-x11
COPY ./setupGUI.sh ./home/

ENV TESTKJY testValueVKJY
ENTRYPOINT ["bash", "./home/setupGUI.sh"]