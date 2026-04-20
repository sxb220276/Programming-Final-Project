import pygame
import random

class Snake():

    def __init__(self, pos = (0,0), length = 3):
        size = 20
        pos = pos
        length = length
        color = 'Green'

    def update_snake():
        # Would update snake on surface
        print()

class SnakeTrail():
    print()

def movement(snake_pos, pixel_size, direction):
    # Updates Position of snake
    #TODO: disable opposite turns; EX going forward then suddenly back
    #if first_init:

    # UP
    if direction == 0:
        snake_pos[1] -= pixel_size
        print(snake_pos[1])
        can_down = False
        can_left, can_right = True, True
        
    # DOWN
    if direction == 1:
        snake_pos[1] += pixel_size
        print(snake_pos[1])
        can_up = False
        can_right, can_left = True, True

    # LEFT
    if direction == 2:
        snake_pos[0] -= pixel_size
        print(snake_pos[0])
        can_right = False
        can_up, can_down = True, True

    # RIGHT
    if direction == 3:
        snake_pos[0] += pixel_size
        print(snake_pos[0])
        can_left = False
        can_up, can_down = True, True

    return snake_pos

def main():
    pygame.init()
    pygame.display.set_caption("Snake")
    clock = pygame.time.Clock()

    resolution = (800, 800)

    screen = pygame.display.set_mode(resolution)
    
    pixel_size = 20
    snake_pos = [resolution[0]//2,resolution[1]//2]
    s_color = 'Green'

    snake = snake_pos

    running = True
    
    # Player movement direction
    direction = None

    while running:

        screen.fill('Black')
        pygame.draw.rect(screen, s_color, (snake_pos[0], snake_pos[1], pixel_size, pixel_size))
        pygame.display.flip()
        dt = clock.tick(12)

        snake_pos = movement(snake_pos, pixel_size, direction)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False


            if event.type == pygame.KEYDOWN:
                #TODO: Move to its own function
                key = pygame.key.get_pressed()
                
                # Up
                if key[pygame.K_w]:
                    direction = 0
                
                # Down
                if key[pygame.K_s]:
                    direction = 1

                # Left
                if key[pygame.K_a]:
                    direction = 2

                # Right
                if key[pygame.K_d]:
                    direction = 3

        


        
    
    pygame.quit




if __name__ == "__main__":
    main()