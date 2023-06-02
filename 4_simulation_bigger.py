import pygame
import random

pygame.init()


screen_width = 1000
screen_height = 1000
screen = pygame.display.set_mode((screen_width, screen_height))

pygame.display.set_caption("COVID Simulation")

# text
Main_Font = pygame.font.Font(None, 30)

background = pygame.image.load("C:/Users/효서/Documents/Programming/python/project_covid_simulation/image/background.png")

# variable
status = ""
citizen_y = []
citizen = []
day = 0

# class
class human: 
    def __init__(self, x_pos, y_pos, status, x_co, y_co):
        self.x_pos = x_pos
        self.y_pos = y_pos
        self.status = status
        self.x_co = x_co
        self.y_co = y_co
        self.neighbor_infected = 0
        self.recover_time = 0
        self.cured_time = 10
        self.sprite = pygame.image.load("C:/Users/효서/Documents/Programming/python/project_covid_simulation/image/healthy_big.png")

    def print_status(self):
        print("human at ({0},{1}) is {2}".format(self.x_pos, self.y_pos, self.status))

    def neighbor(self):
        self.neighbor_infected = 0
        if self.x_co != 0:
            if citizen[self.x_co-1][self.y_co].status == "infected":
                self.neighbor_infected += 1
        
        if self.x_co != 150:
            if citizen[self.x_co+1][self.y_co].status == "infected":
                self.neighbor_infected += 1
        
        if self.y_co != 150:
            if citizen[self.x_co][self.y_co+1].status == "infected":
                self.neighbor_infected += 1
        
        if self.y_co != 0:
            if citizen[self.x_co][self.y_co-1].status == "infected":
                self.neighbor_infected += 1
    
    def healthy(self):
        self.status = "healthy"
        self.sprite = pygame.image.load("C:/Users/효서/Documents/Programming/python/project_covid_simulation/image/healthy_big.png")

    def infect(self):
        self.recover_time = 3
        self.recover_rate = 10
        self.status = "infected"
        self.sprite = pygame.image.load("C:/Users/효서/Documents/Programming/python/project_covid_simulation/image/infected_big.png")

    def cure(self):
        self.cured_time = 25
        self.status = "cured"
        self.sprite = pygame.image.load("C:/Users/효서/Documents/Programming/python/project_covid_simulation/image/cured_big.png")
    
    def die(self):
        self.status = "died"
        self.sprite = pygame.image.load("C:/Users/효서/Documents/Programming/python/project_covid_simulation/image/died_big.png")

    def update(self):
        if self.status == "healthy":
            self.neighbor()
            if self.neighbor_infected > 0:
                if random.randrange(6) < self.neighbor_infected:
                    self.infect()
        if self.status == "infected":
            self.recover_time -= 1
            if self.recover_time <= 0:
                if random.randrange(self.recover_rate) == 0:
                    self.cure()
            if random.randrange(200) == 0:
                self.die()
        if self.status == "cured":
            self.cured_time -= 1
            if self.cured_time == 0:
                self.healthy()


for x in range(2,153):
    for y in range(2,153):
        citizen_y.append(human(x * 6, y * 6,"healthy", x-2, y-2))
    citizen.append(citizen_y)
    citizen_y = []

citizen[random.randrange(150)][random.randrange(150)].infect()

# event loop
running = True
while running:

    # FPS setting
    dt = pygame.time.Clock().tick(10)

    # Check event
    for event in pygame.event.get():
        
        if event.type == pygame.QUIT:
            running = False
        
        # Event about keyboard/mouse
        # if event.type == pygame.KEYDOWN:
        #     if event.key == pygame.K_SPACE:
    day += 1
    for i in citizen:
        for j in i:
            j.update()
    
    # Draw in Screen
    # Draw background
    screen.blit(background, (0, 0))
    # count number
    (h_num, i_num, c_num, d_num) = (0,0,0,0)
    for i in citizen:
        for j in i:
            if j.status == "healthy":
                h_num += 1
            elif j.status == "infected":
                i_num += 1
            elif j.status == "cured":
                c_num += 1
            elif j.status == "died":
                d_num += 1
            
    if i_num == 0:
        running = False
    # text
    healthy_number = Main_Font.render(("healthy : " + str(h_num)),True,(255,255,255))
    infected_number = Main_Font.render(("infected : " + str(i_num)), True, (255,255,255))
    cured_number = Main_Font.render(("cured : " + str(c_num)), True, (255,255,255))
    died_number = Main_Font.render(("died : " + str(d_num)), True, (255,255,255))
    days = Main_Font.render((str(day) + " days"), True, (255,255,255))

    # Draw Sprite
    for i in citizen:
        for j in i:
            if j.status == "healthy":
                screen.blit(j.sprite, (j.x_pos + 30, j.y_pos + 30))
            elif j.status == "infected":
                screen.blit(j.sprite, (j.x_pos + 30, j.y_pos + 30))
            elif j.status == "cured":
                screen.blit(j.sprite, (j.x_pos + 30, j.y_pos + 30))
            elif j.status == "died":
                screen.blit(j.sprite, (j.x_pos + 30, j.y_pos + 30))
            
    # Draw Text
    screen.blit(healthy_number,(10,10))
    screen.blit(infected_number,(210,10))
    screen.blit(cured_number,(410,10))
    screen.blit(died_number,(610,10))
    screen.blit(days, (900,10))

    # Update Screen
    pygame.display.update() 

# pause
pygame.time.delay(1000)
print(h_num)
print(i_num)
print(c_num)
print(d_num)
# end game 
pygame.quit()