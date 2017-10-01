import physics as pf
import pygame
import pygame.gfxdraw
import numpy as np

# initialize physics simulation
DIM = np.asarray([400, 400])
GRAVITY = np.asarray([0, 0])
dt = 0.01
env = pf.Environment(DIM, GRAVITY, dt)

pygame.init()
screen = pygame.display.set_mode((DIM[0], DIM[1]))
pygame.display.set_caption('Elastic Collision Particle Simulation')

number_of_particles = np.random.randint(5,10)

for n in range(number_of_particles):
    radius = np.random.randint(10, 20)
    density = np.random.randint(50, 75)
    mass = (4/3)*density*np.pi*radius**3
    X = np.random.rand(1, 2)*(DIM-radius)+radius
    V = np.random.rand(1, 2)*75
    A = np.asarray([0, 0])
    particle = pf.Particle(env, X, V, A, radius, mass, density)
    env.addParticle(particle)

def display(env):
    for p in env.particles:
        pygame.gfxdraw.filled_circle(screen, int(p.X[0][0]), int(p.X[0][1]), p.radius, p.colour)

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    screen.fill([255, 255, 255])
    env.update()
    display(env)
    pygame.display.flip()
