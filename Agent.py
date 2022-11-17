class Agent:

    # attributes
        # kind
        # x coordinate
        # y coordinate
        # could S types have higher velocities?

    def __init__(self, kind: str, x: int, y: int, screen_size: int, x_vel: int, y_vel: int, colour: tuple):
        self.kind = kind
        self.x = x
        self.y = y
        self.screen_size = screen_size
        self.radius = 10
        self.x_vel = x_vel
        self.y_vel = y_vel
        self.colour = colour

    def move(self, agents):
        
        self.check_collision(agents)
            
        self.x += self.x_vel
        self.y += self.y_vel

    def check_collision(self, agents):
        
        for a in agents:

            x_range = list(range(int((self.x - (self.radius/2))), int((self.x + (self.radius/2)))))
            y_range = list(range(int((self.y - (self.radius/2))), int((self.y + (self.radius/2)))))
            # if self.kind == 'S':
            #     print(x_range, y_range)
            if a.x in x_range and a.y in y_range:
                # check the kinds of the two corresponding agents
                if self.kind == 'S':
                    if a.kind == 'S':
                        break
                    elif a.kind == 'I':
                        a.kind = 'S'
                        a.colour = (215, 45, 45)
                    elif a.kind == 'R':
                        self.kind = 'R'
                        self.colour = (0, 0, 255)

                # elif self.kind == 'I':
                #     if a.kind == 'S':
                #         self.kind = 'S'
                #         self.kind = (215, 45, 45)

        if int(self.x) > self.screen_size or int(self.x) < 0:
            self.x_vel *= -1
        if int(self.y) > self.screen_size or int(self.y) < 0:
            self.y_vel *= -1
