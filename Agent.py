import random

class Agent:

    def __init__(self, kind: str, x: int, y: int, screen_size: int, x_vel: int, y_vel: int, colour: tuple):
        self.kind = kind
        self.x = x
        self.y = y
        self.screen_size = screen_size
        self.radius = 10
        self.x_vel = x_vel
        self.y_vel = y_vel
        self.colour = colour
        self.ruminating_time = 0

    def move(self, agents):
        
        self.check_collision(agents)
            
        self.x += self.x_vel
        self.y += self.y_vel

    def check_collision(self, agents):

        x_range = list(range(int((self.x - 1.5*self.radius)), int((self.x + 1.5*self.radius))))
        y_range = list(range(int((self.y - 1.5*self.radius)), int((self.y + 1.5*self.radius))))
        
        for a in agents:
            
            if (a.x in x_range and a.y in y_range) and a != self:
                
                if self.kind == 'S':
                    if a.kind == 'S':
                        break
                    elif a.kind == 'I':
                        a.kind = 'S'

                        # multiplying by itself over the absolute value of itself
                        # ensures the agent's velocity vector maintains its direction
                        a.x_vel = (a.x_vel/abs(a.x_vel)) * random.randint(5, 10)
                        a.y_vel = (a.x_vel/abs(a.x_vel)) * random.randint(5, 10)
                        a.colour = (215, 45, 45)
                    elif a.kind == 'R':
                        self.kind = 'R'

                        # multiplying by itself over the absolute value of itself
                        # ensures the agent's velocity vector maintains its direction
                        self.x_vel = (self.x_vel/abs(self.x_vel)) * random.randint(4, 6)
                        self.y_vel = (self.x_vel/abs(self.x_vel)) * random.randint(4, 6)
                        self.colour = (0, 0, 255)

                # this doesn't take into account the actual collision dynamics
                # need to calculate the true change in direction as being the 
                # opposite of the other agents vector (in either y or x but not both,
                # which depends on the relative position before the collision)

                # vec_self = [self.x, self.y] * self.y_vel/self.x_vel
                # vec_agent = [a.x, a.y] * a.y_vel/a.x_vel
                # self.x_vel *= -1
                # self.y_vel *= -1
                # a.x_vel *= -1
                # a.y_vel *= -1

        if int(self.x) > self.screen_size or int(self.x) < 0:
            self.x_vel *= -1
        if int(self.y) > self.screen_size or int(self.y) < 0:
            self.y_vel *= -1

    def tick_ruminating_time(self, time_til_bored: int):

        if not self.kind == 'S':
            return
        else:
            self.ruminating_time += 1

        if self.ruminating_time == time_til_bored:
            self.kind = 'R'
            self.colour = (0, 0, 255)