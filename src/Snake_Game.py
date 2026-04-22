import pygame
import random

class SnakeBit():

    def __init__(self, screen, pos=(400, 400)):
        self.size = 20
        self.pos = pos
        self.color = 'Green'
        self.screen = screen

    def draw_snake(self):
        # Would update snake on surface
        pygame.draw.rect(self.screen, self.color, (self.pos[0], self.pos[1], self.size, self.size))
        #print(self.pos)

class SnakeTrail():
    #TODO: Create function that updates all bits within snake_body list
    
    def __init__(self, pos, screen, length):
        self.pos = pos
        self.screen = screen
        self.length = length
        self.snake_body = []

    #creates individual parts of snakes and stores to back of list
    #BUG: does not display all snake bits, 
    #     Snake bits all have same pos value causing them to overlap
    #TODO: Update and add bit on scoring a fruit

    def create_bits(self):
        for x in range(0, self.length):
            bit = SnakeBit(self.screen, self.pos)
            self.snake_body.insert(-1, bit)
    
    # draws bits inside of list
    def draw_bits(self):
        for idx, bit in enumerate(self.snake_body):
            #print(self.snake_body[idx].pos)
            bit.draw_snake()
    
    def _body_movement(self):
        #updates parts of the snake body
        #BUG: Currently updating all of them to have the same pos
        #     Each iteration just overwrites with the heads current location
        #     Logic is wrong, needs to update end of tail first
        for idx in range(self.length - 1, 0, -1):
            #print(idx)
            if idx != self.length - 1:
                self.snake_body[idx].pos = self.snake_body[idx - 1].pos
        #print(body_piece)
        #print(last_pos)
    
    def check_bounds(self, resolution):
        if self.snake_body[0].pos[0] > resolution[0] or self.snake_body[0].pos[0] < 0:
            return True
        
        if self.snake_body[0].pos[1] > resolution[1] or self.snake_body[0].pos[1] < 0:
            return True
        
        return False
            
    
    def movement(self, direction):
        # Updates Position of bit
        head = self.snake_body[0]
        #print(last_pos)
        # UP
        if direction == 0:
            head.pos[1] -= 20
            #print(snake_pos[1])

        # DOWN
        if direction == 1:
            head.pos[1] += 20
            #print(snake_pos[1])

        # LEFT
        if direction == 2:
            head.pos[0] -= 20
            #print(snake_pos[0])

        # RIGHT
        if direction == 3:
            head.pos[0] += 20

        self._body_movement()
            #print(idx)
            #print(last_pos)


class Fruit():

    def __init__(self, screen, resolution):
        self.screen = screen
        self.resolution = resolution
        self.size = 20
        self.score = 0
        self.pos = [ 20 * (random.randrange(0, self.resolution[0] // 20)), 20 * (random.randrange(0, self.resolution[1] // 20))]
    
    def _draw_fruit(self):
        pygame.draw.rect(self.screen, 'Red', (self.pos[0], self.pos[1], self.size, self.size))

    def new_fruit(self):
        self.score += 1
        self.pos = [20 * (random.randrange(0, self.resolution[0] // 20)), 20 * (random.randrange(0, self.resolution[1] // 20))]


#def create_Fruit(screen, resolution):
#    #works, just gets removed by screen.fill
#    location = []
#    location = 20 * (random.randrange()), 20 * (random.randrange(1, resolution[1] // 20))
#    #print(location)
    
    

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

    curFruit = Fruit(screen, resolution)


    running = True
    
    # Player movement direction
    direction = None

    while running:

        screen.fill('Black')
        curFruit._draw_fruit()
        snake.draw_bits()
        pygame.display.flip()
        dt = clock.tick(10)

        snake.movement(direction)

        #snake.snake_body[3].pos[0] += 20
        #for idx in range(3, -1, -1):
            #print(idx)
            #print(snake.snake_body[idx].pos)

        #create_Fruit(screen, resolution)

        if(snake.snake_body[0].pos == curFruit.pos):
            #Checks if player "eats" a fruit
            curFruit.new_fruit()
            print(curFruit.pos)
        
        if(snake.check_bounds(resolution)):
            #checks if player left screen and resets game
            snake = SnakeTrail([resolution[0]//2,resolution[1]//2], screen, 4)
            snake.create_bits()
            curFruit = Fruit(screen, resolution)
            direction = None

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