import random
from Agent import Agent

def create_agents(N, num_ignorants, num_spreaders, num_stiflers):
    
    agents = []

    # note that spreaders have a higher range of velocities
    for s in range(num_spreaders):
        # use RNG to determine the initial agent velocity vector
        x = random.randint(0, N)
        y = random.randint(0, N)
        x_vel = random.randint(5, 10)
        y_vel = random.randint(5, 10)

        agent = Agent('S', x, y, N, x_vel, y_vel, (215, 45, 45))
        agents.append(agent)
                    
    for i in range(num_ignorants):

        # use RNG to determine the initial agent velocity vector
        x = random.randint(0, N)
        y = random.randint(0, N)
        x_vel = random.randint(4, 6)
        y_vel = random.randint(4, 6)

        agent = Agent('I', x, y, N, x_vel, y_vel, (255, 255, 255))
        agents.append(agent)

    for r in range(num_stiflers):

        # use RNG to determine the initial agent velocity vector
        x = random.randint(0, N)
        y = random.randint(0, N)
        x_vel = random.randint(4, 6)
        y_vel = random.randint(4, 6)

        agent = Agent('R', x, y, N, x_vel, y_vel, (0, 0, 255))
        agents.append(agent)

    return agents

def move_agents(agents):
    
    # need to update the positions of all agents and then recreate the domain 
    # according to those updated coordinates
    for i in range(len(agents)):
        agents[i].move(agents)

    return agents