import pygame
from pygame.locals import *

from gl import Renderer, Model
import shaders
import numpy as np

deltaTime = 0.0

# Inicializacion de pygame
pygame.init()
clock = pygame.time.Clock()
screenSize = (1000, 600)
screen = pygame.display.set_mode(screenSize, DOUBLEBUF | OPENGL)

# Inicializacion de nuestro Renderer en OpenGL
r = Renderer(screen)
r.camPosition.z = 1
r.camPosition.y = 0
r.camPosition.x = 0
r.pointLight.x = 200
r.pointLight.z = 200


r.setShaders(shaders.vertex_shader, shaders.fragment_shader)

r.modelList.append(Model('modelos/teodoro.obj', 'modelos/teodoro.bmp'))

def ratatoskr():
    pygame.mixer.music.load('sonidos/rata2.mp3')
    pygame.mixer.music.play(0)
def ratatouille():
    pygame.mixer.music.load('sonidos/lefestin.mp3')
    pygame.mixer.music.play(0)
def loba():
    pygame.mixer.music.load('sonidos/loba.mp3')
    pygame.mixer.music.play(0)  

isPlaying = True
ratatouille()
while isPlaying:

    # Para revisar si una tecla esta presionada
    keys = pygame.key.get_pressed()
    # Move cam
        #a traslada en x-
    if keys[pygame.K_a]:
        r.camPosition.x += 0.2 * deltaTime
       #d traslada en x+  
    if keys[pygame.K_d]:
        r.camPosition.x -= 0.2 * deltaTime
        #S traslada en y+
    if keys[pygame.K_s]:
        r.camPosition.y += 0.2 * deltaTime
        #W traslada en y+
    if keys[pygame.K_w]:
        r.camPosition.y -= 0.2 * deltaTime
        #Espacio traslada en positivo a z+
    if keys[pygame.K_SPACE]:
        r.camPosition.z -= 2 * deltaTime 
        #Backspace traslada en a z-       
    if keys[pygame.K_BACKSPACE]:
        r.camPosition.z += 2 * deltaTime   
        #UP para rotar en eje X+     
    if keys[pygame.K_UP]:
        r.rx += 25 * deltaTime 
        #Down para rotar en eje X-
    if keys[pygame.K_DOWN]:
        r.rx -= 25 * deltaTime  
        #Left para rotar en eje Z-
    if keys[pygame.K_LEFT]:
        r.ry -= 25 * deltaTime 
        #Right rotar en eje z+
    if keys[pygame.K_RIGHT]:
        r.ry += 25 * deltaTime 
        #q para rotar en eje Y+
    if keys[pygame.K_q]:
        r.rz += 25 * deltaTime 
        #E para rotar en eje Y+
    if keys[pygame.K_e]:
        r.rz -= 25 * deltaTime   
        #La tecla r cambia el modelo a la rata
    if keys[pygame.K_r]:
        r.modelList.clear()
        ratatoskr()
        r.camPosition.x = 0
        r.camPosition.y = 0
        r.camPosition.z = -4.2  
        r.modelList.append(Model('modelos/ratatoskr.obj', 'modelos/ratatoskr.bmp'))
        #La t cambia el modelo a teodoro
    if keys[pygame.K_t]:
        r.modelList.clear()
        ratatouille()
        r.camPosition.z = 1
        r.camPosition.y = 0
        r.camPosition.x = 0
        r.modelList.append(Model('modelos/teodoro.obj', 'modelos/teodoro.bmp'))
        #La l cambia el modelo a teodoro
    if keys[pygame.K_l]:
        r.modelList.clear()
        loba()
        r.camPosition.z = -14.2
        r.camPosition.y = 7.7
        r.camPosition.x = 2.5
        r.modelList.append(Model('modelos/loba.obj', 'modelos/loba.bmp'))  
    for ev in pygame.event.get():
        if ev.type == pygame.QUIT:
            isPlaying = False
        elif ev.type == pygame.KEYDOWN:
            # para revisar en el momento que se presiona una tecla
            if ev.key == pygame.K_1:
                r.filledMode()
            elif ev.key == pygame.K_2:
                r.wireframeMode()
                #con escape cerramos py
            elif ev.key == pygame.K_ESCAPE:
                isPlaying = False
                #Tecla click cambia la luz
        elif ev.type == pygame.MOUSEBUTTONUP:
            r.pointLight.x = -r.pointLight.x
            r.pointLight.y = -r.pointLight.y

    # Main Renderer Loop
    r.render()

    pygame.display.flip()
    clock.tick(60)
    deltaTime = clock.get_time() / 1000


pygame.quit()
