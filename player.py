class Player:
    def __init__(self, pygame):
        self.playerImage = pygame.image.load('data/spaceship.png')
        self.player_X = 370
        self.player_Y = 523
        self.player_Xchange = 0

    def