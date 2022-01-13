import pygame
# constans
WIDTH: int = 800
HEIGHT: int = 600

x1: int = WIDTH/2
y1: int = HEIGHT/2

x1_change = 0
y1_change = 0

GAME_OVER = False

SCREEN_SIZE: tuple = (WIDTH, HEIGHT)
WHITE: tuple = (255, 255, 255)
BLUE: tuple = (0, 0, 255)
BLACK: tuple = (0, 0, 0)
RED: tuple = (255, 0, 0)

# RECT = [WIDTH/2, HEIGHT/2, 10, 10]



if __name__ == "__main__":
    # initialize pygame
    pygame.init()

    display = pygame.display.set_mode(SCREEN_SIZE)
    # pygame.display.update()
    pygame.display.set_caption('Snake game by Hoang-mata')


    # for loop
    clock = pygame.time.Clock()

    while not GAME_OVER:
        for event in pygame.event.get():
            # print(event)
            if event.type == pygame.QUIT:
                GAME_OVER = True
                
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    x1_change = -10
                    y1_change = 0
                    
                elif event.key == pygame.K_RIGHT:
                    x1_change = 10
                    y1_change = 0
                    
                elif event.key == pygame.K_UP:
                    y1_change = -10
                    x1_change = 0
                    
                elif event.key == pygame.K_DOWN:
                    y1_change = 10
                    x1_change = 0
        
        x1 += x1_change
        y1 += y1_change
        display.fill(WHITE)
        pygame.draw.rect(display, BLACK,  [x1, y1, 10, 10])
        pygame.display.update()
        clock.tick((60))
        
    pygame.quit()
    quit()  