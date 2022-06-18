import Background as Background
import pygame
import sys
from GameWrapper import GameWrapper 
from Player import Player
from Bullet import Bullet
from Invader import Invader
from Phase import Phase
from Background import Background

PygameWrapper = GameWrapper(pygame)
Player = Player(PygameWrapper.game.image.load('data/nave.png'))
score = 0
Phase = Phase()

if Phase.current_phase == 1:
    BackGround = Background('data/Design sem nome.png', [0,0])
    Bullet = Bullet(PygameWrapper.game.image.load('data/bullet.png'), PygameWrapper.game.mixer.Sound('data/bullet.wav'))
    alien = 'data/alien1.png'
    score = 0
elif Phase.current_phase == 2:
    BackGround = Background('data/Design sem nome1.png', [0,0])
    Bullet = Bullet(PygameWrapper.game.image.load('data/bullet.png'), PygameWrapper.game.mixer.Sound('data/bullet.wav'))
    alien = 'data/alien2.png'
    score = 26
elif Phase.current_phase == 3:
    BackGround = Background('data/Design sem nome2.png', [0,0])
    Bullet = Bullet(PygameWrapper.game.image.load('data/bala1-removebg-preview.png'), PygameWrapper.game.mixer.Sound('data/bullet.wav'))
    alien = 'data/alien3.png'
    score = 81
elif Phase.current_phase == 4:
    BackGround = Background('data/Design sem nome3.png', [0,0])
    Bullet = Bullet(PygameWrapper.game.image.load('data/bullet2.png'), PygameWrapper.game.mixer.Sound('data/bullet.wav'))
    alien = 'data/alien4.png'
    score = 151
score = 0
player_position_x_change = 0

invaders_horde = []
invader_position_x_change = []
invader_position_y_change = []
invader_position_y_change = []

invaders_horde_size = 8

for num in range(invaders_horde_size):
    invaders_horde.append(Invader(PygameWrapper.game.image.load(alien)))
    invader_position_x_change.append(3.0)
    invader_position_y_change.append(50)

bullet_position_y_change = 3

# game loop
playing = True
while playing:

    PygameWrapper.screen.fill([255, 255, 255])
    PygameWrapper.screen.blit(BackGround.image, BackGround.rect)

    for event in PygameWrapper.game.event.get():
        if event.type == PygameWrapper.game.QUIT:
            playing = False

        if event.type == PygameWrapper.game.KEYDOWN:
            if event.key == PygameWrapper.game.K_LEFT:
                player_position_x_change = -1.7
            if event.key == PygameWrapper.game.K_RIGHT:
                player_position_x_change = 1.7
            if event.key == PygameWrapper.game.K_SPACE:


                # Fixing the change of direction of bullet
                if Bullet.state == 'carregada' and not PygameWrapper.current_game_status in (PygameWrapper.GAME_STATUS_OVER, PygameWrapper.GAME_STATUS_FINISHED) :
                    Bullet.position_x = Player.position_x 
                    PygameWrapper.screen.blit(Bullet.image, (Bullet.position_x, Bullet.position_y))
                    Bullet.state = 'disparada'
                    Bullet.sound.play()

        if event.type == PygameWrapper.game.KEYUP:
            player_position_x_change = 0

    Player.position_x += player_position_x_change

    for i in range(invaders_horde_size):
        invaders_horde[i].position_x += invader_position_x_change[i]

    # bullet movement
    if Bullet.position_y <= 0:
        Bullet.position_y = 600
        Bullet.state = "carregada"
    if Bullet.state == "disparada":
        PygameWrapper.screen.blit(Bullet.image, (Bullet.position_x, Bullet.position_y))
        Bullet.state = "disparada"
        Bullet.position_y -= bullet_position_y_change * 4

    # movement of the invader
    for i in range(invaders_horde_size):

        if PygameWrapper.current_game_status == PygameWrapper.GAME_STATUS_FINISHED:
             PygameWrapper.finished_game()
             break

        if invaders_horde[i].position_y >= 450:
            if abs(Player.position_x - invaders_horde[i].position_x) < 80:

                for j in range(invaders_horde_size):
                    invaders_horde[j].position_y = 2000
                    explosion_sound = PygameWrapper.game.mixer.Sound('data/explosion.wav')
                    explosion_sound.play()

                PygameWrapper.game_over()
                break

        if invaders_horde[i].position_x >= 735 or invaders_horde[i].position_x <= 0:
            invader_position_x_change[i] *= -1
            invaders_horde[i].position_y += invader_position_y_change[i]

        hasCollided = PygameWrapper.objectsCollided({'x': Bullet.position_x, 'y': Bullet.position_y}, {'x': invaders_horde[i].position_x, 'y': invaders_horde[i].position_y})

        if score <=3:
            Phase.current_phase = 1
        elif score <=4:
            Phase.current_phase = 2
        elif score <=5:
            Phase.current_phase = 3
        else:
            Phase.current_phase = 4

        if hasCollided:
            if Phase.current_phase ==3:
                score +=4
            elif Phase.current_phase ==4:
                score +=8
            else:
                score +=1
            if not Phase.change_phase(score):
                PygameWrapper.finished_game()
                break

            Bullet.position_y = 600
            Bullet.state = "carregada"
            
            invaders_horde[i].generate_new_position()
            invader_position_x_change[i] *= -1

        PygameWrapper.screen.blit(invaders_horde[i].image, (invaders_horde[i].position_x, invaders_horde[i].position_y))

    # restricting the spaceship so that
    # it doesn't go out of screen
    Player.restrict_player_moviment()

    PygameWrapper.screen.blit(Player.playerImage, (Player.position_x - 16, Player.position_y + 10))

    PygameWrapper.display_info_on_screen("Pontos: " + str(score), (5, 5))
    PygameWrapper.display_info_on_screen("Level: " + str(Phase.current_phase), (720, 5))
    PygameWrapper.game.display.update()