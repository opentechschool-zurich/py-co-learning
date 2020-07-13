import pygame

pygame.init()

screen = pygame.display.set_mode((400, 300))

pygame.mixer.init()

MUSIC_END = pygame.USEREVENT + 1
pygame.mixer.music.set_endevent(MUSIC_END)

def main():
    cat_sound = pygame.mixer.Sound('cat.ogg')


    music_playing = False

    while True:
        for event in pygame.event.get():
            if event.type == MUSIC_END:
                music_playing = False
            if event.type == pygame.QUIT:
                return
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    pygame.quit()
                    return
                elif event.key == pygame.K_a:
                    pygame.mixer.Sound.play(cat_sound)
                elif event.key == pygame.K_b:
                    if not music_playing:
                        music_playing = True
                        pygame.mixer.music.load('marbles.ogg')
                        pygame.mixer.music.play()
                elif event.key == pygame.K_c:
                    music_playing = False
                    pygame.mixer.music.stop()

if __name__ == "__main__":
    main()
