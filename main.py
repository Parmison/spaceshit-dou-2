import pygame
import time
pygame.init()

space = pygame.image.load("lesson 6/image/space bg.png")

yellow_ship = pygame.image.load("lesson 6/image/spaceship yellow.png")
yellow_ship= pygame.transform.scale(yellow_ship,(100,100))

orange_ship = pygame.image.load("lesson 6/image/spaceship orange.png")
orange_ship = pygame.transform.scale(orange_ship,(100,100))

font = pygame.font.SysFont("Times New Roman",36)

screen = pygame.display.set_mode((1250,690))

border = pygame.Rect(625,0,5,690)

#pygame.sprite.Sprite

class spaceship(pygame.sprite.Sprite):
    def __init__(self,x,y,color):
        super().__init__()
        self.color = color
        if color == "yellow":
            self.image = pygame.transform.rotate(yellow_ship,90)
        elif color == "orange":
            self.image = pygame.transform.rotate(orange_ship,270)
        self.rect = self.image.get_rect()
        self.rect.center = (x,y)
        self.health = 100
    def handel_movement(self,keys):
        if self.color == "orange":
            if keys[pygame.K_UP] and self.rect.y>50:
                self.rect.y -= 1
            if keys[pygame.K_DOWN] and self.rect.y<550:
                self.rect.y += 1
            if keys[pygame.K_LEFT] and self.rect.x>650:
                self.rect.x -= 1
            if keys[pygame.K_RIGHT] and self.rect.x<1000:
                self.rect.x += 1

        if self.color == "yellow":
            if keys[pygame.K_w] and self.rect.y>50:
                self.rect.y -= 1
            if keys[pygame.K_s] and self.rect.y<550:
                self.rect.y += 1
            if keys[pygame.K_a] and self.rect.x>50:
                self.rect.x -= 1
            if keys[pygame.K_d] and self.rect.x<450:
                self.rect.x += 1

orange = spaceship(950,330,"orange")
yellow = spaceship(350,330,"yellow")

def draw_text():
    text1 = font.render(f"health left yellow:{yellow.health}",True,"white")
    text2 = font.render(f"health left orange:{orange.health}",True,"white")
    screen.blit(text1,(100,50))
    screen.blit(text2,(900,50))
    pygame.display.update()
    pygame.time.delay(5000)

def draw_window(yellow,orange):
    screen.blit(space,(0,0))
    pygame.draw.rect(screen,"white",border)
    screen.blit(orange.image,orange.rect.center)
    screen.blit(yellow.image,yellow.rect.center)
    pygame.display.update()
clock = pygame.time.Clock()

while True:
    clock.tick(60)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
    keys = pygame.key.get_pressed()
    orange.handel_movement(keys)
    yellow.handel_movement(keys)
    draw_window(yellow,orange)
    draw_text()
