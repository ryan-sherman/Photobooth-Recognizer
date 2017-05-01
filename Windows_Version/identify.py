from easygui import msgbox
import os
import subprocess


def Mbox(title, text):
    msgbox(text, title)

str = subprocess.check_output('python classify_image.py --image_file "test.jpeg"', shell=True)

Mbox("Indentifier", "MY best guesses are:\n "+ str.decode('utf-8'))
os._exit(0)