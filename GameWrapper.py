import math

class GameWrapper:
    GAME_STATUS_PLAYING = 10
    GAME_STATUS_OVER = 20
    GAME_STATUS_FINISHED = 30

    def __init__(self, pygame):
        self.game = pygame
        self.game.init()
        self.screen = None
        self.game_font = {}
        self.current_game_status = self.GAME_STATUS_PLAYING

        self.load_default_config()
        self.load_game_music('data/background.wav')
        
    def load_default_config(self):
        self.set_screen()
        self.game.display.set_caption("UNIBH Space Invaders")
        self.game_font['default_font'] = self.game.font.Font('freesansbold.ttf', 20)
        self.game_font['game_event_font'] = self.game.font.Font('freesansbold.ttf', 64)
        
    def set_screen(self, width = 800, height = 600):
        self.screen = self.game.display.set_mode((width, height))

    def load_game_music(self, music_file):
        self.game.mixer.music.load(music_file)
        self.game.mixer.music.play()

    def display_info_on_screen(self, message, position):
        score_text = self.game_font['default_font'].render(message, True, (255, 255, 255))
        self.screen.blit(score_text, position)

    def game_over(self):
        self.current_game_status = self.GAME_STATUS_OVER
        
        game_over_text = self.game_font['game_event_font'].render('GAME OVER', True, (255, 255, 255))
        self.screen.blit(game_over_text, (190, 250))

    def objectsCollided(self, first_object, second_object):
        return math.sqrt((math.pow(first_object['x'] - second_object['x'], 2)) + (math.pow(first_object['y'] - second_object['y'], 2))) <= 50

    def finished_game(self):
        self.current_game_status = self.GAME_STATUS_FINISHED

        finished_game_text = self.game_font['default_font'].render('Parabéns você salvou a galáxia Anima', True, (255, 255, 255))
        self.screen.blit(finished_game_text, (190, 250))