import pygame
import time
pygame.mixer.init()
pygame.mixer.music.load("alarm.wav")
pygame.mixer.music.play()
time.sleep(3)
pygame.mixer.music.stop()
'''
if (pygame.mixer.music.get_busy()==True):
    time.sleep(3)
  ''' 

