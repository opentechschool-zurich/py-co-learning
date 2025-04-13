import pygame

pygame.init()

screen = pygame.display.set_mode((400, 400))
pygame.display.set_caption("Alien")

color = pygame.Color('yellow')


done = False
while not done:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                done = True

    screen.fill(color)

    pygame.draw.ellipse(screen, 'green', (100, 150, 200, 100)) # body
    pygame.draw.circle(screen, 'white', (200, 100), 30) # eye
    pygame.draw.circle(screen, 'black', (200, 100), 10) # pupil
    pygame.draw.ellipse(screen, 'red', (150, 220, 100, 20)) # mouth
    pygame.draw.line(screen, 'black', (200, 150), (200, 130), 10) # neck
    pygame.draw.polygon(screen, 'blue', ((160, 75), (240, 75), (200, 20)))

    pygame.display.flip()

pygame.quit()
