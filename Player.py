class Player:
    def __init__(self, image):
        self.playerImage = image
        self.position_x = 370
        self.position_y = 523

    def displayPlayer(self, x_axis, y_axis, screen):
        screen.blit(self.playerImage, x_axis, y_axis)
    
    def restrict_player_moviment(self):
        if self.position_x <= 16:
            self.position_x = 16;
        elif self.position_x >= 750:
            self.position_x = 750