# sudo pip install pygame
# sudo pip install pick
#

import pygame
import pygame.camera
from pygame.locals import *
from pick import pick
from time import sleep
import subprocess

#list the available cameras for picking
#pygame.init()
#pygame.camera.init()

# camlist = pygame.camera.list_cameras()
# print "found cameras: " + str(camlist)
# if len(camlist) <= 0:
#     print "No cameras found!  Exiting...\n"
#     exit
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
        pygame.init()
        pygame.camera.init()
        self.size = (640,480)
        self.clist = pygame.camera.list_cameras()
        if not self.clist:
            raise ValueError("Sorry, no cameras detected.  Exiting...")
            exit(0)
        title = "Please choose a camera"
        options = self.clist
        camName, index = pick(options, title)
        print "you chose " + camName
        self.cam = pygame.camera.Camera(camName, self.size)

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
        if self.cam.query_image():
            self.snapshot = self.cam.get_image(self.snapshot)

        # blit it to the display surface.
        self.display.blit(self.snapshot, (0,0))
        pygame.display.flip()

    def save_and_id_image(self):
        self.saved_image = self.snapshot.copy()
        pygame.image.save(self.saved_image, 'test.jpeg')
        subprocess.call('python identify.py', shell=True)

    def runCam(self):
        self.cam.start()
        self.display = pygame.display.set_mode(self.size, 0)
        self.snapshot = pygame.surface.Surface(self.size, 0, self.display)
        self.saved_image = pygame.surface.Surface(self.size, 0, self.display)
        print "press Enter to take a picture for identification, Esc to exit"
        going = True
        while going:
            events = pygame.event.get()
            for e in events:
                if e.type == pygame.QUIT or (e.type == pygame.KEYDOWN and e.key == pygame.K_ESCAPE):
                    # close the camera safely
                    self.cam.stop()
                    going = False
                if (e.type==pygame.KEYDOWN and e.key==pygame.K_RETURN) or (e.type==pygame.MOUSEBUTTONDOWN and e.button == 3):
                    self.save_and_id_image()
                    sleep(.04)

            self.get_and_flip()
            sleep(0.02)

        return