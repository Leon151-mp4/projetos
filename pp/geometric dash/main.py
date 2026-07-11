import pygame

#pygame setup:
pygame.init()
screen = pygame.display.set_mode((800, 600))
relogio = pygame.time.Clock()


#basic's configs:
g = 0.8
jumpe = -14

class Player:
    def __init__(self):
        self.rect = pygame.Rect(100, 300, 50, 50)
        self.image = pygame.image.load("pp/geometric dash/player.png")
        self.image = pygame.transform.scale(self.image, (50, 50))
        self.val_y = 0
        self.chao = False

    def jump(self):
        if self.chao:
            self.val_y = jumpe
            self.chao = False

    def update(self):
        self.val_y += g
        self.rect.y += self.val_y

        if self.rect.bottom >= 400:
            self.rect.bottom = 400
            self.val_y = 0
            self.chao = True
jogador = Player()
rodopiando = True

port_image = pygame.image.load("pp/geometric dash/dash.png")
port_image = pygame.transform.scale(port_image, (800, 600))

port_image2 = pygame.image.load("pp/geometric dash/ground.png")
port_image2 = pygame.transform.scale(port_image2, (800, 200))
while rodopiando:
    relogio.tick(60)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            rodopiando = False

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                jogador.jump()
            
    jogador.update()

    screen.blit(port_image, (0, 0))
    screen.blit(jogador.image, jogador.rect)
    screen.blit(port_image2, (0, 400) )

    pygame.draw.line(screen, (255,255, 255), (0,400), (800, 400),2)

    pygame.display.flip()

pygame.quit()