import pygame

class Snake():

    def __init__(self, pos = (0,0)):
        size = 20
        pos = pos
        color = 'Green'

class SnakeTrail():
    print()

def movement(snake_pos, pixel_size, up, right, down, left):
    # Updates Position of snake
    if up:
        snake_pos[1] -= pixel_size
        print(snake_pos[1])

    if right:
        snake_pos[0] += pixel_size
        print(snake_pos[0])

    if down:
        snake_pos[1] += pixel_size
        print(snake_pos[1])

    if left:
        snake_pos[0] -= pixel_size
        print(snake_pos[0])

    return snake_pos

def main():
    pygame.init()
    pygame.display.set_caption("Snake")

    resolution = (800, 800)

    screen = pygame.display.set_mode(resolution)
    
    pixel_size = 20
    snake_pos = [resolution[0]//2,resolution[1]//2]
    s_color = 'Green'

    snake = snake_pos

    running = True
    
    # Player movement direction
    up = False
    right = False
    down = False
    left = False

    while running:

        screen.fill('Black')
        pygame.draw.rect(screen, s_color, (snake_pos[0], snake_pos[1], pixel_size, pixel_size))
        pygame.display.flip()

        snake_pos = movement(snake_pos, pixel_size, up, right, down, left)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False


            if event.type == pygame.KEYDOWN:
                #TODO: fix diagonal movement via multiple inputs
                #      Move to its own function
                key = pygame.key.get_pressed()
                
                # Up
                if key[pygame.K_w]:
                    up, right, down, left = True, False, False, False
                
                # Down
                if key[pygame.K_s]:
                    up, right, down, left = False, False, True, False
                   # snake_pos = movement(snake_pos, pixel_size, up, right, down, left)

                # Left
                if key[pygame.K_a]:
                    up, right, down, left = False, False, False, True
                   # snake_pos = movement(snake_pos, pixel_size, up, right, down, left)

                # Right
                if key[pygame.K_d]:
                    up, right, down, left = False, True, False, False
                   # snake_pos = movement(snake_pos, pixel_size, up, right, down, left)

        


        
    
    pygame.quit




if __name__ == "__main__":
    main()