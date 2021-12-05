import pygame

pygame.init()

WIDTH, HEIGHT = 1200, 700
WINDOW = pygame.display.set_mode((WIDTH, HEIGHT))

pygame.display.set_caption("Backgammon!")

ICON = pygame.image.load("assets/icon.png")
pygame.display.set_icon(ICON)

BACKGROUND = pygame.image.load("assets/background.jpg")
WINDOW.blit(BACKGROUND, [0,0])

SOUND = pygame.mixer.Sound("assets/music.mp3")
pygame.mixer.Sound.play(SOUND)

def main():
    run = True
    while run:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                print("Bye bye!")
                run = False
        pygame.display.flip()
    pygame.quit()


if __name__ == "__main__":
    main()











