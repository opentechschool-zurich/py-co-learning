import pygame

pygame.init()

screen = pygame.display.set_mode((400, 300))

pygame.mixer.init()

def main():
    cat_sound = pygame.mixer.Sound('cat.ogg')

    while True:
        for event in pygame.event.get():
            print('.')
            if event.type == pygame.QUIT:
                return
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    pygame.quit()
                    return
                elif event.key == pygame.K_a:
                    pygame.mixer.Sound.play(cat_sound)

if __name__ == "__main__":
    main()
