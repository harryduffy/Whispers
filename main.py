from helpers import create_agents, move_agents
import pygame

pygame.init()

# Initialise the system constants
# have these as command line args
# Size of the system
N = 500
# Number of Spreaders
NUM_SPREADERS = 1
# Number of Ignorants
NUM_IGNORANTS = 20
#Number of Stiflers
NUM_STIFLERS = 5
# The amount of time (milliseconds) it takes for a spreader to become a stifler
TIME_TIL_BORED = 200

screen = pygame.display.set_mode((N, N))

pygame.display.set_caption("Whispers")

agents = create_agents(N, NUM_IGNORANTS, NUM_SPREADERS, NUM_STIFLERS)

simulation_time = 0
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
    # if all the agents are Stiflers, the rumination period should cease
    stifler_count = 0
    ignorant_count = 0
    for i in range(len(agents)):
        agent = agents[i]
        agent.tick_ruminating_time(TIME_TIL_BORED)
        
        if agent.kind == 'R':
            stifler_count += 1
        elif agent.kind == 'I':
            ignorant_count += 1

        pygame.draw.circle(screen, agent.colour, (agent.x, agent.y), agent.radius)

    if stifler_count == len(agents) or (stifler_count+ignorant_count) == len(agents):
        screen.fill((255, 255, 255))
        run = False

    pygame.display.update()
    simulation_time += 1

pygame.quit()

print(f"The simulation ran for {simulation_time/10} seconds.")
