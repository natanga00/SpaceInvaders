class Bullet:
    def __init__(self, image, sound):
        self.image = image
        self.sound = sound
        self.position_x = 0
        self.position_y = 500
        self.state = 'carregada' #Carrega significa que a bala "esta preparada", ou seja parada