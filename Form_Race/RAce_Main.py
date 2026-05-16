import math
from pygame.constants import  *
from random import choice, randint
from All_colors import *
import pygame

pygame.init()

def distance(p1, p2):
    return math.sqrt((p2[0] - p1[0]) ** 2 + (p2[1] - p1[1]) ** 2)

info = pygame.display.Info()
size = (800, 600)
screen = pygame.display.set_mode(size)
pygame.display.set_caption('Моя игра')
BACKGROUND = BLACK
screen.fill(BACKGROUND)
pygame.display.flip()

CIRCLE_COLOR = WHITE
background_image = pygame.image.load('Road_Of_Race.jpg')
background_rect1 = background_image.get_rect()
background_rect2 = background_image.get_rect()
background_rect2.x = background_rect1.width
car = pygame.image.load('Car.png')
enemy_car = pygame.image.load('Enemy_car.png')
circle_pos = (320, 240)
angle = 20
speed = 2

dist = 0
max_distance = 500
max_speed = 5
min_speed = 3

fps = 60

clock = pygame.time.Clock()

vx_bg = 0
is_shift = False
is_slow_down = False

minecraft_font = pygame.font.Font('../minecraft.ttf', 32)
minecraft_timer_font = pygame.font.Font('../minecraft.ttf', 50)
minecraft_win_font = pygame.font.Font('../minecraft.ttf', 100)

score = 0
timer = 0
timer_tick = 0

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.KEYUP:
            if event.key == pygame.K_LSHIFT:
                is_shift = False
            elif event.key == pygame.K_SPACE:
                is_slow_down = False

    keys = pygame.key.get_pressed()

    if keys[pygame.K_LSHIFT]:
        is_shift = True
        vx_bg -= 0.05
    elif keys[pygame.K_SPACE]:
        is_slow_down = True
        if vx_bg < 0:
            vx_bg += 0.1

    if vx_bg < 0:
        if is_shift == False and is_slow_down == False:
            vx_bg += 0.03

    timer_tick += 1
    timer = timer_tick // 60
    help_text = minecraft_font.render('Left Shift - газ', True, WHITE)
    help_text2 = minecraft_font.render('Space - тормоз', True, WHITE)
    timer_text = minecraft_timer_font.render(f'Время: {timer}', True, RED, GRAY)
    my_text = minecraft_font.render(f'Скорость: {-((vx_bg * 3) // 1)} км/ч', True, WHITE, GRAY)
    score_text = minecraft_font.render(f'Осталось км: {100 - score}', True, YELLOW, GRAY)
    win_text = minecraft_win_font.render(f'Вы победили!', True, GREEN, GRAY)
    win_text.set_alpha(0)

    # print(vx_bg)
    background_rect1.x += vx_bg
    background_rect2.x += vx_bg

    if background_rect1.right <= 0:
        background_rect1.left = background_rect2.right
        score += 1

    if background_rect2.right <= 0:
        background_rect2.left = background_rect1.right
        score += 1

    mouse_pos = pygame.mouse.get_pos()
    if vx_bg != 0 or vx_bg < 0:
        dx = mouse_pos[0] - circle_pos[0]
        dy = mouse_pos[1] - circle_pos[1]
        angle = math.degrees(math.atan2(dy, dx))

        dist = distance(mouse_pos, circle_pos)
        speed = max_speed - (dist/max_distance) * (max_speed - min_speed)
        dx = speed * math.cos(math.radians(angle))
        dy = speed * math.sin(math.radians(angle))
        circle_pos = (circle_pos[0], circle_pos[1] + dy)


    # if vx_bg <= -84:
    #     vx_bg = -84

    #  Чтобы установить скорость есть вот эта формула : Скорость / -3
    # if vx_bg <= -41:
    #     vx_bg = -41

    enemy_speeds = [-5, -3, -1, 0.1, 1]
    enemy_positions = [(600, 177, 150, 100), (600, 300, 150, 100), (600, 243, 150, 100)]
    enemy_rect = (600, 177, 150, 100)
    if enemy_rect[0] < 0:
        enemy_rect = choice(enemy_positions)
    enemy_pos = (enemy_rect[0] + (vx_bg * (choice(enemy_speeds))), enemy_rect[1])

    if score >= 100:
        win_text.set_alpha(255)

    # Отрисовка объектов
    screen.fill(BACKGROUND)
    screen.blit(background_image, background_rect1)
    screen.blit(background_image, background_rect2)
    rotated_car = pygame.transform.rotate(car, -angle)
    rotated_car_rect = rotated_car.get_rect()
    rotated_car_rect.center = circle_pos
    enemy_car_rect = enemy_rect
    if rotated_car_rect.y <= 170:
        rotated_car_rect.y = 170
    elif rotated_car_rect.y >= 300:
        rotated_car_rect.y = 300
    screen.blit(rotated_car, rotated_car_rect)

    # screen.blit(enemy_car, enemy_car_rect)
    screen.blit(my_text, (0, 10))
    screen.blit(score_text, (0, 60))
    screen.blit(timer_text, (0, 550))
    screen.blit(win_text, (0, 0))
    screen.blit(help_text, (500, 500))
    screen.blit(help_text2, (500, 550))


    pygame.display.flip()
    clock.tick(fps)

pygame.quit()



# import math
# import pygame
# from pygame.constants import *
# from random import choice
# from All_colors import *
#
# pygame.init()
#
# def distance(p1, p2):
#     return math.sqrt((p2[0] - p1[0]) ** 2 + (p2[1] - p1[1]) ** 2)
#
# size = (800, 600)
# screen = pygame.display.set_mode(size)
# pygame.display.set_caption('Моя игра')
# BACKGROUND = BLACK
#
# # Загружаем изображения
# background_image = pygame.image.load('Road_Of_Race.jpg')
# background_rect1 = background_image.get_rect()
# background_rect2 = background_image.get_rect()
# background_rect2.x = background_rect1.width
#
#
# car = pygame.image.load('Car.png')
# enemy_car = pygame.image.load('Enemy_car.png')
#
# # Начальная позиция врага
# enemy_pos = [600, 243]  # Один враг в средней полосе
# enemy_base_speed = -3  # Скорость врага
#
# circle_pos = [320, 240]
# angle = 20
# speed = 2
#
# dist = 0
# max_distance = 500
# max_speed = 5
# min_speed = 3
#
# fps = 60
# clock = pygame.time.Clock()
#
# vx_bg = 0
# is_shift = False
# is_slow_down = False
#
# minecraft_font = pygame.font.Font('../minecraft.ttf', 32)
# minecraft_win_font = pygame.font.Font('../minecraft.ttf', 100)
#
# score = 0
#
# running = True
# while running:
#     for event in pygame.event.get():
#         if event.type == pygame.QUIT:
#             running = False
#         elif event.type == pygame.KEYUP:
#             if event.key == pygame.K_LSHIFT:
#                 is_shift = False
#             elif event.key == pygame.K_SPACE:
#                 is_slow_down = False
#
#     keys = pygame.key.get_pressed()
#
#     if keys[pygame.K_LSHIFT]:
#         is_shift = True
#         vx_bg -= 0.05
#     elif keys[pygame.K_SPACE]:
#         is_slow_down = True
#         if vx_bg < 0:
#             vx_bg += 0.1
#
#     if vx_bg < 0:
#         if not is_shift and not is_slow_down:
#             vx_bg += 0.03
#
#     # Обновляем позицию врага (независимо от vx_bg)
#     enemy_pos[0] += enemy_base_speed + choice([-0.2, 0, 0.2])  # Небольшая случайность
#
#     # Если враг ушёл за экран, возвращаем его назад
#     if enemy_pos[0] < -150:
#         enemy_pos[0] = 800
#
#     my_text = minecraft_font.render(f'Скорость: {-((vx_bg * 3) // 1)} км/ч', True, WHITE, GRAY)
#     score_text = minecraft_font.render(f'Осталось км: {100 - score}', True, YELLOW, GRAY)
#     win_text = minecraft_win_font.render(f'Вы победили!', True, GREEN, GRAY)
#     win_text.set_alpha(0)
#
#     background_rect1.x += vx_bg
#     background_rect2.x += vx_bg
#
#     if background_rect1.right <= 0:
#         background_rect1.left = background_rect2.right
#         score += 1
#
#     if background_rect2.right <= 0:
#         background_rect2.left = background_rect1.right
#         score += 1
#
#     mouse_pos = pygame.mouse.get_pos()
#     if vx_bg != 0 or vx_bg < 0:
#         dx = mouse_pos[0] - circle_pos[0]
#         dy = mouse_pos[1] - circle_pos[1]
#         angle = math.degrees(math.atan2(dy, dx))
#
#         dist = distance(mouse_pos, circle_pos)
#         speed = max_speed - (dist / max_distance) * (max_speed - min_speed)
#         dx_car = speed * math.cos(math.radians(angle))
#         dy_car = speed * math.sin(math.radians(angle))
#
#         # Создаём хитбоксы для проверки столкновений
#         player_rect = pygame.Rect(circle_pos[0] - 75, circle_pos[1] - 50, 150, 100)
#         enemy_rect = pygame.Rect(enemy_pos[0], enemy_pos[1], 150, 100)
#
#         # Проверяем столкновение ДО движения
#         future_player_y = circle_pos[1] + dy_car
#         future_player_rect = pygame.Rect(
#             circle_pos[0] - 75,
#             future_player_y - 50,
#             150,
#             100
#         )
#
#         collision_detected = future_player_rect.colliderect(enemy_rect)
#
#         # Двигаем игрока только если нет столкновения
#         if not collision_detected:
#             # Дополнительно проверяем границы экрана
#             new_y = circle_pos[1] + dy_car
#             if 170 <= new_y <= 300:  # Ограничение по вертикали
#                 circle_pos[1] = new_y
#
#     if vx_bg <= -41:
#         vx_bg = -41
#
#     if score >= 100:
#         win_text.set_alpha(255)
#
#     # Отрисовка объектов
#     screen.fill(BACKGROUND)
#     screen.blit(background_image, background_rect1)
#     screen.blit(background_image, background_rect2)
#
#     # Рисуем машину игрока
#     rotated_car = pygame.transform.rotate(car, -angle)
#     rotated_car_rect = rotated_car.get_rect()
#     rotated_car_rect.center = circle_pos
#     screen.blit(rotated_car, rotated_car_rect)
#
#     # Рисуем врага
#     screen.blit(enemy_car, enemy_pos)
#
#     screen.blit(my_text, (0, 10))
#     screen.blit(score_text, (0, 60))
#     screen.blit(win_text, (0, 0))
#
#     pygame.display.flip()
#     clock.tick(fps)
#
# pygame.quit()