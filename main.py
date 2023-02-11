
import pygame
from sys import exit
import math as ma


class Sirkel(pygame.sprite.Sprite):

    def __init__(self,mouse,radius):
        pygame.sprite.Sprite.__init__(self)
        self.surf = pygame.Surface((2*radius,2*radius),pygame.SRCALPHA,32)
        self.surf = self.surf.convert_alpha()
        self.rect = self.surf.get_rect()
        self.rect.center = (mouse[0],mouse[1])
        pygame.draw.circle(self.surf,"White",(radius,radius),radius,5)

class And(pygame.sprite.Sprite):
    def __init__(self,theta):
        pygame.sprite.Sprite.__init__(self)
        self.surf
        self.surf
        self.rect
        self.rect.center
        self.aks
        self.vinkel = theta

class voksende_ring():
    def __init__(self,mouse):  
        self.radius = 5
        self.iterasjon = 0
        self.sirkel = Sirkel(mouse,self.radius)
        self.posisjon = self.sirkel.rect
        self.alpha = 125
   
    
    def update(self):
        self.iterasjon = self.iterasjon + 1
        self.radius = self.radius + 1
        self.posisjon[0] -= 1
        self.posisjon[1] -= 1
        self.alpha = self.alpha - 1.5
        self.sirkel = Sirkel(self.posisjon,self.radius)
        self.sirkel.surf.set_alpha(self.alpha)

#def roter(surf,image,pos,origenpos,vinkel):

# define a main function
def main():
     
    
    pygame.init()
    pygame.display.set_caption("plopp:)")
    screen = pygame.display.set_mode((1200,800))
    clock = pygame.time.Clock()
    
    bakgrunn = pygame.image.load("textures/bakgrunn.jpg")
    and_surf = pygame.image.load("textures/topviewduck.png").convert_alpha()
    and_surf = pygame.transform.scale(and_surf,(40,40))
    and_rect = and_surf.get_rect(center=(400,250))
    and_surf = pygame.transform.rotate(and_surf,180)
    
    idleringer_timer = pygame.USEREVENT + 1
    and_move_timer = pygame.USEREVENT + 2
    bevegelse_timer = pygame.USEREVENT + 3
    pygame.time.set_timer(and_move_timer,100)
    pygame.time.set_timer(idleringer_timer,600)
    pygame.time.set_timer(bevegelse_timer,20)
    
    ringer = []
    i = 0
    aks = 1
    theta = 90
    sirkel = None
    sirkel_0 = None
    vektor = pygame.math.Vector2(0,3)
    
    while True:
        mouse = pygame.mouse.get_pos()
        keys = pygame.key.get_pressed()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                exit()
            
            if event.type == idleringer_timer: 
                if not keys[pygame.K_w]:
                    sirkel_1 = voksende_ring(and_rect.center)
                    ringer.append(sirkel_1) 
            
            if event.type == and_move_timer: 
                if keys[pygame.K_w]:
                    sirkel_2 = voksende_ring(and_rect.center)
                    ringer.append(sirkel_2)
            
            if event.type == bevegelse_timer:
                and_rect.x = and_rect.x + vektor[0] 
                and_rect.y = and_rect.y - vektor[1]

    
        if keys[pygame.K_a]:
                theta += 1.5
                vektor = pygame.math.Vector2(int(4* ma.cos(ma.radians(theta))),int(4 * ma.sin(ma.radians(theta))))
        if keys[pygame.K_d]:
                theta -= 1.5
                vektor = pygame.math.Vector2(int(4* ma.cos(ma.radians(theta))),int(4 * ma.sin(ma.radians(theta))))
        
        
        vektorlen = vektor.length()
    
        if keys[pygame.K_w]:
            if aks < 1:
                aks += 0.1
            if aks >= 1:
                aks = 1
        if not keys[pygame.K_w]:
            if aks > 0:
                aks -= 0.001
            else: 
                aks = 0
            


        vektor[0] = vektor[0] * aks
        vektor[1] = vektor[1] * aks
            
    
        
        
        if pygame.mouse.get_pressed()[0]:
            i += 1
            if i == 1:
                sirkel = voksende_ring(mouse)
                ringer.append(sirkel)
            if event.type == pygame.MOUSEMOTION:
                    if i % 3 == 0:
                        sirkel_0 = voksende_ring(mouse)
                        ringer.append(sirkel_0)        
            
        screen.blit(bakgrunn,(0,0))
        
        
        for element in ringer:
            if element.radius < 100:
                element.update()
                screen.blit(element.sirkel.surf,element.posisjon)
            if element.radius == 100:
                ringer.remove(element) 
            #print(len(ringer))

        and_surf_rotert = pygame.transform.rotate(and_surf,theta)
        
        if pygame.mouse.get_pressed()[0] == False:
            i = 0
        
        print(vektor,aks)
        screen.blit(and_surf_rotert,and_rect)
        pygame.display.update()
        clock.tick(60)       
        #print(theta)


# run the main function only if this module is executed as the main script
# (if you import this as a module then nothing is executed)
if __name__=="__main__":
    main()



