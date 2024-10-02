import pygame
import random
pygame.init()

#create user defined events
#EVENT_NAME = pygame.USEREVENT+order_of_the_event
SPRITE_COLOR_CHANGE = pygame.USEREVENT+1
BG_COLOR_CHANGE = pygame.USEREVENT+2

#create variables for storing the variety of sprite colors
yellow = pygame.Color("yellow")
white = pygame.Color("white")
pink = pygame.Color("pink")
lightblue = pygame.Color("lightblue")

#create variables for storing the variety of background Colors
blue = pygame.Color('darkblue')
red = pygame.Color('red')
green = pygame.Color('darkgreen')
black = pygame.Color('black')

#to create a sprite a class should be created
class sprite(pygame.sprite.Sprite):
    
    def __init__(self,color,height,width):
        #transfer all the parent class properties to this class
        super().__init__()
        self.image = pygame.Surface([width,height])
        self.image.fill(color)

        #to replace the image with a rectangle
        self.rect = self.image.get_rect()

        #to add movements to the sprite -->  [either -1 or 1, either -1 or 1]
        self.velocity = [random.choice([-1,1]),random.choice([-1,1])]

    #to update the sprite's position everytime it moves and also checks for the boundary collisions
    def update(self):
        self.rect.move_ip(self.velocity)
        boundary_collide = False

        #if the sprite touches the left / right side of the boundary
        if self.rect.left<=0 or self.rect.right>=500:
            #make the sprite move towards the opposite direction
            self.velocity[0] = -self.velocity[0]
            boundary_collide = True
        #if the sprite touches the top / bottom side of the boundary
        if self.rect.top<=0 or self.rect.bottom>=500:
            self.velocity[1] = -self.velocity[1]
            boundary_collide = True

        #If boundary_collide is true, call the color changing events of both sprite and bg
        if boundary_collide:
            pygame.event.post(pygame.event.Event(SPRITE_COLOR_CHANGE))
            pygame.event.post(pygame.event.Event(BG_COLOR_CHANGE))

    #to create a function to change the color of the sprite
    def sprite_color(self):
        self.image.fill(random.choice([yellow,white,lightblue,pink]))

#to create a function to change the background color
def bg_color():
    global bg
    bg = random.choice([red,blue,green,black])

#to create a sprite group --> groupName = pygame.sprite.Group()
spritegroup = pygame.sprite.Group()

#to create a sprite --> spriteName = className(values of the properties)
s1= sprite(white,20,30)

#assign the position for the sprite, anywhere randomly in the screen
s1.rect.x = random.randint(0,480)
s1.rect.y = random.randint(0,470)

#to add the sprite in the group --> groupname.add(spriteName)
spritegroup.add(s1)

#to create a window
screen = pygame.display.set_mode((500,400))
bg = red
screen.fill(bg)

while True:
    for i in pygame.event.get():
        if i.type == pygame.QUIT:
            pygame.quit()
        elif i.type== SPRITE_COLOR_CHANGE:
            s1.sprite_color()
        elif i.type== BG_COLOR_CHANGE:
            bg_color()
    
    #to update the sprites
    spritegroup.update()

    screen.fill(bg)

    #to display the sprites on the screen
    spritegroup.draw(screen)
    pygame.display.flip()