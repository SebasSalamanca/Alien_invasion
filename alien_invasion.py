import sys
from time import sleep
import pygame
from random import randint
from settings import Settings
from game_stats import GameStats
from ship import Ship
from bullet import Bullet
from alien import Alien
from raindrop import Monster


class AlienInvasion:
    """Overall class to manage game assets and behavior"""

    def __init__(self):
        """Initialize the game, and create game resources"""
        pygame.init()
        self.clock = pygame.time.Clock()
        self.settings = Settings()
        self.screen = pygame.display.set_mode((self.settings.screen_width, self.settings.screen_height))
        print(type(self.screen))
        pygame.display.set_caption("Alien_Invasion")

        #Create an instance to store game statistics 
        self.stats = GameStats(self)

        self.ship = Ship(self)
        self.bullets = pygame.sprite.Group()
        self.aliens = pygame.sprite.Group()
        self.monsters = pygame.sprite.Group()

        self._create_fleet()
        

    def _create_fleet(self):
        """Create the fleet of aliens"""
        #Create an alien and keep adding aliens until there's no room left.
        #Spacing between aliens is one alien width and one alien height
        alien = Alien(self)
        alien_width, alien_height = alien.rect.size

        current_x, current_y = alien_width, alien_height

        while current_y < (self.settings.screen_height - 3*alien_height):        
            while current_x < (self.settings.screen_width - 2*alien_width):
                self._create_alien(current_x, current_y)
                current_x += 2 * alien_width    
            #Finished a row: reset x value and increment y value
            current_x = alien_width
            current_y += 1.5*alien_height

    def _create_alien(self, x_position, y_position):
        """Create an alien and place it in the row."""
        new_alien = Alien(self)
        new_alien.x = x_position #Question!!!!
        new_alien.rect.x = x_position
        new_alien.rect.y = y_position
        self.aliens.add(new_alien)

    def _create_fleet_monsters(self):
        number_of_monsters = randint(4, 6)
        for monster_index in range(number_of_monsters):
            new_monster = Monster(self)
            new_monster.set_random_position(monster_index)
            self.monsters.add(new_monster)
        
        
    

    def _check_fleet_edges(self):
        """Respond appropriately if any aliens have reached an edge"""
        for alien in self.aliens.sprites():
            if alien.check_edges():
                self._change_fleet_direction()
                break
    
    def _change_fleet_direction(self):
        """Drop the entire fleet and change the fleet's direction"""
        for alien in self.aliens.sprites():
            alien.rect.y += self.settings.fleet_drop_speed
        self.settings.fleet_direction *= -1


    def _update_aliens(self):
        #Update the position of all aliens in the fleet
        self._check_fleet_edges()
        self.aliens.update() #We use the update() method on the alien group, which calls each alien's update() method.
        """Check if the fleet is at an edge, the update the position"""
        #Look for alien-ship collisions.
        if pygame.sprite.spritecollideany(self.ship, self.aliens):
            print("Ship Hit by alien!")
            self._ship_hit()
        #Lookf for aliens hitting the bottom of the screen 
        self._check_aliens_bottom()

    def _check_aliens_bottom(self):
        #Check if any aliens have reached the bottom of the screen.
        for alien in self.aliens.sprites():
            if alien.rect.bottom >= self.settings.screen_height:
                #Teat this the same as if the ship got hit. 
                self._ship_hit()
                break



    def _create_new_fleet_monsters(self):
        if len(self.monsters) == 0:
            self._create_fleet_monsters()
    
    def _update_monsters(self):
        """Drip the monsters on the screen"""
        self.monsters.update()
        if pygame.sprite.spritecollideany(self.ship, self.monsters):
            print('Ship Hit by monster')
            self._ship_hit()
        for monster in self.monsters.copy():
            if monster.rect.top >= self.settings.screen_height:
                self.monsters.remove(monster)

    


    def run_game(self):
        """Start the main loop for the game"""
        while True:
            self._check_events()            
            self.ship.update()
            self._update_bullets() 
            self._update_aliens()  
            self._create_new_fleet_monsters()
            self._update_monsters() 
            self._update_screen()
            self.clock.tick(60)
    

    def _update_bullets(self):
        """Update position of bullets and get rid of old bullets."""
        #update bullet position
        self.bullets.update()
        #Get rid of bullets that have dissapeared
        for bullet in self.bullets.copy():
            if bullet.rect.bottom <= 0:
                self.bullets.remove(bullet)
        #Check for any bullets that have hit aliens
        #If so, get rid of the bullet and the alien 
        self._check_bullet_alien_collisions()

    def _check_bullet_alien_collisions(self):
        collisions = pygame.sprite.groupcollide(self.bullets, self.aliens,True, True)
        if not self.aliens:
            #Destry existing bullets and create new fleet
            self.bullets.empty()
            self._create_fleet()
        
        
    def _ship_hit(self):
        #Respond to the ship being hit by the alien.
        #Decrement ships_left 
        self.stats.ships_left -= 1

        #Get rid of any remaining bullets and aliens. 
        self.bullets.empty()
        self.aliens.empty()
        self.monsters.empty()

        
        
        #create a new fleet and center the ship.
        self._create_fleet()
        self._create_fleet_monsters()
        self.ship.center_ship()

        #Pause 
        sleep(1)




    def _check_events(self):
        """Respond to key mouse and keyevents"""
        #Whatch for keyboard and mouse events
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
            elif event.type == pygame.KEYDOWN:
                self._check_keydown_events(event)

            elif event.type == pygame.KEYUP:
                self._check_keyup_events(event)  

    def _check_keydown_events(self, event):
        if event.key == pygame.K_RIGHT:
            self.ship.moving_right = True
        elif event.key == pygame.K_LEFT:
            self.ship.moving_left = True
        elif event.key == pygame.K_q:
            sys.exit()
        elif event.key == pygame.K_SPACE:
            self._fire_bullet()

        

        

    def _check_keyup_events(self, event):
        if event.key == pygame.K_RIGHT:
            self.ship.moving_right = False
        elif event.key == pygame.K_LEFT:
            self.ship.moving_left = False
    


    def _fire_bullet(self):
        """Create a new bullet and add it to the bullets group"""
        if len(self.bullets) < self.settings.bullets_allowed: 
            new_bullet = Bullet(self)
            self.bullets.add(new_bullet)



    def _update_screen(self):
        #Redraw the screen during each pass through the loop.
        self.screen.fill(self.settings.bg_color)   
        for bullet in self.bullets.sprites():
            bullet.draw_bullet()
        self.ship.blitme()
        self.aliens.draw(self.screen)
        self.monsters.draw(self.screen)


        #Make the most recently drawn secreen visible
        pygame.display.flip()


if __name__ == '__main__':
    #Make a game instance and run the game
    ai = AlienInvasion()
    ai.run_game()