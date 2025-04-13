import pygame

pygame.init()

screen = pygame.display.set_mode((400, 400))
pygame.display.set_caption("Alien")

done = False
while not done:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                done = True

    screen.fill('yellow')
    pygame.display.flip()

pygame.quit()
