import math
import pygame
from pygame.locals import *
import sys

# kolory

black = (0, 0, 0)
white = (255, 255, 255)
blue = (0, 0, 255)
red = (255, 0, 0)
green = (0, 255, 0)
block_gap = 5

# funkcja do ładowania dźwięków

def load_sound(name):
    """Funkcja odtwarzająca dźwięki.
    :param name: Nazwa pliku dźwiękowego.
    :return dźwięk.
    """
    pygame.mixer.pre_init(44100, -16, 1, 512)
    sound = pygame.mixer.Sound(name)
    return sound

def draw_text(text, font, color, surface, x, y):
    """Funkcja pisząca tekst.
    :param text: tekst jaki będzie napisany.
    :param font: rodzaj czcionki.
    :param color: kolor czcionki.
    :param surface: okno gdzie będzie wyświetlony tekst.
    :param x: współrzędna x.
    :param y: współrzędna y.
    """
    text_obj = font.render(text, 1, color)
    text_rect = text_obj.get_rect()
    text_rect.topleft = (x, y)
    surface.blit(text_obj, text_rect)


class Data(pygame.sprite.Sprite):
    """Klasa initująca tablicę z wynikami i icznikiem żyć."""
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.width = 300
        self.height = 600
        self.image = pygame.Surface((self.width, self.height))
        self.rect = self.image.get_rect()
        self.rect.x = 800
        self.rect.y = 0
        self.image.fill((0, 50, 100))


class Score_Board(pygame.sprite.Sprite):
    """Klasa initująca wynik na tablicy."""
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.score = 0
        self.text = f'Score: {self.score}'
        self.font = pygame.font.SysFont(None, 50)
        self.image = self.font.render(self.text, 1, white)
        self.rect = self.image.get_rect()
        self.rect.x = 870
        self.rect.y = 100

    def update(self):
        """Funkcja aktualizująca wynik na tablicy."""
        self.score += 1
        self.text = f'Score: {self.score}'
        self.image = self.font.render(self.text, 1, white)
        self.rect = self.image.get_rect()
        self.rect.x = 870
        self.rect.y = 100


class Lives_Board(pygame.sprite.Sprite):
    """Klasa initująca licznik żyć na tablicy."""
    def __init__(self, player):
        pygame.sprite.Sprite.__init__(self)
        self.lives = player.lives
        self.text = f'Lives: {self.lives}'
        self.font = pygame.font.SysFont(None, 50)
        self.image = self.font.render(self.text, 1, white)
        self.rect = self.image.get_rect()
        self.rect.x = 870
        self.rect.y = 300

    def update(self):
        """Funkcja aktualizująca ilść żyć na tablicy wyników."""
        self.lives -= 1
        self.text = f'Lives: {self.lives}'
        self.image = self.font.render(self.text, 1, white)
        self.rect = self.image.get_rect()
        self.rect.x = 870
        self.rect.y = 300


class Block(pygame.sprite.Sprite):
    """Klasa zwykłąego bloczka."""
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
    """Klasa pierwszego specjalnego bloczka."""
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
    """Klasa drugiego specjalnego bloczka."""
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
    """Klasa trzeciego specjalnego bloczka."""
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


class Fourth_Special_Block(pygame.sprite.Sprite):
    """Klasa czwartego specjalnego bloczka."""
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
    """Klasa initująca gracza na ekranie."""
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

        self.rect.x = self.screenheight - 250
        self.rect.y = self.screenheight - self.height
        self.consequences = False
        self.time1 = 0

    def update(self, data):
        """Funkcja aktualizująca pozycję gracza na ekranie."""
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
        """Funkcja zmniejszająca szerokość platformy."""
        self.width *= 0.75
        self.image = pygame.Surface((self.width, self.height))
        self.image.fill(white)
        self.x = self.rect.x
        self.rect = self.image.get_rect()
        self.rect.x = self.x
        self.rect.y = self.screenheight - self.height
        allsprites.add(self)

    def consequences2(self, data):
        """Funkcja przyspieszająca poruszanie się platformy."""
        keys = pygame.key.get_pressed()
        if keys[pygame.K_RIGHT] and keys[pygame.K_LEFT]:
            self.rect.x = self.rect.x
        elif keys[pygame.K_RIGHT]:
            if self.rect.x > self.screenwidth - self.width - data.width:
                self.rect.x = self.screenwidth - self.width - data.width
            else:
                self.rect.x += 15
        elif keys[pygame.K_LEFT]:
            if self.rect.x < 0:
                self.rect.x = 0
            else:
                self.rect.x -= 15
        self.consequences = True


class Ball(pygame.sprite.Sprite):
    """Klasa initująca piłkę."""
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
        self.time1 = 0
        self.time2 = 0

    def bounce(self, diff):
        """Funkcja odbijająca piłkę."""
        self.direction = (180 - self.direction) % 360
        self.direction -= diff

    def update(self, blocks, third_special_block, fourth_special_block, fifth_special_block, sixth_special_block,
               board_sound, block_sound, special1, special2, screen, data, score, player, allsprites):
        """Funkcja aktualizująca pozycję piłki na ekranie oraz uwzględniająca kolizje między obiektami."""
        if self.moveing == True:
            k = 0
            a = 0
            b = 0
            block_hit = pygame.sprite.spritecollide(self, blocks, False)
            block3_hit = pygame.sprite.spritecollide(self, third_special_block, True)
            block4_hit = pygame.sprite.spritecollide(self, fourth_special_block, True)
            block5_hit = pygame.sprite.spritecollide(self, fifth_special_block, True)
            block6_hit = pygame.sprite.spritecollide(self, sixth_special_block, True)
            if len(block_hit) > 0 or len(block3_hit) > 0 or len(block4_hit) > 0 or len(block5_hit) > 0 or len(
                    block6_hit) > 0:
                for i in block3_hit:
                    special2.play()
                    player.consequences1(allsprites)
                    k = 1
                    self.time = pygame.time.get_ticks()
                for i in block4_hit:
                    special2.play()
                    self.speed_()
                    a = 1
                    self.time = pygame.time.get_ticks()
                for i in block5_hit:
                    special1.play()
                    player.consequences2(data)
                    player.time1 = pygame.time.get_ticks()
                for i in block6_hit:
                    special2.play()
                    self.size()
                    b = 1
                    self.time2 = pygame.time.get_ticks()

                hits = block3_hit + block_hit + block4_hit + block5_hit + block6_hit
                score.update()

                block_sound.play()
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
                if ((pygame.time.get_ticks() - self.time) // 1000 == 10) or (
                        ((pygame.time.get_ticks() - self.time) // 1000 > 10) and k == 1):
                    special1.play()
                    player.width = 100
                    player.image = pygame.Surface((player.width, player.height))
                    player.image.fill(white)
                    player.x = player.rect.x
                    player.rect = player.image.get_rect()
                    player.rect.x = player.x
                    player.rect.y = player.screenheight - player.height
                    allsprites.add(player)
                    k = 0
            if self.time1 != 0:
                if ((pygame.time.get_ticks() - self.time1) // 1000 == 10) or (
                        ((pygame.time.get_ticks() - self.time1) // 1000 > 10) and a == 1):
                    special1.play()
                    self.speed = -5

            if self.time2 != 0:
                if ((pygame.time.get_ticks() - self.time2) // 1000 == 10) or (
                        ((pygame.time.get_ticks() - self.time2) // 1000 > 10) and b == 1):
                    special1.play()
                    self.width = 15
                    self.height = 15
                    self.image = pygame.Surface([self.width, self.height])
                    self.image.fill(white)

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

    def speed_(self):
        """Funkcja zwalniająca poruszanie się piłki."""
        self.time1 = pygame.time.get_ticks()
        self.speed *= 0.7

    def size(self):
        """Funkcja powiększająca rozmiar piłki."""
        self.time2 = pygame.time.get_ticks()
        self.width = 30
        self.height = 30
        self.image = pygame.Surface([self.width, self.height])
        self.image.fill(white)


class Game:
    """Klasa initująca grę."""
    def __init__(self):
        pygame.mixer.init()
        pygame.init()

        # efekty dźwiękowe

        board_sound = load_sound("Deska.wav")
        block_sound = load_sound("Klocki.wav")
        special1 = load_sound("Zmneijszenie.wav")
        special2 = load_sound("Zwiekszenie.wav")
        loss = load_sound("strata.wav")
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

        self.score = 0

        # ustawianie bloczków
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

        block1 = First_special_Block()
        block1.rect.x = 3 * (block_gap + block1.width)
        block1.rect.y = 2 * (block_gap + block1.height)
        blocks.add(block1)
        allsprites.add(block1)

        block1 = First_special_Block()
        block1.rect.x = 9 * (block_gap + block1.width)
        block1.rect.y = 2 * (block_gap + block1.height)
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
        third_block.rect.y = 2 * block_gap + 2 * third_block.height
        third_special_block.add(third_block)
        allsprites.add(third_block)

        fourth_special_block = pygame.sprite.Group()
        fourth_block = Fourth_Special_Block()
        fourth_block.rect.x = 7 * block_gap + 7 * fourth_block.width
        fourth_block.rect.y = 2 * block_gap + 2 * fourth_block.height
        fourth_special_block.add(fourth_block)
        allsprites.add(fourth_block)

        fifth_special_block = pygame.sprite.Group()
        fifth_block = Fourth_Special_Block()
        fifth_block.rect.x = 5 * block_gap + 5 * fifth_block.width
        fifth_block.rect.y = 2 * block_gap + 2 * fifth_block.height
        fifth_special_block.add(fifth_block)
        allsprites.add(fifth_block)

        sixth_special_block = pygame.sprite.Group()
        sixth_block = Fourth_Special_Block()
        sixth_block.rect.x = 11 * block_gap + 11 * sixth_block.width
        sixth_block.rect.y = 2 * block_gap + 2 * sixth_block.height
        sixth_special_block.add(sixth_block)
        allsprites.add(sixth_block)

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
                    sys.exit()
                if event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE:
                    Main_Menu()
            keys = pygame.key.get_pressed()
            if keys[pygame.K_SPACE]:
                ball.moveing = True

            if pygame.sprite.spritecollide(player, balls, False):
                board_sound.play()
                diff = (player.rect.x + player.width / 2) - (ball.rect.x + ball.width / 2)
                ball.rect.y = screen.get_height() - player.rect.height - ball.rect.height - 1
                ball.bounce(diff)

            allsprites.draw(screen)
            if score.score == 112:
                self.running = False
                self.score = score.score
                with open('wyniki.txt', 'r+') as results:
                    results.write(str(self.score) + '\n')
                    print(results.read())
                with open('wyniki.txt') as results:
                    wyniki = results.read()
                    print(results.read())
                wyniki = wyniki.split('\n')
                print(wyniki)
                if self.score >= 10:
                    del wyniki[1]
                del wyniki[-1]
                wyniki.append('0')
                wyniki = [int(i) for i in wyniki]
                wyniki = sorted(wyniki)
                print(wyniki)
                with open('wyniki.txt', 'w+') as results:

                    for i in wyniki:
                        results.write(str(i) + '\n')
                print(wyniki)
                Game_Over(self)

            if ball.rect.y > 600:
                loss.play()
                if player.lives == 3 or player.lives == 2 or player.lives == 1:
                    ball.x = ball.screenwidth / 2
                    ball.y = ball.screenheight / 2
                    ball.bounce(0)
                    ball.moveing = False
                    player.lives -= 1
                    lives.update()
                else:
                    self.running = False
                    self.score = score.score
                    with open('wyniki.txt', 'r+') as results:
                        results.write(str(self.score) + '\n')
                    with open('wyniki.txt') as results:
                        wyniki = results.read()
                    wyniki = wyniki.split('\n')
                    if self.score >= 10:
                        del wyniki[1]
                    del wyniki[-1]
                    wyniki.append('0')
                    wyniki = [int(i) for i in wyniki]
                    wyniki = sorted(wyniki)
                    with open('wyniki.txt', 'w+') as results:

                        for i in wyniki:
                            results.write(str(i) + '\n')
                    Game_Over(self)

            if player.consequences == False:
                player.update(data)
            else:
                player.consequences2(data)
                if (pygame.time.get_ticks() - player.time1) // 1000 >= 10:
                    player.consequences = False
                    special2.play()
            ball.update(blocks, third_special_block, fourth_special_block, fifth_special_block, sixth_special_block,
                        board_sound, block_sound, special1, special2, screen, data, score, player, allsprites)
            pygame.display.flip()


class Rules():
    """Klasa initująca okno z zasadami gry."""
    def __init__(self):
        pygame.init()
        screen = pygame.display.set_mode([1100, 600])
        pygame.display.set_caption('Gra Piotera')

        while True:
            mx, my = pygame.mouse.get_pos()
            screen.fill((0, 0, 0))
            text1 = "Gra jest klonem starej gry 'Arkanoid', w której chodzi o strącenie wszytskich bloczków z ekranu,"
            text1_5 = "tracąc max 3 życia."
            text2 = "Obsługa:"
            text3 = "1. Spacja - uruchamia poruszanie się piłki"
            text4 = "2. 'Lewo' i 'Prawo' - poruszanie platformą"
            text5 = "W grze występuje kilka rodzajów bloczków:"
            text6 = "1. Bloczek czerwony - zwykły bloczek, po jednym trafieniu zostaje strącony."
            text7 = "2. Bloczek niebieski - po dwóch trafieniach zostaje strącony."
            text8 = "3. Bloczek biały - po trzech trafieniach zostaje strącony."
            text9 = "4. Bloczki zielone mają specjalne funkcje: skrócenie platformy, przyspieszenie sterowania platformą,"
            text10 = "zwolnienie lotu piłki lub powiększenie rozmiaru piłki. Wszystkie efekty trwają 10 sekund."
            text11 = "POWODZENIA!!!"
            draw_text(text1, pygame.font.SysFont(None, 30), white, screen, 0, 50)
            draw_text(text1_5, pygame.font.SysFont(None, 30), white, screen, 800, 80)
            draw_text(text2, pygame.font.SysFont(None, 30), white, screen, 0, 100)
            draw_text(text3, pygame.font.SysFont(None, 30), white, screen, 0, 150)
            draw_text(text4, pygame.font.SysFont(None, 30), white, screen, 0, 200)
            draw_text(text5, pygame.font.SysFont(None, 30), white, screen, 0, 250)
            draw_text(text6, pygame.font.SysFont(None, 30), white, screen, 0, 300)
            draw_text(text7, pygame.font.SysFont(None, 30), white, screen, 0, 350)
            draw_text(text8, pygame.font.SysFont(None, 30), white, screen, 0, 400)
            draw_text(text9, pygame.font.SysFont(None, 30), white, screen, 0, 450)
            draw_text(text10, pygame.font.SysFont(None, 30), white, screen, 100, 480)
            draw_text(text11, pygame.font.SysFont(None, 50), white, screen, 400, 530)
            button1 = pygame.Rect(pygame.display.get_surface().get_width() / 2 +300, 520, 200, 50)
            pygame.draw.rect(screen, red, button1)
            draw_text("Back", pygame.font.SysFont(None, 65), white, screen,
                      pygame.display.get_surface().get_width() / 2 +350, 525)

            pygame.display.update()
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    sys.exit()
                if event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE:
                    Main_Menu()
                if event.type == MOUSEBUTTONDOWN:
                    if event.button == 1:
                        if button1.collidepoint(mx, my):
                            Main_Menu()


class Autor():
    """Klasa initująca okno z informacjami o autorze."""
    def __init__(self):
        pygame.init()
        screen = pygame.display.set_mode([1100, 600])
        pygame.display.set_caption('Gra Piotera')
        while True:
            mx, my = pygame.mouse.get_pos()
            screen.fill((0, 0, 0))
            text1 = "Autor gry:"
            text2 = "Piotr Zieleń"
            text3 = "Student 1. roku Matematyki Stosowanej na Politechnice Wrocłaskiej."
            draw_text(text1, pygame.font.SysFont(None, 50), white, screen, 470, 50)
            draw_text(text2, pygame.font.SysFont(None, 70), white, screen, 420, 150)
            draw_text(text3, pygame.font.SysFont(None, 40), white, screen, 70, 300)
            button1 = pygame.Rect(pygame.display.get_surface().get_width() / 2 +300, 500, 200, 50)
            pygame.draw.rect(screen, red, button1)
            draw_text("Back", pygame.font.SysFont(None, 65), white, screen,
                      pygame.display.get_surface().get_width() / 2 +350, 504)
            pygame.display.update()
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    sys.exit()
                if event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE:
                    Main_Menu()
                if event.type == MOUSEBUTTONDOWN:
                    if event.button == 1:
                        if button1.collidepoint(mx, my):
                            Main_Menu()


class Results():
    """Klasa initująca okno z najlepszymi wynikami."""
    def __init__(self):
        pygame.init()
        screen = pygame.display.set_mode([1100, 600])
        pygame.display.set_caption('Gra Piotera')
        with open('wyniki.txt') as results:
            wyniki = results.read()
            wyniki = wyniki.split('\n')
            del wyniki[-1]
            self.w1 = wyniki[-1]
            self.w2 = wyniki[-2]
            self.w3 = wyniki[-3]
            self.w4 = wyniki[-4]
            self.w5 = wyniki[-5]

        while True:
            screen.fill((0, 0, 0))
            mx, my = pygame.mouse.get_pos()
            text1 = "Najlepsze wyniki:"
            text2 = f"1. {self.w1}"
            text3 = f"2. {self.w2}"
            text4 = f"3. {self.w3}"
            text5 = f"4. {self.w4}"
            text6 = f"5. {self.w5}"
            draw_text(text1, pygame.font.SysFont(None, 70), white, screen, 350, 50)
            draw_text(text2, pygame.font.SysFont(None, 70), white, screen, 100, 130)
            draw_text(text3, pygame.font.SysFont(None, 70), white, screen, 100, 210)
            draw_text(text4, pygame.font.SysFont(None, 70), white, screen, 100, 290)
            draw_text(text5, pygame.font.SysFont(None, 70), white, screen, 100, 370)
            draw_text(text6, pygame.font.SysFont(None, 70), white, screen, 100, 450)
            button = pygame.Rect(pygame.display.get_surface().get_width() / 2 - 100, 500, 200, 50)
            pygame.draw.rect(screen, red, button)
            draw_text("Reset", pygame.font.SysFont(None, 65), white, screen,
                      pygame.display.get_surface().get_width() / 2 - 60, 504)
            button1 = pygame.Rect(pygame.display.get_surface().get_width() / 2 +300, 500, 200, 50)
            pygame.draw.rect(screen, red, button1)
            draw_text("Back", pygame.font.SysFont(None, 65), white, screen,
                      pygame.display.get_surface().get_width() / 2 +350, 504)
            pygame.display.update()
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    sys.exit()
                if event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE:
                    Main_Menu()
                if event.type == MOUSEBUTTONDOWN:
                    if event.button == 1:
                        if button.collidepoint(mx, my):
                            self.reset()
                            Main_Menu()
                        if button1.collidepoint(mx, my):
                            Main_Menu()

    def reset(self):
        """Funkcja resetująca najlepsze wyniki."""
        with open('wyniki.txt', 'w') as results:
            results.write("0\n0\n0\n0\n0\n0\n")


class Game_Over():
    """Klasa initująca okno z uzyskanym wynikiem."""
    def __init__(self, game):
        pygame.init()
        screen = pygame.display.set_mode([1100, 600])
        pygame.display.set_caption('Gra Piotera')
        self.game = game
        self.score = self.game.score
        while True:
            screen.fill((0, 0, 0))
            text1 = "Koniec gry"
            text2 = "Twój wynik:"
            text3 = str(self.score)
            draw_text(text1, pygame.font.SysFont(None, 70), white, screen, 400, 50)
            draw_text(text2, pygame.font.SysFont(None, 70), white, screen, 400, 150)
            draw_text(text3, pygame.font.SysFont(None, 200), white, screen, 500, 300)
            pygame.display.update()
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    sys.exit()
                if event.type == pygame.KEYDOWN and (event.key == pygame.K_ESCAPE or event.key == pygame.K_RETURN):
                    Main_Menu()


class Main_Menu():
    """Klasa initująca okno z menu głównym."""
    def __init__(self):
        pygame.init()
        screen = pygame.display.set_mode([1100, 600])
        pygame.display.set_caption('Gra Piotera')
        while True:
            screen.fill((0, 0, 0))

            draw_text('Main menu', pygame.font.SysFont(None, 80), white, screen,
                      pygame.display.get_surface().get_width() / 2 - 150, 20)

            mx, my = pygame.mouse.get_pos()

            button_1 = pygame.Rect(pygame.display.get_surface().get_width() / 2 - 100, 100, 200, 50)
            pygame.draw.rect(screen, red, button_1)
            draw_text("Play", pygame.font.SysFont(None, 65), white, screen,
                      pygame.display.get_surface().get_width() / 2 - 45, 103)

            button_2 = pygame.Rect(pygame.display.get_surface().get_width() / 2 - 100, 200, 200, 50)
            pygame.draw.rect(screen, red, button_2)
            draw_text("Rules", pygame.font.SysFont(None, 65), white, screen,
                      pygame.display.get_surface().get_width() / 2 - 60, 205)

            button_3 = pygame.Rect(pygame.display.get_surface().get_width() / 2 - 100, 300, 200, 50)
            pygame.draw.rect(screen, red, button_3)
            draw_text("High scores", pygame.font.SysFont(None, 45), white, screen,
                      pygame.display.get_surface().get_width() / 2 - 80, 310)

            button_4 = pygame.Rect(pygame.display.get_surface().get_width() / 2 - 100, 400, 200, 50)
            pygame.draw.rect(screen, red, button_4)
            draw_text("About author", pygame.font.SysFont(None, 45), white, screen,
                      pygame.display.get_surface().get_width() / 2 - 95, 410)

            button_5 = pygame.Rect(pygame.display.get_surface().get_width() / 2 - 100, 500, 200, 50)
            pygame.draw.rect(screen, red, button_5)
            draw_text("Exit", pygame.font.SysFont(None, 65), white, screen,
                      pygame.display.get_surface().get_width() / 2 - 50, 505)

            for event in pygame.event.get():
                if event.type == MOUSEBUTTONDOWN:
                    if event.button == 1:
                        if button_1.collidepoint(mx, my):
                            Game()
                        if button_2.collidepoint(mx, my):
                            Rules()
                        if button_3.collidepoint(mx, my):
                            Results()
                        if button_4.collidepoint(mx, my):
                            Autor()
                        if button_5.collidepoint(mx, my):
                            sys.exit()
                if event.type == pygame.QUIT:
                    sys.exit()
                if event.type == pygame.KEYDOWN and event.key == pygame.K_RETURN:
                    Game()
            pygame.display.update()


if __name__ == "__main__":
    try:
        f = open("wyniki.txt")
        f.close()
    except:
        with open('wyniki.txt', 'a+') as results:
            if len(results.read()) == 0:
                results.write("0\n0\n0\n0\n0\n0\n")
            else:
                pass
    Main_Menu()
