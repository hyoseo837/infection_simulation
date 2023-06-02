class human:
    def __init__(self, x_pos, y_pos, status):
        self.x_pos = x_pos
        self.y_pos = y_pos
        self.status = status

    def print_status(self):
        print("human at ({0},{1}) is {2}".format(self.x_pos, self.y_pos, self.status))

citizen_y = []
citizen = []

for x in range(1,11):
    for y in range(1,11):
        citizen_y.append(human(x,y,"healthy"))
    citizen.append(citizen_y)
    citizen_y = []

# for i in citizen:
#     for j in i:
#         j.print_status()