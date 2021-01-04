class Mario_Bros:

    def __init__(self, name:str, lives:int, power:str):
        self.name = name
        self.lives = lives
        self.power = power

    def move_right(self):
        print('{} is moving right'.format(self.name))
    
    def move_left(self):
        print('{} is moving left'.format(self.name))
    
    def look_up(self):
        print('{} is looking up'.format(self.name))
    
    def duck(self):
        print('{} is ducking'.format(self.name))
    
    def speed_up(self):
        print('{} is running'.format(self.name))
