import pygame
import sys

pygame.init()

ANCHO, ALTO = 600, 600
pantalla = pygame.display.set_mode((ANCHO, ALTO))
pygame.display.set_caption("Laberinto con Checkpoints y Colisiones")

BLANCO = (255, 255, 255)
NEGRO = (0, 0, 0)
AZUL = (0, 0, 255)
VERDE = (0, 255, 0)
ROJO = (255, 0, 0)


jugador_tam = 20
jugador = pygame.Rect(40, 40, jugador_tam, jugador_tam)


checkpoint = pygame.Rect(250, 300, 30, 30)
punto_final = pygame.Rect(550, 550, 30, 30)


paredes = [
    pygame.Rect(0, 0, 600, 20), pygame.Rect(0, 0, 20, 600), pygame.Rect(580, 0, 20, 600), pygame.Rect(0, 580, 600, 20),
    pygame.Rect(60, 60, 120, 20), pygame.Rect(180, 60, 20, 100), pygame.Rect(100, 140, 100, 20),
    pygame.Rect(100, 140, 20, 100), pygame.Rect(100, 240, 120, 20), pygame.Rect(220, 140, 20, 100),
    pygame.Rect(220, 140, 100, 20), pygame.Rect(300, 60, 20, 100), pygame.Rect(320, 140, 120, 20),
    pygame.Rect(420, 140, 20, 100), pygame.Rect(340, 240, 100, 20), pygame.Rect(340, 240, 20, 100),
    pygame.Rect(340, 340, 120, 20), pygame.Rect(460, 240, 20, 100), pygame.Rect(460, 240, 100, 20),
    pygame.Rect(540, 340, 20, 100), pygame.Rect(440, 440, 120, 20), pygame.Rect(440, 440, 20, 100),
    pygame.Rect(340, 540, 100, 20), pygame.Rect(340, 540, 20, 40), pygame.Rect(220, 540, 100, 20),
    pygame.Rect(220, 540, 20, 40), pygame.Rect(100, 540, 100, 20), pygame.Rect(100, 440, 20, 100),
    pygame.Rect(100, 440, 100, 20), pygame.Rect(200, 340, 20, 100), pygame.Rect(200, 340, 100, 20),
]


velocidad = 5
checkpoint_alcanzado = False
posicion_inicial = (40, 40)
posicion_checkpoint = (250, 300)


corriendo = True
while corriendo:
    pantalla.fill(BLANCO)
    for evento in pygame.event.get():
        if evento.type == pygame.QUIT:
            corriendo = False

    teclas = pygame.key.get_pressed()
    movimiento_x, movimiento_y = 0, 0
    if teclas[pygame.K_LEFT]:
        movimiento_x = -velocidad
    if teclas[pygame.K_RIGHT]:
        movimiento_x = velocidad
    if teclas[pygame.K_UP]:
        movimiento_y = -velocidad
    if teclas[pygame.K_DOWN]:
        movimiento_y = velocidad

    nuevo_jugador = jugador.move(movimiento_x, movimiento_y)

    colision = False
    for pared in paredes:
        if nuevo_jugador.colliderect(pared):
            colision = True
            break

    if colision:
        if checkpoint_alcanzado:
            jugador.topleft = posicion_checkpoint
        else:
            jugador.topleft = posicion_inicial
    else:
        jugador = nuevo_jugador

    if jugador.colliderect(checkpoint):
        checkpoint_alcanzado = True

    if jugador.colliderect(punto_final):
        print("¡Has completado el laberinto!")
        corriendo = False

    pygame.draw.rect(pantalla, AZUL, jugador)
    pygame.draw.rect(pantalla, VERDE, checkpoint)
    pygame.draw.rect(pantalla, ROJO, punto_final)
    for pared in paredes:
        pygame.draw.rect(pantalla, NEGRO, pared)

    pygame.display.flip()
    pygame.time.delay(30)

pygame.quit()
sys.exit()
