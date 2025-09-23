import pygame

class SoundEffect():
    
    def __init__(self): 

        pygame.mixer.init()
        pygame.mixer.music.load("sounds/spaceinvaders1.mpeg") 
        self.shoot = pygame.mixer.Sound("sounds/shoot.wav")
        self.kill_alien = pygame.mixer.Sound("sounds/invaderkilled.wav")
        self.explosion  = pygame.mixer.Sound("sounds/explosion.wav")
        
        

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
        self.explosion.set_volume(0.1)
        self.explosion.play()

        