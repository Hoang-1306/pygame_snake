import pygame
import time
import random
# constans
WIDTH: int = 800
HEIGHT: int = 600

SNAKE_BLOCK: int = 10
SNAKE_SPEED: int = 30

SCREEN_SIZE: tuple = (WIDTH, HEIGHT)
WHITE: tuple = (255, 255, 255)
BLUE: tuple = (0, 0, 255)
BLACK: tuple = (0, 0, 0)
GREEN: tuple = (0, 255, 0)
RED: tuple = (255, 0, 0)

# RECT = [WIDTH/2, HEIGHT/2, 10, 10]

def message(msg, color):
    mesg = FONT_STYLE.render(msg, True, color)
    display.blit(mesg, [WIDTH/6, HEIGHT/3])
def your_score(score):
    value = SCORE_FONT.render("You Score: " + str(score), True, RED)
    display.blit(value, [0, 0])

def our_snake(snake_block, snake_list):
    for x in snake_list:
        pygame.draw.rect(display, BLACK, [x[0], x[1], snake_block, snake_block])
def game_loop():
    GAME_OVER = False
    GAME_CLOSE = False
    
    x1: int = WIDTH/2
    y1: int = HEIGHT/2
    
    x1_change = 0
    y1_change = 0
    
    snake_list = []
    length_of_snake = 1
    
    FOODX = round(random.randrange(0, WIDTH - SNAKE_BLOCK)/10.0) * 10.0
    FOODY = round(random.randrange(0, HEIGHT - SNAKE_BLOCK)/10.0) * 10.0
    # game loop
    while not GAME_OVER:
        
        
        while GAME_CLOSE == True:
            display.fill(BLUE)
            message("You Lost! Press Q-Quit or C-Play Again", RED)
            your_score(length_of_snake - 1)
            pygame.display.update()
            
            for event in pygame.event.get():
                if event.type == pygame.KEYDOWN:
                    if event.type == pygame.QUIT:
                        GAME_OVER = True
                    if event.key == pygame.K_q:
                        GAME_OVER = True
                        GAME_CLOSE = False
                    if event.key == pygame.K_c:
                        # GAME_OVER = True
                        game_loop()
                                    
        for event in pygame.event.get():
            print(event)
            if event.type == pygame.QUIT:
                GAME_OVER = True

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    x1_change -= SNAKE_BLOCK
                    y1_change = 0

                elif event.key == pygame.K_RIGHT:
                    x1_change = SNAKE_BLOCK
                    y1_change = 0

                elif event.key == pygame.K_UP:
                    y1_change -= SNAKE_BLOCK
                    x1_change = 0

                elif event.key == pygame.K_DOWN:
                    y1_change = SNAKE_BLOCK
                    x1_change = 0

        if x1 >= WIDTH or x1 < 0 or y1 >= HEIGHT or y1 < 0:
            GAME_CLOSE = True
        
        x1 += x1_change
        y1 += y1_change
        display.fill(WHITE)
        pygame.draw.rect(display, GREEN, [FOODX, FOODY, SNAKE_BLOCK, SNAKE_BLOCK])
        
        # pygame.draw.rect(display, BLACK,  [x1, y1, SNAKE_BLOCK, SNAKE_BLOCK])
        snake_head = []
        snake_head.append(x1)
        snake_head.append(y1)
        snake_list.append(snake_head)
        
        if len(snake_list) > length_of_snake:
            del snake_list[0]
        for x in snake_list[:-1]:
            if x == snake_head:
                GAME_CLOSE = True
                
        our_snake(SNAKE_BLOCK, snake_list)
        your_score(length_of_snake - 1)
        
        pygame.display.update()
        
        if x1 == FOODX and y1 == FOODY:
            FOODX = round(random.randrange(0, WIDTH - SNAKE_BLOCK)/10.0) * 10.0
            FOODY = round(random.randrange(0, HEIGHT - SNAKE_BLOCK)/10.0) * 10.0
            length_of_snake += 1
            # print("Yummy!")
        
        clock.tick(SNAKE_SPEED)
    # message("Game over", RED)
    # pygame.display.update()
    # time.sleep(3)
        # pygame.quit()
    pygame.quit()
    quit()
if __name__ == "__main__":
    # initialize pygame
    pygame.init()
    clock = pygame.time.Clock()
    display = pygame.display.set_mode(SCREEN_SIZE)
    # pygame.display.update()
    pygame.display.set_caption('Snake game by Hoang-mata')

    FONT_STYLE = pygame.font.SysFont("bahnschrift", 40)
    SCORE_FONT = pygame.font.SysFont("comicsansms", 50)
    game_loop()
    pygame.quit()
    quit()