import pygame

WHITE = (255, 255, 255)
ORANGE = (255, 153, 0)
BLACK = (0, 0, 0)
RED = (255, 0, 0)
BLUE = (0, 0, 255)
orange=(255,153,0)
black = (0,0,0)
red = (255,25,25)

character1 = pygame.image.load('swatshootingcycle1.png')
character1= pygame.transform.scale(character1,(70,75))
character1.set_colorkey(WHITE)
character2 = pygame.image.load('swatswalkingcycle2.png')
character2= pygame.transform.scale(character2,(70,75))
character2.set_colorkey(WHITE)
shotsFired = pygame.image.load('swatshootingcycle2.png')
shotsFired = pygame.transform.scale(shotsFired,(70,75))
shotsFired.set_alpha()
shotsFired.set_colorkey(WHITE)
ShootingSprite =[character1,shotsFired]


#background = pygame.image.load('action cycle 3.jpg')
#background= pygame.transform.scale(background,(50,55))
Realbackground = pygame.image.load('Mbackground.png')
Realbackground= pygame.transform.scale(Realbackground,(1250,800))
characterAnimationL = [character1,character2]
Startscreen = pygame.image.load("ChocoBible.png")
Startscreen = pygame.transform.scale(Startscreen,(1250,800))
Startscreen2 = pygame.image.load("ChocoPages.png")
Startscreen2 = pygame.transform.scale(Startscreen2, (1250 ,800))
CopyRight = pygame.image.load("ChocoCopyright.png")
CopyRight = pygame.transform.scale(CopyRight,(1250 ,(800)))



enemyF= pygame.image.load('dinoVillan1.png')
enemyF= pygame.transform.scale(enemyF,(60,50))
enemyF.set_colorkey(WHITE)
enemyF.set_alpha()
enemy2 = pygame.image.load('dinoVillan2.png')
enemy2= pygame.transform.scale(enemy2,(60,50))
enemy2.set_colorkey(WHITE)
enemy2.set_alpha()
bullet=pygame.Surface((10,4))
pygame.draw.rect(bullet,black,(0, 0, 10, 4))
        