import pygame 

pygame.init()
pygame.mixer_music.load('MC_POZE_NOS_ANOS_80.mp3')
pygame.mixer.music.play()


while pygame.mixer.music.get_busy():
    continue

pygame.mixer_music.pause
pygame.quit()