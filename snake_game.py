# pygame 라이브러리를 import 합니다.
import pygame
# sys 라이브러리를 import 합니다.
import sys
# random 라이브러리를 import 합니다.
import random

# pygame 라이브러리를 초기화합니다.
pygame.init()

# 게임 설정
CELL_SIZE = 20
GRID_WIDTH = 20
GRID_HEIGHT = 20
FPS = 5

# 색상
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
GREEN = (0, 255, 0)
RED = (255, 0, 0)

# 윈도우를 초기화합니다.
screen = pygame.display.set_mode((GRID_WIDTH * CELL_SIZE, GRID_HEIGHT * CELL_SIZE))
pygame.display.set_caption("Snake Game")
clock = pygame.time.Clock()

# Snake 클래스를 정의합니다.
class Snake:
    def __init__(self):
        self.body = [(GRID_WIDTH // 2, GRID_HEIGHT // 2)]
        self.direction = (0, -1)

    def move(self):
        head = (self.body[0][0] + self.direction[0], self.body[0][1] + self.direction[1])
        self.body.insert(0, head)
        self.body.pop()

    def grow(self):
        tail = self.body[-1]
        self.body.append(tail)

    def is_collision(self):
        return self.body[0] in self.body[1:] or \
               self.body[0][0] < 0 or \
               self.body[0][1] < 0 or \
               self.body[0][0] >= GRID_WIDTH or \
               self.body[0][1] >= GRID_HEIGHT

# Food 클래스를 정의합니다.
class Food:
    def __init__(self):
        self.position = (random.randint(0, GRID_WIDTH - 1), random.randint(0, GRID_HEIGHT - 1))

    def respawn(self, snake_body):
        while self.position in snake_body:
            self.position = (random.randint(0, GRID_WIDTH - 1), random.randint(0, GRID_HEIGHT - 1))

# main 함수를 정의합니다.
def main():
    # Snake 객체와 Food 객체를 생성합니다.
    snake = Snake()
    food = Food()

    while True:
        # 이벤트를 처리합니다.
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_UP and snake.direction != (0, 1):
                    snake.direction = (0, -1)
                elif event.key == pygame.K_DOWN and snake.direction != (0, -1):
                    snake.direction = (0, 1)
                elif event.key == pygame.K_LEFT and snake.direction != (1, 0):
                    snake.direction = (-1, 0)
                elif event.key == pygame.K_RIGHT and snake.direction != (-1, 0):
                    snake.direction = (1, 0)

        # 게임 상태를 업데이트합니다.
        snake.move()

        if snake.is_collision():
            print('collision')
            break

        if snake.body[0] == food.position:
            snake.grow()
            food.respawn(snake.body)
            print('grow')

        # 게임을 그립니다.
        screen.fill(WHITE)

        for segment in snake.body:
            pygame.draw.rect(screen, GREEN, (segment[0] * CELL_SIZE, segment[1] * CELL_SIZE, CELL_SIZE, CELL_SIZE))

        pygame.draw.rect(screen, RED, (food.position[0] * CELL_SIZE, food.position[1] * CELL_SIZE, CELL_SIZE, CELL_SIZE))

        pygame.display.flip()
        clock.tick(FPS)

# main 함수를 호출합니다.
if __name__ == "__main__":
    main()
