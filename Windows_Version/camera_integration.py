# sudo pip install pygame
# sudo pip install pick

import pygame
import sys
import pygame.camera
from pygame.locals import *
from pick import pick
from time import sleep
import subprocess
import numpy as np
import cv2

#list the available cameras for picking
#pygame.init()
#pygame.camera.init()

# camlist = pygame.camera.list_cameras()
# print "found cameras: " + str(camlist)
# if len(camlist) <= 0:
#	 print "No cameras found!  Exiting...\n"
#	 exit
# title = "Please choose a camera"
# options = camlist
# cam, index = pick(options, title)
# print "you chose " + cam
#
# cam = pygame.camera.Camera(cam,(640,480))
# cam.start()
# image = cam.get_image()

class Capture(object):
	def __init__(self):
		print("enter the number of the camera you would like to use, e.g. 0")
		self.cam = int(input("number: "))
		self.cap = cv2.VideoCapture(self.cam)

		#self.cam.start()

		# create a display surface. standard pygame stuff
		#self.display = pygame.display.set_mode(self.size, 0)
		#self.saved_display = pygame.display.set_mode(self.size, 0)
		# create a surface to capture to.  for performance purposes
		# bit depth is the same as that of the display surface.
		#self.snapshot = pygame.surface.Surface(self.size, 0, self.display)
		#self.saved_image = pygame.surface.Surface(self.size, 0, self.display)

	def get_and_flip(self):
		# if you don't want to tie the framerate to the camera, you can check
		# if the camera has an image ready.  note that while this works
		# on most cameras, some will never return true.
		ret, self.frame = self.cap.read()
		#gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
		cv2.imshow('frame',self.frame)

	def save_and_id_image(self):
		self.saved_image = self.frame.copy()
		cv2.imwrite('test.jpeg',self.saved_image)
		subprocess.call('python identify.py', shell=True)

	def runCam(self):
		print ("press Enter to take a picture for identification, Esc to exit")
		going = True
		while going:
			self.get_and_flip()
			k = cv2.waitKey(1)
			#exit on q or esc
			if k == 27:
				break
			#identify on enter or right-click
			elif k == 13:
				self.save_and_id_image()
			#otherwise print what you clicked
			elif k != 255:
				print(k)
			sleep(0.02)
		self.cap.release()
		cv2.destroyAllWindows()
		return