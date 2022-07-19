import pygame
class Game:
    def __init__(self):
        # konfiguracja
        self.tps = 100.0

        # inicjalizacja
        pygame.init()
        self.screen = pygame.display.set_mode((1280, 720))
        self.tps_clock = pygame.time.Clock()
        self.tps_delta = 0.0

        # deska gracza
        self.player = Board(self)

        # piłka
        self.ball = Ball(self)


        self.running = True
        while self.running:
            for event in pygame.event.get():
                if event.type == pygame.QUIT or event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE:
                    self.running = False
            # tiknięcia
            self.tps_delta += self.tps_clock.tick() / 1000.0
            while self.tps_delta > 1 / self.tps:
                self.tick()
                self.tps_delta -= 1 / self.tps

            # wykonanie
            self.screen.fill((0, 0, 0))
            self.screen.blit(self.player.board, self.player.position)
            self.screen.blit(self.ball.ball, self.ball.position)

            if pygame.sprite.collide_rect(self.player, self.ball):
                if self.ball.x_velocity < 0:
                    if self.ball.position[1] == self.player.position[1]:
                        self.ball.y_velocity = -self.ball.y_velocity
                    else:
                        self.ball.position[0] -= self.ball.x_velocity
                        self.ball.y_velocity = -self.ball.y_velocity
                elif self.ball.x_velocity > 0:
                    if self.ball.position[1] == self.ball.position[1]:
                        self.ball.y_velocity = -self.ball.y_velocity
                        self.ball.x_velocity = -self.ball.x_velocity
                    else:
                        self.ball.position[0] -= self.ball.x_velocity
                        self.ball.y_velocity = -self.ball.y_velocity
            pygame.display.flip()

    def tick(self):
        self.player.tick()
        self.ball.tick()


class Board(pygame.sprite.Sprite):
    def __init__(self, Game):
        pygame.sprite.Sprite.__init__(self)
        self.board = pygame.image.load('board.jpg')
        self.rect = self.board.get_rect()
        self.game = Game
        self.velocity = [0, 0]
        self.size = self.game.screen.get_size()
        self.position = [self.size[0]/2-75, self.size[1]-70]

    def tick(self):
        # klawisze
        keys = pygame.key.get_pressed()
        if keys[pygame.K_RIGHT] and keys[pygame.K_LEFT]:
            self.velocity[0] = 0
        elif keys[pygame.K_RIGHT]:
            if self.position[0] > self.size[0]-250:
                self.position[0] = self.size[0]-250
            else:
                self.position[0] += 2
        elif keys[pygame.K_LEFT]:
            if self.position[0] < 0:
                self.position[0] = 0
            else:
                self.position[0] -= 2
        elif self.position[0] == (self.size[0] - 500) or self.position[0] == 0:
            self.position[0] = 600
        self.rect.topleft = self.position[0], self.position[1]





class Ball(pygame.sprite.Sprite):
    def __init__(self, Game):
        pygame.sprite.Sprite.__init__(self)
        self.ball = pygame.image.load('ball.jpg')
        self.rect = self.ball.get_rect()
        self.x_velocity = 3
        self.y_velocity = -3
        self.game = Game
        self.velocity = [self.x_velocity, self.y_velocity]
        self.size = self.game.screen.get_size()
        self.position = [self.size[0] / 2, self.size[1]/2]

    def tick(self):
        self.position[0] += self.x_velocity
        self.position[1] += self.y_velocity
        if self.position[0] == self.size[0]-10:
            self.x_velocity = -self.x_velocity
        elif self.position[0] < 3:
            self.x_velocity = -self.x_velocity
        elif self.position[1] < 3:
            self.y_velocity = -self.y_velocity
        elif self.position[1] > self.size[1]:
            self.game.running = False

        self.rect.topleft = self.position[0], self.position[1]






if __name__ == "__main__":
    Game()