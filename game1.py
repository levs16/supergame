import pygame

#window settings
FPS = 60
WIDTH = 600
HEIGHT = 600


#colors
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)
LIME = (0, 255, 0)
BLUE = (0, 0, 255)
YELLOW = (25,255,0)
GRAY = (128, 128, 128)
VIOLET = (126, 8, 236)
PINK = (255, 192, 203)
ORANGE = (255, 165, 0)
PURPLE = (128, 0, 128)
GREEN = (0,128,0)
CYAN = (0, 255, 255)
LIGHTGRAY = (211, 211, 211)
NAVY = (0, 0, 128)
MEDIUMSLATEBLUE = (123, 104, 238)
SKYBLUE = (0, 191, 255)
HONEYDEW = (240, 255, 240)
SNOW = (255, 250, 250)
IVORY = (255, 255, 240)
YELLOWGREEN = (154, 205, 50)
DARKGREEN = (0, 100, 0)
INDIGO = (75, 0, 130)

#text
def text(screen, text, size, color, textFont, x, y):
    fontName = pygame.font.match_font(textFont)
    font = pygame.font.Font(fontName, size)
    textSurf = font.render(text, True, color)
    textRect = textSurf.get_rect()
    textRect.center = (x,y)
    screen.blit(textSurf, textRect)

#player 1 :)
class Player(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.transform.scale(player1Img,(50,50))
        self.image.set_colorkey(WHITE)
        self.rect = self.image.get_rect()
        self.rect.center = (WIDTH//2,HEIGHT//2)

    def update(self):
        self.speedx = 5
        self.speedy = 5
        keys = pygame.key.get_pressed()
        if keys[pygame.K_LEFT]:
            self.speedx = -5
        if keys[pygame.K_RIGHT]:
            self.speedx = 5
        if keys[pygame.K_UP]:
            self.speedy = -5
        if keys[pygame.K_DOWN]:
            speedy = 5
        if keys[pygame.K_RSHIFT]:
            self.speedx += 5
            self.speedy += 5
        self.rect.x += self.speedx
        self.rect.y += self.speedy

        if self.rect.right > WIDTH:
            self.rect.right = WIDTH

        if self.rect.left < 305:
            self.rect.left = 305

        if self.rect.top < 0:
            self.rect.top = 0

        if self.rect.bottom > HEIGHT:
            self.rect.bottom = HEIGHT

    def shoot(self):
        bullet = bulletP1(self.rect.centerx, self.rect.centery)
        sprites.add(bullet)
        bulletsPlayer1.add(bullet)

#player 2 :(
class Player2(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.transform.scale(player2Img,(50,50))
        self.image.set_colorkey(WHITE)
        self.rect = self.image.get_rect()
        self.rect.center = (600,0)
    
    def update(self):
        self.speedx = -5
        self.speedy = 5
        keys = pygame.key.get_pressed()
        if keys[pygame.K_a]:
            self.speedx = -5
        if keys[pygame.K_d]:
            self.speedx = 5
        if keys[pygame.K_w]:
            self.speedy = -5
        if keys[pygame.K_s]:
            speedy = 5
        if keys[pygame.K_LSHIFT]:
            self.speedx -= 5
            self.speedy += 5
        self.rect.x += self.speedx
        self.rect.y += self.speedy
        if self.rect.x < 0 and self.rect.y > HEIGHT:
            self.rect.center = (600,0)

        if self.rect.right > 295:
            self.rect.right = 295

        if self.rect.left < 0:
            self.rect.left = 0

        if self.rect.top < 0:
            self.rect.top = 0

        if self.rect.bottom > HEIGHT:
            self.rect.bottom = HEIGHT

    def shoot(self):
        bullet = bulletP2(self.rect.centerx, self.rect.centery)
        sprites.add(bullet)
        bulletsPlayer2.add(bullet)

#bullet player 1
class bulletP1(pygame.sprite.Sprite):
    def __init__(self,x,y):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.transform.scale(p1b,(10,5))
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
        self.speedx = -15
    def update(self):
        self.rect.x += self.speedx
        if self.rect.x<0:
            self.kill()

#bullet player 2
class bulletP2(pygame.sprite.Sprite):
    def __init__(self,x,y):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.transform.scale(p2b,(10,5))
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
        self.speedx = 15
    def update(self):
        self.rect.x += self.speedx
        if self.rect.x>WIDTH:
            self.kill()

#window design
pygame.init()
window = pygame.display.set_mode((WIDTH, HEIGHT))
clock = pygame.time.Clock()
pygame.display.set_caption('Supermegaultragood game')
pygame.display.set_icon(pygame.image.load('icon.svg'))

#textures
background = pygame.image.load('bg.png').convert()
background = pygame.transform.scale(background,(WIDTH, HEIGHT))
background_rect = background.get_rect()
bgsc0 = pygame.image.load('game0.jpeg').convert()
bgsc0 = pygame.transform.scale(bgsc0,(WIDTH, HEIGHT))
bgsc0_rect = bgsc0.get_rect()
menuESCbg = pygame.image.load('menuESC.jpeg').convert()
menuESCbg = pygame.transform.scale(menuESCbg,(WIDTH, HEIGHT))
menuESCbg_rect = menuESCbg.get_rect()
endbg = pygame.image.load('endbg.jpeg').convert()
endbg = pygame.transform.scale(endbg,(WIDTH, HEIGHT))
endbg_rect = endbg.get_rect()
mainbg = pygame.image.load('mainbg.jpeg').convert()
mainbg = pygame.transform.scale(mainbg,(WIDTH, HEIGHT))
mainbg_rect = mainbg.get_rect()
player1Img = pygame.image.load('p1.png').convert()
player2Img = pygame.image.load('p2.png').convert()
p1b = pygame.image.load('p1b.jpeg')
p2b = pygame.image.load('p2b.jpeg')

#music
pygame.mixer.music.load('theme2.mp3')
pygame.mixer.music.set_volume(0)
pygame.mixer.music.play(loops = -1)

#objects
player = Player()
sprites = pygame.sprite.Group()
sprites.add(player)
bulletsPlayer1 = pygame.sprite.Group()
bulletsPlayer2 = pygame.sprite.Group()
player2 = Player2()
enemies = pygame.sprite.Group()
enemies.add(player2)
s1 = 0
s2 = 0

#main cycle
game = 0
run = True
while run:
    clock.tick(FPS)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_l:
                player.shoot()
            if event.key == pygame.K_e:
                player2.shoot()
            if event.key == pygame.K_ESCAPE:
                if game != 0:
                    game = 4
            if event.key == pygame.K_n:
                    game = 1
            if event.key == pygame.K_q:
                if game != 1:
                    run = False
            if event.key == pygame.K_c:
                if game != 0:
                    game = 1
            if event.key == pygame.K_m:
                if game !=1:
                    game = 0


    #bullets and their hits
    bulletHitP2 = pygame.sprite.spritecollide(player2, bulletsPlayer1, True)
    bulletHitP1 = pygame.sprite.spritecollide(player, bulletsPlayer2, True)

    if bulletHitP2:
        s1+=1
        pygame.mixer.music.load('bruh.mp3')
        pygame.mixer.music.set_volume(0.3)
        pygame.mixer.music.play()

    if bulletHitP1:
        s2+=1
        pygame.mixer.music.load('bruh.mp3')
        pygame.mixer.music.set_volume(0.3)
        pygame.mixer.music.play()


    #playerHit = pygame.sprite.spritecollide(player, enemies, False)
    '''for k in playerHit:
        if k:
            text(window, 'Hit', 100, WHITE, 'Arial',WIDTH//2,HEIGHT//2)
            pygame.mixer.music.load('amongus.mp3')
            pygame.mixer.music.set_volume(0.1)
            pygame.mixer.music.play()'''

    #bullet hit counter
    if s1 == 10:    
        game = 3
    if s2 == 10:
        game = 2

    #drawing graphics
    if game == 0:
        window.blit(mainbg, mainbg_rect)
        text(window, '|Start |N|', 40, GRAY,'Arial', WIDTH//2, HEIGHT//2)
        text(window, '|Exit to desktop |Q|', 40, GRAY, 'Arial', WIDTH//2, HEIGHT//2+50)
        text(window, 'THIS GAME IS DISCONTINUED! THERE WOULD BE NO UPDATES!', 20, RED, 'Arial', WIDTH//2, HEIGHT//2+100)
        text(window, 'You can visit my github for other games: https://github.com/levs16/', 20, SKYBLUE, 'Arial', WIDTH//2, HEIGHT//2+150)
        text(window, 'Version 0.5.1', 20, LIGHTGRAY, 'Arial', 545, 580 )
        text(window, 'Aboba Games®. All rights reserved©', 20, LIGHTGRAY, 'Arial', 140, 580)
        pygame.display.update()

    if game == 1:
        window.blit(background, background_rect)
        pygame.draw.rect(window, BLACK, (295,0,10,600))
        sprites.draw(window)
        sprites.update()
        enemies.draw(window)
        enemies.update()
        #text(window, 'АБОБА', 40, YELLOW, 'Arial', WIDTH//2, HEIGHT//2)
        text(window, str(s1), 30, SKYBLUE, 'Arial', 150, 100)
        text(window, str(s2), 30, SKYBLUE, 'Arial', 450, 100)
        pygame.display.update()
    if game == 3:
            window.blit(endbg, endbg_rect)
            text(window, 'The end!', 72, RED,'Arial', WIDTH//2, HEIGHT//2)
            text(window, 'Player 1 is dead!', 40, RED, 'Arial', WIDTH//2, HEIGHT//2+50)
            pygame.display.update()
    if game == 2:
        window.blit(endbg, endbg_rect)
        text(window, 'The end!', 72, RED,'Arial', WIDTH//2, HEIGHT//2)
        text(window, 'Player 2 is dead!', 40, RED, 'Arial', WIDTH//2, HEIGHT//2+50)
        pygame.display.update()
    if game == 4:
        window.blit(menuESCbg, menuESCbg_rect)
        text(window, '==PAUSE==', 80, VIOLET, 'Arial', WIDTH//2, HEIGHT//2-100)
        text(window, '|Continue |C|', 40, INDIGO, 'Arial', WIDTH//2, HEIGHT//2)
        text(window, '|Exit to main menu |M|', 40, INDIGO, 'Arial', WIDTH//2, HEIGHT//2+50)
        text(window, '|Exit to desktop|Q|', 40, INDIGO, 'Arial', WIDTH//2, HEIGHT//2+100)
        pygame.display.update()

        
pygame.quit()
#V0.5.2
