# Working on a Docker
※ Terminal input is written as $echo form.   
※ Disclaimer : The following information might not be the best way. However, it is correct way for now and the current settings of server(2022/March)...

## Docker General
### [Docker Overview_Github.pdf](https://github.com/KJYoung/DockerFilesForCryoET/blob/master/Docker%20Overview_Github.pdf) file would be helpful!

* Docker is different from Virtual Machine! Docker engine is located in the upper level compared to host OS(Therefore, it is much faster[Memory access, File I/O, Network access, ...] than VM). More theoretical stuffs could be accessed from google:)
* Before starting to work with docker, you might need to request the docker user permission to the Server administrator. If you want to check the permission, you can test with some commands(such as `$docker ps`, `$docker images`, ...)
* Docker helps you to make the independent environment for each programs or purpose. When we use Docker, there is two key concepts : Docker image, Docker container.
    * We “build” the docker image with “Dockerfile” and `$docker build` command.
    * We “run” the existing docker image as an individual docker container with `$docker run` command. We can iteratively make the docker container by the docker image.
* In summary, if you want to build a new docker image which can be instantiated into docker containers, you have to do just the following two things.
    * Write a “Dockerfile”
    * Build a “Docker image”
    * Then, you can make a docker container from the built docker image.
* All of the docker commands are formatted as `$docker <command>` form.
    * (ex.) `$docker images`, `$docker ps`, `$docker build`, `$docker run`, ... 

## Docker Commands..

* pull : Download the docker image from the Dockerhub.
    * (ex.) `docker pull <image name>:<tag>`
    * For  <tag>, you can just give “latest”.
* images : Print all the docker images you have now.
    * (ex.) docker images
* build : Make a docker image from the Dockerfile.
    * (ex.) `docker build <options> <location of Dockerfile>`
    * With --tag option, you can specify the tag of the images.
* run : Make a docker container from the existing docker image.
    * (ex.) `docker run <options> <image name> <file to execute>`
    * Generally, you would use run command with -it, --name, --rm, (-e, --net=host [for GUI]) options.
* ps : Print the list of running containers. (With -a option, also print the stopped containers)
    * (ex.) `docker ps -a`
* rm, rmi : Remove a container or an image, respectively. (With -f option, force the remove)
* There are many other commands(start, stop, restart, attach, history, cp, commit, diff, inspect, push, ...). However, build&run command is sufficient for many situation.
  
## Docker Build & Run.
### 1. Start point for docker : Tutorial.
1. Make a workspace directory. Let's assume "test" directory.   
2. Make a file named "Dockerfile" in test directory.   
3. Write just the following : ''' FROM ubuntu:20.04 '''   
4. Execute the following : ''' docker build --tag testimage .   
5. Execute the following : ''' docker run -it --rm --name testcontainer testimage
### 2. Write Custom Dockerfile.
To build our own docker image, we should modify the Dockerfile.   
The following code block is the example of Dockerfile(NOT WORKING, JUST FOR THE SYNTAX EXAMPLE).

```
# Specify the Base images : You can find these base images from hub.docker.com
FROM ubuntu:latest

# Ex) Execute commands : Install packages
RUN apt-get update && apt-get install -y [INSTALL PACKAGE NAMES]

# Ex) Execute commands : Wget downloads
RUN wget [Link] -O [Output File Directory]

# Ex) Setting environment variable
ENV PATH /root/eman2-sphire-sparx/bin:$PATH

# Ex) Copy files from the same directory of the dockerfile into the image inside.
COPY ./setupGUI.sh ./home/
```
  
As you can see from the example above, Dockerfile has a simple grammar, `“[COMMAND] [ARGUMENT]”`
* First of all, you have to specify the basis of your docker image with FROM.
    * `FROM scratch` : basis as an empty image
    * `FROM ubuntu:latest` : basis as an latest ubuntu image
    * `FROM ubuntu:20.04` : specify the specific tag of the image.
    * You can find these base images from [*Docker hub*](https://docs.docker.com/)

* Then, you can specify what you want to do in the container.
    * MAINTAINER
        * Specify the image’s author metadata.
    * RUN
        * Run the shell script or commands. During the docker image building, commands cannot get a user-input. Therefore, you have to deal with some user-input-required situations. (ex. apt-get install commands should be used with -y options. Moreover, some program(such as tzdata, keyboard-configuration) require user-input during installation even with the -y option so that you have to deal with those problem.)
        * Most of the case, the following lines will help.
          ```
          ENV TZ=Asia/Seoul \
          DEBIAN_FRONTEND=noninteractive
          RUN ln -snf /usr/share/zoneinfo/$TZ /etc/localtime && echo $TZ > /etc/timezone
          ```
    * ENV
        * Set the environment variable. Don’t use ”=” sign.
        * (ex.) ENV PATH $PATH:/usr/local/bin
    * COPY
        * Copy files from your working system to inside of your image.
        * *File should be in the same directory with the current Dockerfile*
        * *The destination doesn’t include the file name(just its location!).*
        * (ex.) COPY ./setupGUI.sh ./home/   
          : Copy from “./setupGUI.sh” to “./home/setupGUI.sh”
    * ENTRYPOINT
        * Execute specified script or command once container is initiated(docker run or docker start).
        * Similar with CMD(Slightly different).
        * (ex. with sh) ENTRYPOINT touch /home/test.txt
        * (ex. without sh) ENTRYPOINT [”/home/test.sh”]
        * (ex. without sh with parameter) ENTRYPOINT [”/home/test2.sh”, “--param1=1”, “--param2=2”]
    * VOLUME, ADD, CMD, EXPOSE, ...

### 3. Build the Docker image.
If you have valid Dockerfile, you can build the docker image with docker build command only. Let’s see an example. Assume you are in /home and /home/dockerForEMAN has the Dockerfile(filename is “Dockerfile” literally). Then, you can build the Docker image with one of the following commands.

  ```$ docker build --tag <Image Name> <path for dockerForEMAN directory>```
 
Then, you can see the generating procedure immediately and the generated image with docker images command.
 
### Run the Docker container.
#### Docker Run Options   
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
  --gpus all   
    Enable all GPU devices in the docker container(Nvidia-docker installastion required.)   
    + Installation of nvidia-cuda-toolkit is recommended!
    + Specify the base image with the system-corresponding CUDA image!
      + Ex. `FROM nvidia/cuda:11.4.0-devel-ubuntu20.04` if your system's cuda version is 11.4
  --ipc=host
    If there are some "shared memory" issue, specify this option might helpful.   
    If you need more information, refer [docs.docker.com](https://docs.docker.com/engine/reference/run/#ipc-settings---ipc)
#### Examples   
  ```
  $docker run -it --rm --net=host -e DISPLAY --name gui_test gui_kjy
  $docker run -it --rm --name no_gui gui_kjy
  $docker run -it --rm --name disk_share -v /home/kimv/:/home/exinput eman2_kjy
  $docker run --rm -it --net=host -e DISPLAY --gpus all -v /home/kimv/FROMWINDOW/:/cdata --name all pipe3_dynamo:matlab "$(xauth list | grep vision)"
  ```   
  
### Other things
* You can get out of the current docker container with “$exit”.   
* Detach from the current container : ``` Ctrl + P then Ctrl + Q ```   
  * "Detach and commit" is quite useful.   
  * Attach into the detached container : ``` docker attach "container name"```
  * [***Detach and Attach***](https://stackoverflow.com/questions/19688314/how-do-you-attach-and-detach-from-dockers-process)  
* If you meet the following messages, you can add the `network=host` option into docker build
  ```
    W: Failed to fetch http://archive.ubuntu.com/ubuntu/dists/focal/InRelease  Temporary failure resolving ‘archive.ubuntu.com’
    W: Failed to fetch http://archive.ubuntu.com/ubuntu/dists/focal-updates/InRelease  Temporary failure resolving ‘archive.ubuntu.com’
    W: Failed to fetch http://archive.ubuntu.com/ubuntu/dists/focal-backports/InRelease  Temporary failure resolving ‘archive.ubuntu.com’
    W: Failed to fetch http://security.ubuntu.com/ubuntu/dists/focal-security/InRelease  Temporary failure resolving ‘security.ubuntu.com’
    W: Some index files failed to download. They have been ignored, or old ones used instead.
    ...
    E: Unable to locate package wget
  ```

## Docker GUI(Write based on Mac environment)
### Basic GUI Settings
1. First, you have to make a connection between server and your Mac machine(marked as local below).
    * In your local terminal, you have to install xquartz.
        1. ```$brew install xquartz```
        2. Reboot your local machine.
        3. Use -X option for ssh connection and test your connection.
          (ex.) I tested with the “nautilus”(GUI-based Directory Viewer). If you successfully made a connection, the GUI window would appear after the “nautilus” commands.
    * Although you already connected server and local, GUI connection seems to be disconnected from time to time if you continue to connect to the server(or when you do some specific action). If the GUI connection is disconnected, you can disconnect from the server and re-connect through ssh again.   
        * If your GUI connection is broken, you would see the messages similar to the following.   
      (org.gnome.Nautilus:13): Gtk-WARNING **: 05:32:09.276: cannot open display: localhost:10.0   
    * __[FOR Windows User!!]__ In your local machine, you have to install VcXsrv.
        1. You can install VcXsrv in [***here***](https://sourceforge.net/projects/vcxsrv)
        2. Search about more detailed information. At least, the program's name guide you to the right direction!
2. Second, you have to make a connection between server and your docker container.
    * [server] Run the following command, and copy the output(if output is multiline, choose just one line or delete others to make single line). The output will change when you re-connect to the server. 
      `$ xauth list`
    * [server] Execute docker run command with the following options.
    --net=host -e DISPLAY
    * [docker container] Run the following command.
      `$ xauth add <the copied output>`
    * [docker container] Finished! However, you might see lots of graphics-related error when you execute the GUI-based program. You should solve these error then(Probably with “install something, set some environment variable, etc”).
3. You can automate these steps.   
    a. Write .sh file like this(Let’s assume this file’s name “setupGUI.sh” and share a same location with Dockerfile).
    ```shell  
    #!/bin/bash
    bash 
    xauth add $@
    ```
    b. Write the following lines in Dockerfile.   
    ```shell  
    COPY ./setupGUI.sh /home
    ...
    ENTRYPOINT ["bash", "/home/setupGUI.sh"]
    ```
    c. Then, execute the docker run command with “\$(xauth list)”   
        (ex.) docker run -it --rm --net=host -e DISPLAY --name kjy_gui2 gui_kjy “$(xauth list)”

## For OpenGL activation in X11 forwarding!
### Mac os : Xquartz
You should type the following commands in your local terminal!

```$defaults write org.xquartz.X11 enable_iglx –bool true```

This commands make an effect in the following codes(in /opt/X11/bin/startx)

<img width="528" alt="opt-X11-bin-startx_ default write usage" src="https://user-images.githubusercontent.com/10249736/150919840-49d345f6-e0a6-4e7c-8317-3f83facdb27e.png">

### Windows os(WSL2, Ubuntu 20.04 LTS) : VcXsrv
You should configure VcXsrv as following.   
   1. Unmark Native opengl   
   2. Put "-ac" into "Additional parameters for VcXsrv"   

## Docker with NVIDIA GPU
First, your system is equipped with 
## Docker Images for Cryo-ET
`<NAME>` : name for the container   
$ : in the server.   
\$$ : in the docker container.   
Dockerfiles and More informations are available at https://github.com/KJYoung/DockerFilesForCryoET   
  
### MotionCor2
  ```
    $docker pull jykim157/motioncor2:base
    $docker run --rm -it --name <NAME> jykim157/motioncor2:base
    $$motioncor2 --help
  ```
### Warp
#### base : with pre-compiled version 1.0.0 and [**dynamo2m**](https://github.com/alisterburt/dynamo2m)
  ```
    $docker pull jykim157/warpcli:base
    $docker run --rm -it --net=host -e DISPLAY --name <NAME> jykim157/warpcli:base "$(xauth list)"
    $$warpcli
    $$dynamo2warp
  ```
#### with compiled version 1.0.9 : Currently trying to compile...   
   
### IMOD
  ```
    $docker pull jykim157/imod:base
    $docker run --rm -it --name <NAME> --net=host -e DISPLAY jykim157/imod:base "$(xauth list)"
    $$imodcfg
    $$imod
  ```
### EMAN2
#### with GUI
  ```
    $docker pull jykim157/eman2:base
    $docker run --rm -it --name <NAME> --net=host -e DISPLAY jykim157/eman2:base "$(xauth list)"
    $$e2version.py
    // with GUI : $$e2display.py can be executed.
  ```
#### without GUI
  ```
    $docker run --rm -it --name <NAME> jykim157/eman2:base
    $$e2version.py
  ```
There is many python files can be executed. The following figure shows the procedure to test EMAN2(without GUI, we cannot execute e2display.py).
  
### [Dynamo](https://wiki.dynamo.biozentrum.unibas.ch/w/index.php/Main_Page) + [IMOD](https://bio3d.colorado.edu/imod/doc/guide.html)
#### Extended : [**autoalign_dynamo**](https://github.com/alisterburt/autoalign_dynamo)[Modified for Docker env.]
#### Extended : [**dynamo2m**](https://github.com/alisterburt/dynamo2m)
#### Helpful reference : [Dynamo GPU configuration](https://wiki.dynamo.biozentrum.unibas.ch/w/index.php/GPU#Installation)
  This version is incomplete due to the MATLAB!   
  IMOD is also required for the valid operation of autoalign_dynamo as specified in its github readme's prerequisite.
  ```
    $docker pull jykim157/dynamoimod:base
    $docker run --rm -it --name --net=host -e DISPLAY --gpus all -v <DATA DIRECTORY>:/cdata <NAME> jykim157/dynamoimod:base
    
    $$ cd matlab && ./install (First, you should install the MATLAB with the following 5 toolboxes.)
    $$ ^P and ^Q (Then, ctrl P + Q to pause the current container and execute the following.)
    $docker ps (Then, copy the container's ID.)
    $docker commit <copied ID> <jykim157/dynamoimod:matlabinstall> (you can rename the image surely.)
  ```
   Required toolbox   
      * [**for autolalign_dynamo**] Computer vision toolbox, Curve fitting toolbox, Image processing toolbox, Parallel computing toolbox   
      * [**for execution of autoalign_dynamo**] Statistics and machine learning toolbox
   ########################## After the installation : Ready to use! ##########################
  ```
    $$source /home/dynamoRoot/dynamo_activate_linux_shipped_MCR.sh
    $$ (execute dynamo project exe file! (standalong project))
    OR
    $$matlab
        <For dynamo>
        >> run /home/dynamoRoot/dynamo_activate.m
        >> dcp, dcm, ...
        <For autoalign_dynamo>
        >> run /opt/autoalign_dynamo/autoalign_activate.m
        >> dautoalign4warp, warp2catalogue, ...

    $$imodcfg
    $$imod
  ```
### CTFFIND4
  ```
    $docker pull jykim157/ctffind4:base
    $docker run --rm -it --name <NAME> jykim157/ctffind4:base
    $$ctffind
  ```
### RELION : also GUI available(2022/02/04 Updated).
  ```
    $docker pull jykim157/relion:base
    $docker run --rm -it --name <NAME> jykim157/relion:base
    $$relion_... (There are many scripts to run. ex) relion_prepare_subtomogram)
  ```
   
## Docker images are available also in the Dockerhub!
  * [MotionCor2 hub](https://hub.docker.com/r/jykim157/motioncor2)
  * [Warpcli hub](https://hub.docker.com/r/jykim157/warpcli)
  * [Dynamo IMOD hub](https://hub.docker.com/repository/docker/jykim157/dynamoimod)
  * [EMAN2 hub](https://hub.docker.com/r/jykim157/eman2)
  * [CTFFIND4 hub](https://hub.docker.com/r/jykim157/ctffind4)
  * [RELION hub](https://hub.docker.com/r/jykim157/relion)
  * [Dynamo hub : deprecated](https://hub.docker.com/r/jykim157/dynamo)
  * [IMOD hub : deprecated](https://hub.docker.com/r/jykim157/imod)

## TODO & Doing :   
   * Warp, Dynamo Feature study
