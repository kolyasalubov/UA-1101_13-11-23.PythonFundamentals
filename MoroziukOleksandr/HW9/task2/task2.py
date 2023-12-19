import pygame

def main():
    # Ініціалізація Pygame
    pygame.init()

    # Створення вікна програми
    window = pygame.display.set_mode((640, 480))

    # Створення прямокутника
    rect = pygame.Rect(100, 100, 200, 100)

    # Основний цикл програми
    while True:
        # Обробка подій
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

        # Перемальовування вікна
        window.fill((0, 0, 0))
        pygame.draw.rect(window, (255, 0, 0), rect)
        pygame.display.update()

    # Обмеження координат прямокутника
    rect.x = max(0, rect.x)
    rect.y = max(0, rect.y)
    rect.x = min(window.get_width() - rect.w, rect.x)
    rect.y = min(window.get_height() - rect.h, rect.y)

if __name__ == "__main__":
    main()
