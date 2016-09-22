#!/bin/bash

sudo add-apt-repository ppa:thopiekar/pygame
sudo apt-get update
sudo apt-get install python3-pygame

# ... otherwise, uncomment the following lines:
# sudo apt-get install mercurial python3-pip python3-dev python3-numpy libav-tools libsdl-image1.2-dev libsdl-mixer1.2-dev libsdl-ttf2.0-dev libsmpeg-dev libsdl1.2-dev  libportmidi-dev libswscale-dev libavformat-dev libavcodec-dev libfreetype6-dev
# sudo pip3 install hg+http://bitbucket.org/pygame/pygame
