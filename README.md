# Working on a Docker
※ Terminal input is written as $echo form.
※ Disclaimer : The following information might not be the best way. However, it is correct way for now and the current settings of server(2022/Jan)...

## Docker General

1. Docker is different from Virtual Machine! Docker engine is located in the upper level compared to host OS(Therefore, it is much faster[Memory access, File I/O, Network access, ...] than VM). More theoretical stuffs could be accessed from google:)
2. Before starting to work with docker, you might need to request the docker user permission to the Server administrator. If you want to check the permission, you can test with some commands(such as “$docker ps”, “$docker images”, ...)
3. Docker helps you to make the independent environment for each programs or purpose. When we use Docker, there is two key concepts : Docker image, Docker container.
  1. We “build” the docker image with “Dockerfile” and “$docker build” command.
  2. We “run” the existing docker image as an individual docker container with “$docker run” command. We can iteratively make the docker container by the docker image.
4. In summary, if you want to build a new docker image which can be instantiated into docker containers, you have to do just the following two things.
  1. Write a “Dockerfile”
  2. Build a “Docker image”
  3. Then, you can make a docker container from the built docker image.
5. All of the docker commands are formatted as “$docker <command>” form.
  1. (ex.) $docker images, $docker ps, $docker build, $docker run, ... 

## Docker Commands..

1. search : Search the pre-existing images from the Dockerhub.
    * (ex.) docker search <keyword>
2. pull : Download the docker image from the Dockerhub.
    * (ex.) docker pull <image name>:<tag>
    * For  <tag>, you can just give “latest”.
3. images : Print all the docker images you have now.
    * (ex.) docker images
4. build : Make a docker image from the Dockerfile.
    * (ex.) docker build <options> <location of Dockerfile>
    * With --tag option, you can specify the tag of the images.
5. run : Make a docker container from the existing docker image.
    * (ex.) docker run <options> <image name> <file to execute>
    * Generally, you would use run command with -it, --name, --rm, (-e, --net=host [for GUI]) options.
6. ps : Print the list of running containers. (With -a option, also print the stopped containers)
    * (ex.) docker ps -a
7. rm, rmi : Remove a container or an image, respectively. (With -f option, force the remove)
8. There are many other commands(start, stop, restart, attach, history, cp, commit, diff, inspect, push, ...). However, if you just want to use already-built docker images, run command is sufficient for the purpose!
  
## Docker Build & Run
### Write the Dockerfile.
To build our own new docker image, we should make a Dockerfile. The following code block is the example of Dockerfile(modified from Dockerfile for Eman2).
```
FROM ubuntu:latest

# Comment  
RUN apt-get update && apt-get install -y \
    wget \
    xauth \
    mesa-utils libgl1-mesa-glx

RUN wget "https://cryoem.bcm.edu/cryoem/static/software/release-2.91/eman2.91_sphire1.4_sparx.linux64.sh" -O /home/eman2.91.sh

ENV PATH /root/eman2-sphire-sparx/bin:$PATH

RUN conda install eman-deps=25 -c cryoem -c defaults -c conda-forge -y

COPY ./setupGUI.sh ./home/
ENTRYPOINT ["bash", "./home/setupGUI.sh"]
```
As you can see from the example above, Dockerfile has a simple grammar, “<COMMAND> <ARGUMENT>”
1. First of all, you have to specify the basis of your docker image with FROM.
  1. “FROM scratch” : basis as an empty image
  2. “FROM ubuntu:latest” : basis as an latest ubuntu image
2. Then, you can specify what you want to do in the container.
  1. MAINTAINER
    1. Specify the image’s author metadata.
  2. RUN
    1. Run the shell script or commands. During the docker image building, commands cannot get a user-input. Therefore, you have to deal with some input-needed commands. (ex. apt-get install commands should be used with -y options. Moreover, some program(such as tzdata, keyboard-configuration) require user-input during installation even with the -y option so that you have to deal with those problem.)
  3. ENV
    1. Set the environment variable. Don’t use ”=” sign.
    2. (ex.) ENV PATH $PATH:/usr/local/bin
  4. COPY
    1. Copy the file. The destination doesn’t include the file name(just its location!).
    2. (ex.) COPY ./setupGUI.sh ./home/
      : Copy from “./setupGUI.sh” to “./home/setupGUI.sh”
  5. ENTRYPOINT
    1. Execute specified script or command once container is initiated(docker run or docker start).
    2. Similar with CMD(Slightly different).
    3. (ex. with sh) ENTRYPOINT touch /home/test.txt
    4. (ex. without sh) ENTRYPOINT [”/home/test.sh”]
    5. (ex. without sh with parameter) ENTRYPOINT [”/home/test2.sh”, “--param1=1”, “--param2=2”]
  6. VOLUME
    1. equivalent with -v option of docker run command.
  7. ADD, CMD, EXPOSE, ...

Build the Docker image.
If you have valid Dockerfile, you can build the docker image with docker build command only. Let’s see an example. Assume you are in /home and /home/dockerForEMAN has the Dockerfile(filename is “Dockerfile” literally). Then, you can build the Docker image with one of the following commands.

  $ docker build --tag <Image Name> <path for dockerForEMAN directory>
 
Then, you can see the generating procedure immediately and the generated image with docker images command.
 
Run the Docker container.
Docker Run Options
  -it
    For the interactive bash shell interaction with docker container.
  --name <CONTAINER NAME>
    Specify the name of container.
  --rm
    Remove the container automatically after getting out of the container.
  -v <ABSOLUTE PATH of HostOS>:<ABSOLUTE PATH of Container>
    Share a disk volume.
  -e <Environment Variable>
    Share an environment variable.
  --net=host
    Port related works : Refer
  -p <Host port number>:<Container port number>
    Open the specific container’s port and connect to the specific host port
Examples
  $docker run -it --rm --net=host -e DISPLAY --name gui_test gui_kjy
  $docker run -it --rm --name no_gui gui_kjy
  $docker run -it --rm --name disk_share -v /home/kimv/:/home/exinput eman2_kjy
Other things
You can get out of the current docker container with “$exit”.
Docker GUI(Write based on Mac environment)
Basic GUI Settings
1. First, you have to make a connection between server and your Mac machine(marked as local below).
  1. In your local terminal, you have to install xquartz.
    1. >>brew install xquartz
    2. Reboot your local machine.
    3. Use -X option for ssh connection and test your connection.
      (ex.) I tested with the “nautilus”(GUI-based Directory Viewer). If you successfully made a connection, the GUI window would appear after the “nautilus” commands.
  2. Although you already connected server and local, GUI connection seems to be disconnected from time to time if you continue to connect to the server(or when you do some specific action). If the GUI connection is disconnected, you can disconnect from the server and re-connect through ssh again.
    1. If your GUI connection is broken, you would see the messages similar to the following.
      (org.gnome.Nautilus:13): Gtk-WARNING **: 05:32:09.276: cannot open display: localhost:10.0
2. Second, you have to make a connection between server and your docker container.
  1. [server] Run the following command, and copy the output(if output is multiline, choose just one line or delete others to make single line). The output will change when you re-connect to the server. 
    $ xauth list
  2. [server] Execute docker run command with the following options.
    --net=host -e DISPLAY
  3. [docker container] Run the following command.
    $ xauth add <the copied output>
  4. [docker container] Finished! However, you might see lots of graphics-related error when you execute the GUI-based program. You should solve these error then(Probably with “install something, set some environment variable, etc”).
3. You can automate these steps.
  a. Write .sh file like this(Let’s assume this file’s name “setupGUI.sh” and share a same location with Dockerfile).
  
#!/bin/bash
bash 
xauth add $@
  
  b. Write the following lines in Dockerfile.
  
COPY ./setupGUI.sh /home
...
ENTRYPOINT ["bash", "/home/setupGUI.sh"]
  
  c. Then, execute the docker run command with “$(xauth list)”
  (ex.) docker run -it --rm --net=host -e DISPLAY --name kjy_gui2 gui_kjy “$(xauth list)”
For OpenGL
You should type the following commands in your local terminal!

$defaults write org.xquartz.X11 enable_iglx –bool true

This commands make an effect in the following codes(in /opt/X11/bin/startx)

opt-X11-bin-startx_ default write usage.png

Docker Images for Cryo-ET
<NAME> : name for the container
$ : in the server.
$$ : in the docker container.
Dockerfiles are available at https://github.com/KJYoung/DockerFilesForCryoET
MotionCor2
$docker run --rm -it --name <NAME> motioncor2_kjy
$$motioncor2 --help
Warp
with pre-compiled version 1.0.0
$docker run --rm -it --net=host -e DISPLAY --name <NAME> warpcli_kjy "$(xauth list)"
$$warpcli
with compiled version 1.0.9 : Currently trying...
IMOD
$docker run --rm -it --name <NAME> --net=host -e DISPLAY imod_kjy "$(xauth list)"
$$imodcfg
$$imod
EMAN2
with GUI
$docker run --rm -it --name <NAME> --net=host -e DISPLAY eman2_kjy "$(xauth list)"
$$e2version.py
with GUI : $$e2display.py can be executed.

without GUI
$docker run --rm -it --name <NAME> eman2_kjy
$$e2version.py

There is many python files can be executed. The following figure shows the procedure to test EMAN2(without GUI, we cannot execute e2display.py.

eman2 test.png
Dynamo
$docker run --rm -it --name <NAME> dynamo_kjy
$$dynamocfg
$$dynamo
CTFFIND4
$docker run --rm -it --name <NAME> ctff_kjy
$$ctffind
RELION
$docker run --rm -it --name <NAME> relion_kjy
$$relion_... (There are many scripts to run. ex) relion_prepare_subtomogram)
