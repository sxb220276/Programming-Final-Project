import pygame

class Snake():

    def __init__(self, pos = (0,0)):
        size = 20
        pos = pos
        color = 'Green'

class SnakeTrail():
    print()

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

    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False


            if event.type == pygame.KEYDOWN:
                #TODO: fix diagonal movement via multiple inputs
                #      Move to its own function
                key = pygame.key.get_pressed()
                if key[pygame.K_w]:
                    snake_pos[1] -= pixel_size
                
                if key[pygame.K_s]:
                    snake_pos[1] += pixel_size

                if key[pygame.K_a]:
                    snake_pos[0] -= pixel_size

                if key[pygame.K_d]:
                    snake_pos[0] += pixel_size

        screen.fill('Black')
        pygame.draw.rect(screen, s_color, (snake_pos[0], snake_pos[1], pixel_size, pixel_size))
        pygame.display.flip()


        
    
    pygame.quit




if __name__ == "__main__":
    main()