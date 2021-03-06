import pygame
import GraphicsLib as GLib
from Util import *
import random
SECSPERPOINT=18

EnemyPositionList=[50,100,150,200,250,300,350,400,450,500,550,600]
# a great example of an object that can move on the screen
class damagetaken:
    def __init__(self):
        self.update(0)
        self.x = 300
        self.y = 350
    def update(self, damagetext):
        myfont=pygame.font.SysFont('Calibri',70,bold=True)
        self.img=myfont.render(str(damagetext),1,GLib.RED)
        
class Score:
    def __init__(self):
        self.update(0)
        self.x = 1095
        self.y = 5
        
    def update(self,scoreNum):
        myfont=pygame.font.SysFont('Calibri',40,bold=True)
        self.img=myfont.render(str(scoreNum),1,GLib.RED)
        
class Ammo:
    def __init__(self):
        self.update(20)
        self.x=10
        self.y=5
        
    def update(self,bulletNum):
        myfont=pygame.font.SysFont('Calibri',20,bold=True)
        self.img=myfont.render("Ammo:"+str(bulletNum),1,GLib.BLACK)
#original basic boy
class enemy1():
    def __init__(self):
        self.enemyAnim = [GLib.enemyF,GLib.enemy2]
        self.img = GLib.enemyF
        self.x = 1225
        self.vx = -8
        self.y=EnemyPositionList[random.randint(0,len(EnemyPositionList)-1)]
        self.t =0
    def update(self):
        self.x += self.vx
        self.img = self.enemyAnim[(self.t // 2 )% 2] 
        self.t = self.t + 1
# big boy
class enemyW():
    def __init__(self):
        self.enemyAnimA = [GLib.enemy3, GLib.enemy32]
        self.img = GLib.enemy3
        self.x = 1225
        self.vx= -1
        self.y =EnemyPositionList[random.randint(0,len(EnemyPositionList)-1)]
        self.t=0
    def update(self):
        self.x += self.vx      
        self.img = self.enemyAnimA[(self.t // 2)% 2]
        self.t = self.t + 1        
# drag boy  
class enemyQ(): 
    def __init__(self):
        self.enemyAnimaT = [GLib.enemy4, GLib.enemy42]
        self.img = GLib.enemy4
        self.x = 1225
        self.vx = -10
        self.y = EnemyPositionList[random.randint(0,len(EnemyPositionList)-1)]
        self.t = 0
    def update(self):
        self.x += self.vx
        self.img = self.enemyAnimaT[(self.t // 2)% 2]
        self.t = self.t + 1

class enemyK():
    def __init__(self):
        self.enemyAnim = [GLib.enemy5,GLib.enemy52]
        self.img = GLib.enemy5
        self.x = 1225
        self.vx = -6
        self.vy = 3
        self.y=EnemyPositionList[random.randint(0,len(EnemyPositionList)-1)]
        self.t =0
    def update(self):
        self.x += self.vx
        self.y += self.vy
        self.img = self.enemyAnim[(self.t // 2 )% 2] 
        self.t = self.t + 1
        bounceIn(self,-100,50,1300,650)
        
        
class enemyT():
    def __init__(self):
        self.enemyAnim = [GLib.enemy6,GLib.enemy62]
        self.img = GLib.enemy6
        self.x = 1225
        self.vx = -10
        self.y=EnemyPositionList[random.randint(0,len(EnemyPositionList)-1)]
        self.t =0  
    def update(self):
        self.x += self.vx
        self.img = self.enemyAnim[(self.t // 2 )% 2] 
        self.t = self.t + 1
#wtf another original basic boy??

class Bullet:
# self.sprite.x , self.sprite.y
    def __init__(self, x, y): 
        self.x=x-3
        self.y=y+19
        self.img=GLib.bullet
        
    def update(self):
        self.x += 35
        
class Sprite:
    def __init__(self):
        # ------------------------
        # [REQUIRED PART] for any class that will be drawn on the screen
        # Grab the surface that Graphics people worked very hard on
        self.img = GLib.character1
        # Set the initial coordinate of this object
        self.x = 100
        self.y = 50
        self.pastx = self.x
        self.pasty = self.y
        # ------------------------
        # TODO: add more properties to Sprite based on your game
        self.vx = 0
        self.vy = 0
        self.lives=10
        self.bullets=20
    

    # an example of updating position of the object
    def update(self):
        # TODO: what else Sprite is going to do in each frame
        bounceIn(self, 0, 0, 1225, 700)
        
    def MovementDetection(self):
        CharacterAnimationL = [GLib.character1]
        if self.x != self.pastx or self.y != self.pasty:
            CharacterAnimationL= GLib.characterAnimationL
        self.pastx = self.x
        self.pasty = self.y
        return CharacterAnimationL
                    

# the minimum class for an object that can be displaced on the screen



class Game:
    def __init__(self):
        # initialize the timer to zero. This is like a little clock
        self.timer = 0
        self.reloadTimer=0
        self.damageTimer=0
        self.sprite = Sprite()
        self.enemyList = []
        self.enemy2List = []
        self.enemy3List = []
        self.enemy4List = []
        self.enemy5List = []
        self.bulletList=[]
        self.score = Score()
        self.ammo=Ammo()
        self.damagetext = damagetaken()
        self.LastBulletShot=0
        self.Lives=10
        self.EWlives=3
        self.EQlives=2
        
        # self.ball = Ball(250, 250, GLib.ballSpriteBLUE)
        # TODO: add any variables you think will be needed as a property of Game
        # ...
        # ..
        # .
        # TODO: add any objects that you would like to be drawn on the screen
        # Make sure that all of those objects has x, y and img defined as their property
        #self.objectsOnScreen = [self.enemyList, self.bulletList, self.score, self.ammo, self.sprite]

        #self.objectsOnScreen = [self.enemyList, self.bulletList, self.score, self.ammo, self.sprite]
        self.objectsOnScreen = []


    def shoot(self):
        if self.reloadTimer < self.timer:
            if self.timer-self.LastBulletShot>10 and self.sprite.bullets>0:
                self.bulletList.append(Bullet(self.sprite.x , self.sprite.y ))
                self.LastBulletShot=self.timer
                self.sprite.bullets-=1


    # Try to update all the elements
    # if you want to add another to the screen:                 self.objectsOnScreen.add(x)
    # if you want to remove a object from the screen:           self.objectsOnScreen.remove(x)
    # if you want to switch to another the state                return 10                      --> this switches to state 10
    # if you want to bring a object to the front                
        # just remove it first and then added it back
        # the last added object is going to be on the top
    def updateInState(self, state):
        # increment the timer
        
        # check what state the game is at
        if state == "Normal" or state == "Attack":
            self.timer += 1
            if self.timer > 0 and self.timer < 500:    
                if self.timer % 80 == 0:
                    e=enemy1()
                    self.enemyList.append(e)
            if self.timer > 499 and self.timer < 1000:
                if self.timer % 80 == 0:
                    e=enemy1()
                    self.enemyList.append(e)
                if self.timer % 80 == 0:
                    e=enemy1()
                    self.enemyList.append(e)
            if self.timer > 999 and self.timer < 1500:
                if self.timer % 80 == 0:
                    e=enemy1()
                    self.enemyList.append(e)
                if self.timer % 80 == 0:
                    e=enemyQ()
                    self.enemy3List.append(e)
            if self.timer > 1499 and self.timer < 2000:
                if self.timer % 80 == 0:
                    e=enemy1()
                    self.enemyList.append(e)
                if self.timer % 80 == 0:
                    e=enemyQ()
                    self.enemy3List.append(e)
                if self.timer % 80 == 0:
                    e=enemyW()
                    self.enemy2List.append(e)
            if self.timer > 1999 and self.timer < 2500:
                if self.timer % 80 == 0:
                    e=enemy1()
                    self.enemyList.append(e)
                if self.timer % 80 == 0:
                    e=enemyK()
                    self.enemy5List.append(e)
            if self.timer > 2499 and self.timer < 3000:
                if self.timer % 110 == 0:
                    e=enemy1()
                    self.enemyList.append(e)
                if self.timer % 110 == 0:
                    e=enemy1()
                    self.enemyList.append(e)
                if self.timer % 110 == 0:
                    e=enemyW()
                    self.enemy2List.append(e)
                if self.timer % 110 == 0:
                    e=enemyQ()
                    self.enemy3List.append(e)
            if self.timer > 2999:
                if self.timer % 150 == 0:
                    e=enemy1()
                    self.enemyList.append(e)
                if self.timer % 150 == 0:
                    e=enemyW()
                    self.enemy2List.append(e)
                if self.timer % 150 == 0:
                    e=enemyW()
                    self.enemy2List.append(e)                    
                if self.timer % 150 == 0:
                    e=enemyQ()
                    self.enemy3List.append(e)
                if self.timer % 150 == 0:
                    e=enemyK()
                    self.enemy5List.append(e)
                    
            for e in self.enemyList: 
                e.update()
                if e.x<=-50:
                    if e in self.enemy2List:
                        self.enemy2List.remove(e)
                    if e in self.enemy3List:
                        self.enemy3List.remove(e)
                    self.enemyList.remove(e)
                    self.Lives -= 1
                    self.damageTimer=self.timer+10
            
            if self.damageTimer > self.timer:
                self.damagetext.update("Damage Taken!")
            else:
                self.damagetext.update(" ")

            for e in self.enemy2List:
                e.update()
                if e.x<=-50:
                    if e in self.enemyList:
                        self.enemyList.remove(e)
                    if e in self.enemy3List:
                        self.enemy3List.remove(e)
                    self.enemy2List.remove(e)
                    self.Lives-=5
                    self.damageTimer=self.timer+10
            if self.damageTimer > self.timer:
                self.damagetext.update("Damage Taken!")
            else:
                self.damagetext.update(" ")

            for e in self.enemy3List:
                e.update()
                if e.x<=-50:
                    if e in self.enemyList:
                        self.enemyList.remove(e)
                    if e in self.enemy2List:
                        self.enemy2List.remove(e)
                    self.enemy3List.remove(e)
                    self.Lives-=1
                    self.damageTimer=self.timer+10
            if self.damageTimer > self.timer:
                self.damagetext.update("Damage Taken!")
            else:
                self.damagetext.update(" ")
            
            for e in self.enemy5List:
                e.update()
                if e.x<=-50:
                    self.Lives-=1
                    self.enemy5List.remove(e)
                    self.damageTimer=self.timer+10
            if self.damageTimer > self.timer:
                self.damagetext.update("Damage Taken!")
            else:
                self.damagetext.update(" ")
                    
            for i in self.bulletList:
                i.update()
                if i.x>=1200:
                    if i in self.bulletList:
                        self.bulletList.remove(i)
            self.score.update(self.timer//SECSPERPOINT)
            self.ammo.update(self.sprite.bullets)
            if self.reloadTimer==self.timer:
                self.sprite.bullets=20
            for i in self.bulletList:
                for e in self.enemyList:
                    if hasCollideRect(i, e):
                        if i in self.bulletList:
                            self.bulletList.remove(i)
                        if e in self.enemyList:
                            self.enemyList.remove(e)
                        break
                for e in self.enemy2List:
                    if hasCollideRect(i, e):
                        if i in self.bulletList:
                            self.bulletList.remove(i)
                        self.EWlives-=1
                    if self.EWlives==0:
                        if e in self.enemy2List:
                            self.enemy2List.remove(e)
                        self.EWlives=3
                        break
                for e in self.enemy3List:
                    if hasCollideRect(i, e):
                        if i in self.bulletList:
                            self.bulletList.remove(i)
                        self.EQlives-=1
                    if self.EQlives==0:
                        if e in self.enemy3List:
                            self.enemy3List.remove(e)
                        self.EQlives=2
                        break
                for e in self.enemy5List:
                    if hasCollideRect(i, e):
                        if i in self.bulletList:
                            self.bulletList.remove(i)
                        if e in self.enemy5List:    
                            self.enemy5List.remove(e)
                        break
                        
            for e in self.enemyList:
                if hasCollideRect(self.sprite, e):
                    if e in self.enemyList:
                        self.enemyList.remove(e)
                    self.Lives -= 1
                    self.damageTimer=self.timer+10
            if self.damageTimer > self.timer:
                self.damagetext.update("Damage Taken!")
            else:
                self.damagetext.update(" ")

            for e in self.enemy2List:
                if hasCollideRect(self.sprite, e):
                    if e in self.enemy2List:
                        self.enemy2List.remove(e)
                    self.Lives -= 5
                    self.damageTimer=self.timer+10
            if self.damageTimer > self.timer:
                self.damagetext.update("Damage Taken!")
            else:
                self.damagetext.update(" ")

            for e in self.enemy3List:
                if hasCollideRect(self.sprite, e):
                    if e in self.enemy3List:    
                        self.enemy3List.remove(e)
                    self.Lives -= 1
                    self.damageTimer=self.timer+10
            if self.damageTimer > self.timer:
                self.damagetext.update("Damage Taken!")
            else:
                self.damagetext.update(" ")

            for e in self.enemy5List:
                if hasCollideRect(self.sprite, e):
                    if e in self.enemy5List:    
                        self.enemy5List.remove(e)
                    self.Lives -= 1
                    self.damageTimer=self.timer+10
            if self.damageTimer > self.timer:
                self.damagetext.update("Damage Taken!")
            else:
                self.damagetext.update(" ")
                                

            if self.Lives < 1:
                self.objectsOnScreen =[]
            
                return "Died"
            if state == "Normal":
                showAnimationOn(self.sprite, self.sprite.MovementDetection(), self.timer )
            else:
                showAnimationOn(self.sprite, GLib.ShootingSprite, self.timer/2)
            self.sprite.update()
        elif state == "Startscreen2":
            pass
        elif state == "Startscreen3":
            pass
        elif state == "Startscreen4":
            pass
        elif state == "Startscreen":
            pass
        elif state == "ControlScreen":
            pass
        elif state == "Died":
            pass
        else:
            print("Undefined game state " + str(state))
            exit()
        # return the same state if you decided not to switch a state
        return state

    





    # A method that does all the drawing for you.
    def draw(self,state, screen):
        # The first line clear the screen
        # TODO: if you want a differnt background, 
            # you can replace the next line                     
        if state == "Normal":
            screen.blit(GLib.Realbackground, (-25, -15))
            screen.blit(GLib.Lives,(96.5,1))
            myfont=pygame.font.SysFont('Calibri',20,bold=True)
            img=myfont.render(str(self.Lives),1,GLib.WHITE)
            screen.blit(img,(110,10))
        elif state == "Startscreen2":
            screen.blit(GLib.Startscreen2,(0,0))
        elif state == "Startscreen3":
            screen.blit(GLib.Startscreen3,(0,0))
        elif state == "Startscreen4":
            screen.blit(GLib.Startscreen4,(0,0))
        elif state == "Startscreen":
            screen.blit(GLib.Startscreen,(0,0))
        elif state == "ControlScreen":
            screen.blit(GLib.ControlScreen,(0,0))
        if state == "Attack":
            screen.blit(GLib.Realbackground,(-25,-15))
        if state == "Died":
            screen.blit(GLib.GameoverS,(0,0))
            


        for obj in self.objectsOnScreen:
            if type(obj) is list:
                for i in obj:
                    screen.blit(i.img, (i.x, i.y))
            else:
                screen.blit(obj.img, (obj.x, obj.y))
        if state == "StartScreen":
            screen.blit(GLib.Startscreen,(0,0))