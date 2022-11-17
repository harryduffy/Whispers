from helpers import create_agents, move_agents
import pygame

pygame.init()


# have these as command line args
# Size of the system
N = 500
# Number of Spreaders
num_spreaders = 1
# Number of Ignorants
num_ignorants = 20

size = (N, N)
screen = pygame.display.set_mode(size)

pygame.display.set_caption("Whispers")
agents = create_agents(N, num_ignorants, num_spreaders)

run = True
while run:
    pygame.time.delay(100)
    
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False

    keys = pygame.key.get_pressed()

    if keys[pygame.K_ESCAPE]:
        run = False

    screen.fill((0, 0, 0))

    agents = move_agents(agents)
    
    # plot all the different circles
    for i in range(len(agents)):
        agent = agents[i]
        pygame.draw.circle(screen, agent.colour, (agent.x, agent.y), agent.radius)

    pygame.display.update()

pygame.quit()
