import pygame
import sys
import os


def get_reurce_path(relative_path):
    """Get aboslute path to resource, works for dev and for PyInstaller"""
    try:
        #Pyinstaller creates a temp folder and stores path in MEIPASS
        base_path = sys._MEIPASS
    except Exception:
        base_path = os.path.abspath(".")
    
    return os.path.join(base_path, relative_path)


class SoundEffect():
    
    def __init__(self): 

        pygame.mixer.init()
        pygame.mixer.music.load(get_reurce_path("sounds/spaceinvaders1.wav"))
        self.shoot = pygame.mixer.Sound(get_reurce_path("sounds/shoot.wav"))
        self.kill_alien = pygame.mixer.Sound(get_reurce_path("sounds/invaderkilled.wav"))
        self.explosion  = pygame.mixer.Sound(get_reurce_path("sounds/explosion.wav"))   
        
        

    def play_back_sound(self):
        pygame.mixer.music.play(-1)

    def stop_back_sound(self):
        pygame.mixer.music.stop()
    
    def play_shoot(self):
        self.shoot.set_volume(0.1)
        self.shoot.play()
        
    def play_kill_alien(self):
        self.kill_alien.set_volume(0.1)
        self.kill_alien.play()

    def play_explosion(self):
        self.explosion.play()

        