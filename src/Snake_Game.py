import pygame
import random

class SnakeBit():

    def __init__(self, pos, screen):
        self.size = 20
        self.pos = pos
        self.color = 'Green'
        self.screen = screen

    def draw_snake(self):
        # Would update snake on surface
        pygame.draw.rect(self.screen, self.color, (self.pos[0], self.pos[1], self.size, self.size))
        print(self.pos)

class SnakeTrail():
    #TODO: Create function that updates all bits within snake_body list
    
    def __init__(self, pos, screen, length):
        self.pos = pos
        self.screen = screen
        self.length = length
        self.snake_body = []

    #creates individual parts of snakes and stores to back of list
    #TODO: add loop to create all needed parts
    #      Need to make a function that adds a bit on scoring fruit

    def create_bits(self):
        bit = SnakeBit(self.pos, self.screen)
        self.snake_body.insert(-1, bit)
    
    # draws bits inside of list
    def draw_bits(self):
        for idx in self.snake_body:
            idx.draw_snake()

def movement(snake_pos, pixel_size, direction):
    # Updates Position of snake

    # UP
    if direction == 0:
        snake_pos[1] -= pixel_size
        #print(snake_pos[1])

    # DOWN
    if direction == 1:
        snake_pos[1] += pixel_size
        #print(snake_pos[1])

    # LEFT
    if direction == 2:
        snake_pos[0] -= pixel_size
        #print(snake_pos[0])

    # RIGHT
    if direction == 3:
        snake_pos[0] += pixel_size
        #print(snake_pos[0])

def create_Fruit(screen, resolution):
    #works, just gets removed by screen.fill
    #TODO: need to make a fruit class :/
    location = []
    location = 20 * (random.randrange(0, resolution[0] // 20)), 20 * (random.randrange(1, resolution[1] // 20))
    #print(location)
    pygame.draw.rect(screen, 'Red', (location[0], location[1], 20, 20))
    

def main():
    pygame.init()
    pygame.display.set_caption("Snake")
    clock = pygame.time.Clock()

    resolution = (800, 800)

    screen = pygame.display.set_mode(resolution)
    
    pixel_size = 20
    snake_pos = [resolution[0]//2,resolution[1]//2]
    snake = SnakeTrail(snake_pos, screen, 4)
    #all bits are created by Snake_Trail calling Snake bit from inside class functions
    snake.create_bits()
    


    running = True
    
    # Player movement direction
    direction = None

    while running:

        screen.fill('Black')
        snake.draw_bits()
        pygame.display.flip()
        dt = clock.tick(12)

        movement(snake_pos, pixel_size, direction)

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