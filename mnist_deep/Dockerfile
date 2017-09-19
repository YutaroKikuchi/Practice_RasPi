FROM ubuntu:16.04

RUN apt-get update
RUN apt-get install -y \
    build-essential \
    bzip2 \
    cmake \
    curl \
    git \
    libboost-all-dev \
    libbz2-dev \
    libfluidsynth-dev \
    libfreetype6-dev \
    libgme-dev \
    libgtk2.0-dev \
    libjpeg-dev \
    libopenal-dev \
    libpng12-dev \
    libsdl2-dev \
    libwildmidi-dev \
    libzmq3-dev \
    nano \
    nasm \
    pkg-config \
    rsync \
    software-properties-common \
    sudo \
    tar \
    timidity \
    unzip \
    wget \
    zlib1g-dev

# Python3
RUN apt-get install -y python3-dev python3 python3-pip
RUN pip3 install pip --upgrade


RUN pip3 install tensorflow
RUN pip3 install matplotlib scipy scikit-image tqdm numpy

WORKDIR "/home/workplace"

RUN mkdir /home/workplace/mnist_deep
RUN mkdir /home/workplace/mnist_deep/MNIST

COPY mnist_deep.py /home/workplace/mnist_deep
COPY input_data.py /home/workplace/mnist_deep
COPY MNIST /home/workplace/mnist_deep/MNIST
CMD /bin/bash
