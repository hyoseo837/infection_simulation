import pygame
import random

pygame.init()


screen_width = 600
screen_height = 600
screen = pygame.display.set_mode((screen_width, screen_height))

pygame.display.set_caption("COVID Simulation")

# text
Main_Font = pygame.font.Font(None, 20)

background = pygame.image.load("image/background.png")

# independent variables
speed = 30
while True:
    print("=== CHOOSE THE VIRUS ===")
    print("1. COVID-19")
    print("2. SARS")
    print("3. MERS")
    ans = input()
    if ans == "1":
        iv_infect_rate = 5 
        iv_recover_time = 15
        iv_recover_rate = 30
        iv_cure_time = 200
        iv_death_rate = 2000
        virus = "COVID-19"
        break
    elif ans == "2":
        iv_infect_rate = 7
        iv_recover_time = 10
        iv_recover_rate = 30
        iv_cure_time = 230
        iv_death_rate = 500
        virus = "SARS"
        break
    elif ans == "3":
        iv_infect_rate = 2 
        iv_recover_time = 20
        iv_recover_rate = 20
        iv_cure_time = 200
        iv_death_rate = 150
        virus = "MERS"
        break
    else:
        print("Answer Error: Please enter the number")

# variable
status = ""
citizen_y = []
citizen = []
day = 0
pause = True
mod = "infect"
timer = 6
click_size = 1


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
        self.sprite = pygame.image.load("image/healthy_big.png")

    def print_status(self):
        print("human at ({0},{1}) is {2}".format(self.x_pos, self.y_pos, self.status))

    def neighbor(self):
        self.neighbor_infected = 0
        if self.x_co != 0:
            if citizen[self.x_co-1][self.y_co].status == "infected":
                self.neighbor_infected += 1
        
        if self.x_co != 82:
            if citizen[self.x_co+1][self.y_co].status == "infected":
                self.neighbor_infected += 1
        
        if self.y_co != 82:
            if citizen[self.x_co][self.y_co+1].status == "infected":
                self.neighbor_infected += 1
        
        if self.y_co != 0:
            if citizen[self.x_co][self.y_co-1].status == "infected":
                self.neighbor_infected += 1
    
    def healthy(self):
        self.status = "healthy"
        self.sprite = pygame.image.load("image/healthy_big.png")

    def infect(self):
        self.recover_time = iv_recover_time
        self.recover_rate = iv_recover_rate
        self.status = "infected"
        self.sprite = pygame.image.load("image/infected_big.png")

    def cure(self):
        self.cured_time = iv_cure_time
        self.status = "cured"
        self.sprite = pygame.image.load("image/cured_big.png")
    
    def die(self):
        self.status = "died"
        self.sprite = pygame.image.load("image/died_big.png")

    def blank(self):
        self.status = "blank"

    def update(self):
        if self.status == "healthy":
            if self.neighbor_infected > 0:
                if random.randrange(30) - self.neighbor_infected < iv_infect_rate:
                    self.infect()
        if self.status == "infected":
            self.recover_time -= 1
            if self.recover_time <= 0:
                if random.randrange(self.recover_rate) == 0:
                    self.cure()
            if random.randrange(iv_death_rate) == 0:
                self.die()
        if self.status == "cured":
            self.cured_time -= 1
            if self.cured_time == 0:
                self.healthy()


for x in range(2,85):
    for y in range(2,85):
        citizen_y.append(human(x * 6, y * 6,"healthy", x-2, y-2))
    citizen.append(citizen_y)
    citizen_y = []


# event loop
running = True
while running:

    # FPS setting
    dt = pygame.time.Clock().tick(speed)

    if not pause:
        timer += 1
    # 이벤트 처리
    event = pygame.event.poll()
    if event.type == pygame.QUIT:
        running = False
    elif event.type == pygame.MOUSEBUTTONDOWN:
        click_point = (int((event.pos[0]-30)/6) - 2, int((event.pos[1]-30)/6) - 2)
        
        for i in range(-click_size, click_size-1):
            for j in range(-click_size, click_size-1):
                if mod == "infect":
                    citizen[click_point[0] + i][click_point[1] + j].infect()
                elif mod == "blank":
                    citizen[click_point[0]+i][click_point[1]+j].blank()
                elif mod == "healthy":
                    citizen[click_point[0]+i][click_point[1]+j].healthy()

    elif event.type == pygame.KEYDOWN:
        if event.key == pygame.K_SPACE:
            pause = not pause
        if event.key == pygame.K_r:
            day = 0
            for i in citizen:
                for j in i:
                    j.healthy()
        if event.key == pygame.K_m:
            if mod == "infect":
                mod = "blank"
            elif mod == "blank":
                mod = "healthy"
            elif mod == "healthy":
                mod = "infect"
        if event.key == pygame.K_o:
            click_size -= 1
        if event.key == pygame.K_p:
            click_size += 1
    
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
            
    # if i_num == 0:
    #     running = False
    # text
    virus_name = Main_Font.render(virus, True, (255,255,255))
    healthy_number = Main_Font.render(("healthy : " + str(h_num)),True,(255,255,255))
    infected_number = Main_Font.render(("infected : " + str(i_num)), True, (255,255,255))
    cured_number = Main_Font.render(("cured : " + str(c_num)), True, (255,255,255))
    died_number = Main_Font.render(("died : " + str(d_num)), True, (255,255,255))
    days = Main_Font.render((str(day)), True, (255,255,255))
    mods = Main_Font.render(("mod : " + mod), True, (255,255,255))
    mouse_size = Main_Font.render(("size : ") + str(click_size), True, (255,255,255))

    # Draw Sprite
    for i in citizen:
        for j in i:
            if j.status != "blank":
                if j.status == "healthy":
                    screen.blit(j.sprite, (j.x_pos + 35, j.y_pos + 35))
                elif j.status == "infected":
                    screen.blit(j.sprite, (j.x_pos + 35, j.y_pos + 35))
                elif j.status == "cured":
                    screen.blit(j.sprite, (j.x_pos + 35, j.y_pos + 35))
                elif j.status == "died":
                    screen.blit(j.sprite, (j.x_pos + 35, j.y_pos + 35))
            
    # Draw Text
    screen.blit(healthy_number,(10, 20))
    screen.blit(infected_number,(110, 20))
    screen.blit(cured_number,(210, 20))
    screen.blit(died_number,(310, 20))
    screen.blit(days, (screen_width - 60, 10))
    screen.blit(mods, (10, screen_height - 20))
    screen.blit(mouse_size, (screen_width - 60, screen_height - 20))
    screen.blit(virus_name, (screen_width/2 - round(virus_name.get_rect().size[0]/2), screen_height - 20))

    # Update Screen
    pygame.display.update() 
    
    if not pause:
        day += 1
        for i in citizen:
            for j in i:
                j.neighbor()
        for i in citizen:
            for j in i:
                j.update()

# pause
pygame.time.delay(1000)
print(h_num)
print(i_num)
print(c_num)
print(d_num)
# end game 
pygame.quit()