To use this program in Windows with python 3.5, perform the following steps:
1.  Install tensorflow with Anaconda to ~/tensorflow, detailed instructions at
	https://www.tensorflow.org/install/install_windows
	be sure that when you create the Anaconda environment you specify the python
	version that is currently compatible with Tensorflow.  The exact command as is:
	> conda create -n tensorflow python=3.5

2.  Each time you start a new console/cmd window, initiate the tensorflow virtual environment
using the command:
activate tensorflow

3.  Install any required packages:
pip install easygui
pip install pygame
pip install pick
pip install subprocess

if you have a 32 bit operating system:
pip install curses-2.2-cp35-none-win32.whl
pip install pygame-1.9.3-cp35-cp35m-wi32.whl
pip install opencv_python‑3.2.0‑cp35‑cp35m‑win32.whl

if you have a 64 bit operating system (this is typical nowadays)
pip install curses-2.2-cp35-none-win_amd64.whl
pip install pygame-1.9.3-cp35-cp35m-win_amd64.whl
pip install opencv_python‑3.2.0‑cp35‑cp35m‑win_amd64.whl

4.  You should now be able to run the program.  Running for the first time may take a while, and
there may be a long delay and/or unusual output the first time you take a picture.
The "frame" window may say "not responding" this does not indicate failure.
If it takes well over a minute, abort with Ctrl+c in the console.

Navigate to the Ubuntu_Version directory, and enter the command:
$ python run.py
You will be given the option to pick a camera to use.  0 usually contains the built in camera, if it is not the camera you want, try 1.
A window with a live feed from the camera should pop up.
When you have an item you want to identify in the camera's view, press enter with the window selected.
The video feed will pause while the model attempts to classify the object among the 1000 classes in the imagenet dataset.
The top 5 guesses for the item are displayed in a popup window.
When you click "okay" the video feed will resume, and you may press enter to try another object.
Press escape with the video feed window selected to end the program.
