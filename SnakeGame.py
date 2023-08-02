import pygame
import random

white = (255, 255, 255)
red = (255, 0, 0)
green = (0, 255, 0)
black = (0, 0, 0)

screen_width = 600
screen_height = 600
grid_size = 30
grid_width = screen_width // grid_size
grind_heigth = screen_height // grid_size


class Snake:
    def __init__(self):
        self.body = [(grid_width // 2, grind_heigth // 2)]
        self.direction = (1, 0)

    def move(self):
        head_x, head_y = self.body[0]
        dx, dy = self.direction
        new_head = ((head_x + dx) % grid_width, (head_y + dy) % grind_heigth)
        self.body.insert(0, new_head)

    def turn(self, direction):
        self.direction = direction

    def collide_with_food(self, food_position):
        return self.body[0] == food_position

    def check_collision(self):
        return len(self.body) != len(set(self.body))

    def get_head(self):
        return self.body[0]

    def get_body(self):
        return self.body[1:]


def main():
    pygame.init()


    screen = pygame.display.set_mode((screen_width, screen_height))
    pygame.display.set_caption('Snake Game')

  
    snake = Snake()
    food = (random.randint(0, grid_width - 1), random.randint(0, grind_heigth - 1))

    
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                return

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_UP:
                    snake.turn((0, -1))
                elif event.key == pygame.K_DOWN:
                    snake.turn((0, 1))
                elif event.key == pygame.K_LEFT:
                    snake.turn((-1, 0))
                elif event.key == pygame.K_RIGHT:
                    snake.turn((1, 0))

        snake.move()

        if snake.collide_with_food(food):
            food = (random.randint(0, grid_width - 1), random.randint(0, grind_heigth - 1))
        else:
            snake.body.pop()

        if snake.check_collision():
            print("Fim de jogo! Pontuação:", len(snake.body))
            pygame.quit()
            return

        screen.fill(black)
        pygame.draw.rect(screen, green, (food[0] * grid_size, food[1] * grid_size, grid_size, grid_size))

        for segment in snake.get_body():
            pygame.draw.rect(screen, white, (segment[0] * grid_size, segment[1] * grid_size, grid_size, grid_size))

        pygame.draw.rect(screen, red, (snake.get_head()[0] * grid_size, snake.get_head()[1] * grid_size, grid_size, grid_size))

        pygame.display.update()
        pygame.time.delay(150)

if __name__ == "__main__":
    main()
