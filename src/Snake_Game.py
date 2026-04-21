import pygame
import random

class Snake():

    def __init__(self, pos = (0,0), length = 3):
        self.size = 20
        self.pos = pos
        self.length = length
        self.color = 'Green'

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

    # DOWN
    if direction == 1:
        snake_pos[1] += pixel_size
        print(snake_pos[1])

    # LEFT
    if direction == 2:
        snake_pos[0] -= pixel_size
        print(snake_pos[0])

    # RIGHT
    if direction == 3:
        snake_pos[0] += pixel_size
        print(snake_pos[0])

    return snake_pos

def create_Fruit(screen, resolution):
    location = []
    location = 20 * (random.randrange(0, resolution[0] // 20)), 20 * (random.randrange(1, resolution[1] // 20))
    print(location)
    pygame.draw.rect(screen, 'Red', (location[0], location[1], 20, 20))
    

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

       # screen.fill('Black')
        pygame.draw.rect(screen, s_color, (snake_pos[0], snake_pos[1], pixel_size, pixel_size))
        pygame.display.flip()
        dt = clock.tick(12)

        snake_pos = movement(snake_pos, pixel_size, direction)

        create_Fruit(screen, resolution)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False


            if event.type == pygame.KEYDOWN:
                #TODO: Move to its own function
                key = pygame.key.get_pressed()
                
                # Up
                if key[pygame.K_w] and direction != 1:
                    direction = 0
                
                # Down
                if key[pygame.K_s] and direction != 0:
                    direction = 1

                # Left
                if key[pygame.K_a] and direction != 3:
                    direction = 2

                # Right
                if key[pygame.K_d] and direction != 2:
                    direction = 3

        


        
    
    pygame.quit




if __name__ == "__main__":
    main()