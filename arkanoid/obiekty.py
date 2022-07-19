import math
import pygame

black = (0, 0, 0)
white = (255, 255, 255)
blue = (0, 0, 255)
red = (255, 0, 0)
green = (0, 255, 0)
block_gap = 5


def load_sound(name):
    sound = pygame.mixer.Sound(name)
    return sound


class Data(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.width = 300
        self.height = 600
        self.image = pygame.Surface((self.width, self.height))
        self.rect = self.image.get_rect()
        self.rect.x = 800
        self.rect.y = 0
        self.image.fill((0, 100, 100))


class Score_Board(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.score = 0
        self.text = f'Score: {self.score}'
        self.font = pygame.font.SysFont(None, 50)
        self.image = self.font.render(self.text, 1, white)
        self.rect = self.image.get_rect()
        self.rect.x = 870
        self.rect.y = 20

    def update(self):
        self.score += 1
        self.text = f'Score: {self.score}'
        self.image = self.font.render(self.text, 1, white)
        self.rect = self.image.get_rect()
        self.rect.x = 870
        self.rect.y = 20


class Lives_Board(pygame.sprite.Sprite):
    def __init__(self, player):
        pygame.sprite.Sprite.__init__(self)
        self.lives = player.lives
        self.text = f'Lives: {self.lives}'
        self.font = pygame.font.SysFont(None, 50)
        self.image = self.font.render(self.text, 1, white)
        self.rect = self.image.get_rect()
        self.rect.x = 870
        self.rect.y = 100

    def update(self):
        self.lives -= 1
        self.text = f'Lives: {self.lives}'
        self.image = self.font.render(self.text, 1, white)
        self.rect = self.image.get_rect()
        self.rect.x = 870
        self.rect.y = 100


class Block(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.width = 62
        self.height = 30
        self.image = pygame.Surface((self.width, self.height))
        self.image.fill(red)
        self.rect = self.image.get_rect()
        self.lives = 1
        self.x = 0
        self.y = 0


class First_special_Block(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.width = 62
        self.height = 30
        self.image = pygame.Surface((self.width, self.height))
        self.image.fill(white)
        self.rect = self.image.get_rect()
        self.x = 0
        self.y = 0
        self.lives = 3


class Second_special_Block(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.width = 62
        self.height = 30
        self.image = pygame.Surface((self.width, self.height))
        self.image.fill(blue)
        self.rect = self.image.get_rect()
        self.x = 0
        self.y = 0
        self.lives = 2


class Third_Special_Block(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.width = 62
        self.height = 30
        self.image = pygame.Surface((self.width, self.height))
        self.image.fill(green)
        self.rect = self.image.get_rect()
        self.x = 0
        self.y = 0
        self.lives = 1


class Player(pygame.sprite.Sprite):

    def __init__(self):
        pygame.sprite.Sprite.__init__(self)

        self.width = 100
        self.height = 10
        self.lives = 3
        self.image = pygame.Surface([self.width, self.height])
        self.image.fill(white)

        self.rect = self.image.get_rect()
        self.screenheight = pygame.display.get_surface().get_height()
        self.screenwidth = pygame.display.get_surface().get_width()

        self.rect.x = 0
        self.rect.y = self.screenheight - self.height

    def update(self, data):
        keys = pygame.key.get_pressed()
        if keys[pygame.K_RIGHT] and keys[pygame.K_LEFT]:
            self.rect.x = self.rect.x
        elif keys[pygame.K_RIGHT]:
            if self.rect.x > self.screenwidth - self.width - data.width:
                self.rect.x = self.screenwidth - self.width - data.width
            else:
                self.rect.x += 5
        elif keys[pygame.K_LEFT]:
            if self.rect.x < 0:
                self.rect.x = 0
            else:
                self.rect.x -= 5

    def consequences1(self, allsprites):
        self.width *= 0.75
        self.image = pygame.Surface((self.width, self.height))
        self.image.fill(white)
        self.x = self.rect.x
        self.rect = self.image.get_rect()
        self.rect.x = self.x
        self.rect.y = self.screenheight - self.height
        allsprites.add(self)
        self.time = pygame.time.get_ticks()


class Ball(pygame.sprite.Sprite):
    def __init__(self, data):
        pygame.sprite.Sprite.__init__(self)
        self.moveing = False
        self.speed = -5
        self.direction = 200
        self.width = 15
        self.height = 15
        self.image = pygame.Surface([self.width, self.height])
        self.image.fill(white)
        self.rect = self.image.get_rect()
        self.screenheight = pygame.display.get_surface().get_height()
        self.screenwidth = pygame.display.get_surface().get_width() - data.width
        self.x = self.screenwidth / 2
        self.y = self.screenheight / 2
        self.rect.x = self.x
        self.rect.y = self.y
        self.time = 0

    def bounce(self, diff):
        self.direction = (180 - self.direction) % 360
        self.direction -= diff

    def update(self, blocks, third_special_block, ball_sound, screen, data, score, player, allsprites):
        if self.moveing == True:
            block_hit = pygame.sprite.spritecollide(self, blocks, False)
            block3_hit = pygame.sprite.spritecollide(self, third_special_block, True)
            if len(block_hit) > 0 or len(block3_hit) > 0:
                for i in block3_hit:
                    player.consequences1(allsprites)
                    self.time = pygame.time.get_ticks()
                hits = block3_hit + block_hit
                score.update()

                # ball_sound.play()
                collision_tolerante = 5
                if abs(hits[-1].rect.y - self.height - self.y) < collision_tolerante:
                    self.bounce(0)
                if abs(hits[-1].rect.y + hits[-1].height - self.y) < collision_tolerante:
                    self.bounce(0)
                if abs(hits[-1].rect.x + hits[-1].width - self.x) < collision_tolerante:
                    self.bounce(180)
                if abs(hits[-1].rect.x - self.width - self.x) < collision_tolerante:
                    self.bounce(180)
                if hits[-1].lives == 3:
                    hits[-1].lives = 2
                    hits[-1].image.fill(blue)
                elif hits[-1].lives == 2:
                    hits[-1].lives = 1
                    hits[-1].image.fill(red)
                elif hits[-1].lives == 1:
                    hits[-1].kill()
            if self.time != 0:
                if (pygame.time.get_ticks() - self.time) // 1000 == 5:
                    player.width = 100
                    player.image = pygame.Surface((player.width, player.height))
                    player.image.fill(white)
                    player.x = player.rect.x
                    player.rect = player.image.get_rect()
                    player.rect.x = player.x
                    player.rect.y = player.screenheight - player.height
                    allsprites.add(player)

            direction_radians = math.radians(self.direction)
            self.x += self.speed * math.sin(direction_radians)
            self.y -= self.speed * math.cos(direction_radians)

            if self.rect.y <= 0:
                self.bounce(0)
                self.y = 1

            if self.rect.x <= 0:
                self.direction = (360 - self.direction) % 360
                self.x = 1

            if self.x > self.screenwidth - self.width:
                self.direction = (360 - self.direction) % 360
                self.x = self.screenwidth - self.width - 1
        self.rect.x = self.x
        self.rect.y = self.y


class Game:
    def __init__(self):
        pygame.init()
        # efekty dźwiękowe
        # load_sound("Humo-ahora-Money-Heist-La-Casa-de-Papel-Original-Soundtrack.wav").play()
        ball_sound = load_sound("fed_laser.wav")
        # ball_sound.play()
        # inicalizacja

        screen = pygame.display.set_mode([1100, 600])
        pygame.display.set_caption('Gra Piotera')

        # Sprite'y
        allsprites = pygame.sprite.Group()

        player = Player()
        allsprites.add(player)

        data = Data()
        allsprites.add(data)

        balls = pygame.sprite.Group()
        ball = Ball(data)
        balls.add(ball)
        allsprites.add(ball)

        score = Score_Board()
        allsprites.add(score)

        lives = Lives_Board(player)
        allsprites.add(lives)

        blocks = pygame.sprite.Group()

        for j in range(12):
            block = Block()
            block.rect.x = j * (block_gap + block.width)
            block.rect.y = 0
            blocks.add(block)
            allsprites.add(block)

        for j in range(6):
            block = Block()
            block.rect.x = j * (2 * block_gap + 2 * block.width) + block.width + block_gap
            block.rect.y = block.height + block_gap
            blocks.add(block)
            allsprites.add(block)

        for j in range(12):
            block1 = First_special_Block()
            block1.rect.x = j * (block_gap + block1.width)
            block1.rect.y = 4 * (block_gap + block1.height)
            blocks.add(block1)
            allsprites.add(block1)
        for i in range(6):
            for j in range(1, 3):
                block = Second_special_Block()
                block.rect.x = i * (2 * block_gap + 2 * block.width)
                block.rect.y = j * (block_gap + block.height)
                blocks.add(block)
                allsprites.add(block)
        for i in range(12):
            for j in range(3, 6, 2):
                block = Block()
                block.rect.x = i * (block_gap + block.width)
                block.rect.y = j * (block_gap + block.height)
                blocks.add(block)
                allsprites.add(block)

        third_special_block = pygame.sprite.Group()
        third_block = Third_Special_Block()
        third_block.rect.x = block_gap + third_block.width
        third_block.rect.y = 300 + block_gap + third_block.height
        third_special_block.add(third_block)
        allsprites.add(third_block)

        clock = pygame.time.Clock()
        self.running = True
        while self.running:
            clock.tick(100)
            screen.fill(black)

            third_block.update()
            blocks.update()

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.running = False
            keys = pygame.key.get_pressed()
            if keys[pygame.K_SPACE]:
                ball.moveing = True

            if pygame.sprite.spritecollide(player, balls, False):
                # ball_sound.play()
                diff = (player.rect.x + player.width / 2) - (ball.rect.x + ball.width / 2)
                ball.rect.y = screen.get_height() - player.rect.height - ball.rect.height - 1
                ball.bounce(diff)

            allsprites.draw(screen)

            if ball.rect.y > 600:
                if player.lives == 3 or player.lives == 2 or player.lives == 1:
                    ball.x = ball.screenwidth / 2
                    ball.y = ball.screenheight / 2
                    ball.moveing = False
                    player.lives -= 1
                    lives.update()
                else:
                    self.running = False

            player.update(data)
            ball.update(blocks, third_special_block, ball_sound, screen, data, score, player, allsprites)
            pygame.display.flip()


class Main_Menu():
    def __init__(self):
        screen


if __name__ == "__main__":
    Game()