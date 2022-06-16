import random

class Invader:
    def __init__(self, image):
        self.image = image
        self.position_x = random.randint(64, 737)
        self.position_y = random.randint(30, 180)

    def generate_new_position(self):
        self.position_x = random.randint(64, 737)
        self.position_y = random.randint(30, 180)