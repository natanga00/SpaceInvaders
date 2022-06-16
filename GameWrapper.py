import math

class GameWrapper:
    def __init__(self, pygame):
        self.game = pygame
        self.game.init()
        self.screen = None
        self.game_font = {}

        self.load_default_config()
        self.load_game_music('data/background.wav')
        
    def load_default_config(self):
        self.set_screen()
        self.game.display.set_caption("UNIBH Space Invaders")
        self.game_font['default_font'] = self.game.font.Font('freesansbold.ttf', 20)
        self.game_font['game_over_font'] = self.game.font.Font('freesansbold.ttf', 64)
        
    def set_screen(self, width = 800, height = 600):
        self.screen = self.game.display.set_mode((width, height))

    def load_game_music(self, music_file):
        self.game.mixer.music.load(music_file)
        self.game.mixer.music.play()

    def display_score(self, score):
        score_text = self.game_font['default_font'].render("Pontos: " + str(score), True, (255, 255, 255))
        self.screen.blit(score_text, (5, 5))

    def game_over(self):
        game_over_text = self.game_font['game_over_font'].render('GAME OVER', True, (255, 255, 255))
        self.screen.blit(game_over_text, (190, 250))

    def objectsCollided(self, first_object, second_object):
        return math.sqrt((math.pow(first_object['x'] - second_object['x'], 2)) + (math.pow(first_object['y'] - second_object['y'], 2))) <= 50