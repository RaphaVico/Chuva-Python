import sys, pygame,time
import numpy as np
import random

display=pygame.display.set_mode((500,500))
clock = pygame.time.Clock()

class gota():
    def __init__(self,xi,yi,m):
        self.xi = xi
        self.yi = yi
        self.m = np.array([m])
        self.pos = np.array([xi,yi])
        self.vel = np.array([0,0])
        self.acc = np.array([0,0])
        self.tamanho = random.uniform(1*m,2*m)

    def applyForce(self,force):
        self.acc = force/self.m

    def edge(self):
        if self.pos[1] >=500:
            self.pos[1] = random.uniform(0,10)
            self.pos[0] = random.uniform(0,500)
            self.vel = np.array([0,random.uniform(0,10)])

    def update(self):
        self.pos = self.vel+self.pos
        self.vel = self.vel+self.acc

    def draw(self):
        return pygame.draw.line(display,(138,43,226),(self.pos[0],self.pos[1]),(self.pos[0],self.pos[1]-self.tamanho))

gotas = []
for i in range(0,500):
    x = random.uniform(0,500)
    y = random.uniform(0,500)
    m = random.uniform(1, 11)
    gotas.append(gota(x,y,m))

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT: sys.exit()
    display.fill((0, 0, 0))
    for i in gotas:
        i.applyForce([0,0.1*i.m])
        i.edge()
        i.draw()
        i.update()
    clock.tick(30)
    pygame.display.flip()
