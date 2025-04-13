import pygame

pygame.init()

screen = pygame.display.set_mode((400, 400))
pygame.display.set_caption("Alien")

color = pygame.Color('yellow')

eye_open = True
mouth_open = True

done = False
while not done:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                done = True
            elif event.key == pygame.K_a:
                eye_open = True
            elif event.key == pygame.K_z:
                eye_open = False
            elif event.key == pygame.K_b:
                mouth_open = True
            elif event.key == pygame.K_o:
                mouth_open = False

    if eye_open:
        eye_color = 'white'
    else:
        eye_color = 'green'
    if mouth_open:
        mouth_color = 'red'
    else:
        mouth_color = 'black'

    screen.fill(color)

    pygame.draw.ellipse(screen, 'green', (100, 150, 200, 100)) # body
    pygame.draw.circle(screen, eye_color, (200, 100), 30) # eye
    if eye_open:
        pygame.draw.circle(screen, 'black', (200, 100), 10) # pupil
    pygame.draw.ellipse(screen, mouth_color, (150, 220, 100, 20)) # mouth
    pygame.draw.line(screen, 'black', (200, 150), (200, 130), 10) # neck
    pygame.draw.polygon(screen, 'blue', ((160, 75), (240, 75), (200, 20)))

    pygame.display.flip()

pygame.quit()
