from cgitb import text
import pygame
from sys import exit
from random import randint

def display_score():
    current_time = int(pygame.time.get_ticks() / 1000) - start_time
    score_surf = text_font.render(f'Score: {current_time}', False, (64,64,64))
    score_rect = score_surf.get_rect(center = (400, 50))
    screen.blit(score_surf,score_rect)
    return current_time

def obstacle_movement(obstacle_list):
    if obstacle_list:
        for obstacle_rect in obstacle_list:
            obstacle_rect.x -= 5

            if obstacle_rect.bottom == 300: screen.blit(snail_surf,obstacle_rect)
            else: screen.blit(fly_surf,obstacle_rect)
        
        obstacle_list = [obstacle for obstacle in obstacle_list if obstacle.x > -100]
        
        return obstacle_list
    else: return []

def collisions (player,obstacles):
    if obstacles:
        for obstacle_rect in obstacles:
            if player.colliderect(obstacle_rect): return False
    return True

def player_animation():
    global player_surf, player_index

    if player_rect.bottom < 300:
        player_surf = player_jump
    else:
        player_index += 0.1
        if player_index <1:
            player_surf = player_walk_1
        else:
            player_surf = player_walk_2
            if player_index >2: player_index = 0


pygame.init()
score = 0     
screen = pygame.display.set_mode((800,400))
pygame.display.set_caption('Python Runner')
clock = pygame.time.Clock()
text_font = pygame.font.Font('Assets/font/Pixeltype.ttf',50)
game_active = False
start_time = 0

# Background surfaces
bg1_surface = pygame.image.load('Assets\graphics\BG\Bg1.png').convert_alpha()
bg1_x_pos = 0 
bg2_surface = pygame.image.load('Assets\graphics\BG\Bg2.png').convert_alpha()
bg2_x_pos = 0
bg3_surface = pygame.image.load('Assets\graphics\BG\Bg3.png').convert_alpha()
ground_surface = pygame.image.load('Assets\graphics\ground.png').convert()
ground_x_pos = 0

# Textos
#score_surf = text_font.render('Meu Jogo', False, (64,64,64))


# Obstaculos
snail_frame_1 = pygame.image.load('Assets\graphics\snail\snail1.png').convert_alpha()
snail_frame_2 = pygame.image.load('Assets\graphics\snail\snail2.png').convert_alpha()
snail_frames = [snail_frame_1,snail_frame_2]
snail_index = 0
snail_surf = snail_frames[snail_index]

fly_frame_1 = pygame.image.load('Assets\graphics\Fly\Fly1.png').convert_alpha()
fly_frame_2 = pygame.image.load('Assets\graphics\Fly\Fly2.png').convert_alpha()
fly_frames = [fly_frame_1,fly_frame_2]
fly_index = 0
fly_surf = fly_frames[fly_index]

obstacle_rect_list = []

# Player
player_walk_1 = pygame.image.load('Assets\graphics\player\player_walk_1.png').convert_alpha()
player_walk_2 = pygame.image.load('Assets\graphics\player\player_walk_2.png').convert_alpha()
player_walk = [player_walk_1, player_walk_2]
player_index = 0
player_jump =  pygame.image.load('Assets\graphics\player\jump.png').convert_alpha()

player_surf = player_walk[player_index]
player_rect = player_surf.get_rect(midbottom = (80,300))
player_g = 0

jump_sound = pygame.mixer.Sound('Assets\Audio\jump.mp3')
jump_sound.set_volume(0.2)

bg_music = pygame.mixer.Sound('Assets\Audio\music.mp3')
bg_music.set_volume(0.4)
bg_music_c = False

# Menu
player_stand = pygame.image.load('Assets\graphics\player\player_stand.png').convert_alpha()
player_stand = pygame.transform.scale2x(player_stand)
player_stand_rect = player_stand.get_rect(center = (400,200))

game_name = text_font.render('Pyhton Runner',False,(111,196,169))
game_name_rect = game_name.get_rect(center = (400,50))

game_msg = text_font.render('Press space to run',False,(111,196,169))
game_msg_rect = game_msg.get_rect(center = (400,350))

# Timer
obstacle_timer = pygame.USEREVENT + 1
pygame.time.set_timer(obstacle_timer, 1500)

snail_animation_timer = pygame.USEREVENT + 2
pygame.time.set_timer(snail_animation_timer, 500)

fly_animation_timer = pygame.USEREVENT + 2
pygame.time.set_timer(fly_animation_timer, 200)




while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()

        if game_active:

            # Inputs
            if bg_music_c:
                bg_music.play(loops = -1)
                bg_music_c = False
            if event.type == pygame.MOUSEBUTTONDOWN:
                if player_rect.bottom == 300: player_g = -20

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE and player_rect.bottom == 300:
                    player_g = -21
                    jump_sound.play()
            
            # Eventos
            if event.type == obstacle_timer:
                if randint(0,2):
                    obstacle_rect_list.append(snail_surf.get_rect(bottomright = (randint(900,1100),300)))
                else:
                    obstacle_rect_list.append(fly_surf.get_rect(bottomright = (randint(900,1100),200)))
            
            if event.type == snail_animation_timer:
                if snail_index == 0: snail_index = 1
                else: snail_index = 0
                snail_surf = snail_frames[snail_index]

            if event.type == fly_animation_timer:
                if fly_index == 0: fly_index = 1
                else: fly_index = 0
                fly_surf = fly_frames[fly_index]


        else:
            if event.type == pygame.KEYDOWN and event.key == pygame.K_SPACE:
                game_active = True
                start_time = int(pygame.time.get_ticks()/1000)
                bg_music_c = True


    if game_active:
        # Elementos na tela
        

        screen.blit(bg3_surface,(0,0))

        screen.blit(bg2_surface,(bg2_x_pos,70))
        screen.blit(bg2_surface,(bg2_x_pos+800,70))
        bg2_x_pos += -0.5
        if bg2_x_pos < -800: bg2_x_pos = 0

        screen.blit(bg1_surface,(bg1_x_pos,120))
        screen.blit(bg1_surface,(bg1_x_pos+800,120))
        bg1_x_pos += -1.0
        if bg1_x_pos < -800: bg1_x_pos = 0


        screen.blit(ground_surface,(ground_x_pos,300))
        screen.blit(ground_surface,(ground_x_pos+800,300))
        ground_x_pos += -1.5
        if ground_x_pos <-800: ground_x_pos = 0

        score = display_score()

        # Player
        player_g += 1  #velocidade da gravidade
        player_rect.y += player_g
        if player_rect.bottom >= 300: player_rect.bottom = 300
        player_animation()
        screen.blit(player_surf,player_rect)

        # Obstaculos
        obstacle_rect_list = obstacle_movement(obstacle_rect_list)

        # Colisões
        game_active = collisions(player_rect,obstacle_rect_list)
        

    else:
        bg_music.stop()
        bg_music_c = True
        screen.fill((94,129,162))
        screen.blit(player_stand,player_stand_rect)
        obstacle_rect_list.clear()
        player_rect.midbottom = (80,300)
        player_g = 0

        score_msg = text_font.render(f'Your score: {score}',False,(111,196,169))
        score_msg_rect = score_msg.get_rect(center = (400,350))
        screen.blit(game_name,game_name_rect)

        if score == 0:
            screen.blit(game_msg, game_msg_rect)
        else:
            screen.blit(score_msg, score_msg_rect)




    pygame.display.update()
    clock.tick(60) #Framerate
