import pygame


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

# class
class human:
    def __init__(self, x_pos, y_pos, status):
        self.x_pos = x_pos
        self.y_pos = y_pos
        self.status = status
        self.sprite = pygame.image.load("C:/Users/효서/Documents/Programming/python/project_covid_simulation/image/healthy.png")

    def print_status(self):
        print("human at ({0},{1}) is {2}".format(self.x_pos, self.y_pos, self.status))

for x in range(2,49):
    for y in range(2,49):
        citizen_y.append(human(x * 20, y * 20,"healthy"))
    citizen.append(citizen_y)
    citizen_y = []


# event loop
running = True
while running:

    # FPS setting
    # dt = clock.tick([FPS])

    # Check event
    for event in pygame.event.get():
        
        if event.type == pygame.QUIT:
            running = False
        
        # Event about keyboard/mouse
        # if event.type == pygame.KEYDOWN:
        #     if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
        #         [Action]
    
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
            
    # text
    healthy_number = Main_Font.render(str(h_num),True,(255,255,255))
    infected_number = Main_Font.render(str(i_num), True, (255,255,255))
    cured_number = Main_Font.render(str(c_num), True, (255,255,255))
    died_number = Main_Font.render(str(d_num), True, (255,255,255))

    # Draw Sprite
    for i in citizen:
        for j in i:
            if j.status == "healthy":
                screen.blit(j.sprite, (j.x_pos, j.y_pos))
            elif j.status == "infected":
                screen.blit(j.sprite, (j.x_pos, j.y_pos))
            elif j.status == "cured":
                screen.blit(j.sprite, (j.x_pos, j.y_pos))
            elif j.status == "died":
                screen.blit(j.sprite, (j.x_pos, j.y_pos))
            
    # Draw Text
    screen.blit(healthy_number,(10,10))
    screen.blit(infected_number,(110,10))
    screen.blit(cured_number,(210,10))
    screen.blit(died_number,(310,10))

    # Update Screen
    pygame.display.update() 

# pause
pygame.time.delay(200)

# end game 
pygame.quit()