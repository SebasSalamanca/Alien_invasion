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
    """Load the files and create methods to play them"""
    def __init__(self): 
        
        pygame.mixer.init()
        pygame.mixer.music.load(get_reurce_path("sounds/spaceinvaders1.wav"))
        self.shoot = pygame.mixer.Sound(get_reurce_path("sounds/shoot.wav"))
        self.kill_alien = pygame.mixer.Sound(get_reurce_path("sounds/invaderkilled.wav"))
        self.explosion  = pygame.mixer.Sound(get_reurce_path("sounds/explosion.wav"))   
        
        

    def play_back_sound(self):
        #Main song play loop until the game ends
        pygame.mixer.music.play(-1)

    def stop_back_sound(self):
        #Stop main song
        pygame.mixer.music.stop()
    
    def play_shoot(self):
        #reproduce shoot sound
        self.shoot.set_volume(0.1)
        self.shoot.play()
        
    def play_kill_alien(self):
        #reproduce kill alien sound 
        self.kill_alien.set_volume(0.1)
        self.kill_alien.play()

    def play_explosion(self):
        #reproduce ship_hit sound 
        self.explosion.play()

        