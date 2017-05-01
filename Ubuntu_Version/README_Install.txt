To use this program in Linux with python 2.7.6, perform the following steps:
1.  Install tensorflow with virtualenv to ~/tensorflow, detailed instructions at
    https://www.tensorflow.org/install/install_linux

2.  Each time you enter a new console, initiate tensorflow using one of the following commands:
$ source ~/tensorflow/bin/activate      # if you use bash, sh, ksh, or zsh
$ source ~/tensorflow/bin/activate.csh  # if you use csh or tcsh

you can end the tensorflow session by entering:
$ deactivate

3.  Install any required packages:
$ sudo pip install easygui, pygame, pick, subprocess

4.  You should now be able to run the program.  Running for the first time may take a while, and
there may be a long delay and/or unusual output the first time you take a picture.

Navigate to the Ubuntu_Version directory, and enter the command:
$ python run.py
You will be given the option to pick from available cameras, the first one generally works.
A window with a live feed from the camera should pop up.
When you have an item you want to identify in the camera's view, press enter or right-click in the window.
The video feed will pause while the model attempts to classify the object among the 1000 classes in the imagenet dataset.
The top 5 guesses for the item are displayed in a popup window.
When you click "okay" the video feed will resume, and you may press enter to try another object.
Press escape with the video feed window selected to end the program.
