import math

import pygame

pygame.init()
screen_width = 640
screen_height = 480
screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption("Draw a perfect circle")
clock = pygame.time.Clock()
circle_center = (screen_width // 2, screen_height // 2)
circle_radius = min(screen_width, screen_height) // 100
circle_color = (255, 0, 0)
pygame.draw.circle(screen, circle_color, circle_center, circle_radius, 2)
loop = True
press = False
quality_threshold = 90
while loop:
    try:
        # pygame.mouse.set_visible(False)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                loop = False

        px, py = pygame.mouse.get_pos()
        color = (255, 255,255)

        curr_pos = pygame.mouse.get_pos()
        distance = math.dist(curr_pos, circle_center)

        if distance < circle_radius + 10:
            print("Too close to circle!")
            color = (255, 0, 0)
        elif distance < circle_radius+45:
            color = (255,255,0)
        elif distance < circle_radius+ 35:
            color = (255,255,102)
        else:
            color = (128, 255, 0)


        if event.type == pygame.MOUSEBUTTONUP:
            press == False
        if distance <= circle_radius:
            quality = 100
        else:
            quality = 100 - ((distance - circle_radius) / (screen_width / 2 - circle_radius) * 100)
        if quality < quality_threshold:
           color = (128, 255, 0)
        if pygame.mouse.get_pressed() == (1, 0, 0):
            pygame.draw.rect(screen, color, (px, py, 10, 10))

        pygame.display.update()
        clock.tick(1000)
    except Exception as e:
        print(e)
        pygame.quit()