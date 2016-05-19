import pygame
import sys
from pygame.locals import *
FPS = 60
fpsClock = pygame.time.Clock()
pygame.init()
display_info = pygame.display.Info()
wid = display_info.current_w
hei = display_info.current_h
dis = pygame.display.set_mode((wid/2,hei/2),0,32)
BLACK = (0,0,0,255)
WHITE = (255,255,255,255)
GREEN = (0,255,0,255)
BLUE = (0,0,255,255)
RED = (255,0,0,0)
direction = 'left'
snail = pygame.image.load('snail.png')
snail = pygame.transform.scale(snail,(300,150))
snailx=0
snaily=0
pygame.display.set_caption("what is this screen?")

while True:
     flip_x = False
     for event in pygame.event.get():
          if event.type == QUIT:
               pygame.quit()
               sys.exit()
          if event.type == KEYDOWN:

               if direction == 'right' and event.key == K_RIGHT:
                    flip_x = False
               elif direction == 'right' and event.key == K_LEFT:
                    flip_x = True
               elif direction == 'left' and event.key == K_LEFT:
                    flip_x = False
               elif direction == 'left' and event.key == K_RIGHT:
                    flip_x = True

               if event.key == K_RIGHT:
                    direction = 'right'
               elif event.key == K_LEFT:
                    direction = 'left'
                    
     dis.fill(WHITE)
     snail = pygame.transform.flip(snail,flip_x,False)
     dis.blit(snail,(snailx,snaily))
               
     key_pressed =pygame. key.get_pressed()
     
     if key_pressed[K_RIGHT]:
          if snailx == wid/2:
               snailx += 0
          else:
               snailx += 1
     elif key_pressed[K_DOWN]:
          if snaily == hei/2:
               snaily +=0
          else:
               snaily += 1
     elif key_pressed[K_LEFT]:
          if snailx == 0:
               snailx +=0
          else:
               snailx -= 1
     elif key_pressed[K_UP]:
          if snaily ==0:
               snaily +=0
          else:
               snaily -= 1
          
     pygame.display.update()
