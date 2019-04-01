import pygame
pygame.mixer.init()
pygame.mixer.music.load("alarm.wav")
pygame.mixer.music.play()
#dette er en test
while (pygame.mixer.music.get_busy()==True):
    continue
