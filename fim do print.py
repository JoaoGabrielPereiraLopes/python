import pygame
import random

# Inicialização do Pygame
pygame.init()

# Definições da tela
SCREEN_WIDTH = 1600
SCREEN_HEIGHT = 900
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("Flappy Bird")

# Definições de cores
WHITE = (255, 255, 255)
GREEN = (0, 255, 0)

# Definições do pássaro
BIRD_WIDTH = 34
BIRD_HEIGHT = 24
bird = pygame.Rect(50, SCREEN_HEIGHT//2 - BIRD_HEIGHT//2, BIRD_WIDTH, BIRD_HEIGHT)
bird_velocity = 0
GRAVITY = 0.5
FLAP_STRENGTH = -10

# Definições dos canos
PIPE_WIDTH = 70
PIPE_HEIGHT = random.randint(150, 400)
PIPE_GAP = 150
pipes = []
pipe_frequency = 1500  # milissegundos
last_pipe = pygame.time.get_ticks() - pipe_frequency

# Definições de pontuação
score = 0
font = pygame.font.SysFont(None, 36)

# Função para desenhar texto
def draw_text(text, font, color, surface, x, y):
    textobj = font.render(text, True, color)
    textrect = textobj.get_rect()
    textrect.topleft = (x, y)
    surface.blit(textobj, textrect)

# Função para desenhar o pássaro
def draw_bird():
    pygame.draw.rect(screen, GREEN, bird)

# Função para desenhar os canos
def draw_pipes():
    for pipe in pipes:
        pygame.draw.rect(screen, GREEN, pipe)

# Loop principal do jogo
running = True
clock = pygame.time.Clock()

while running:
    screen.fill(WHITE)

    # Eventos
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                bird_velocity = FLAP_STRENGTH

    # Atualização do pássaro
    bird_velocity += GRAVITY
    bird.y += bird_velocity

    # Criação de novos canos
    current_time = pygame.time.get_ticks()
    if current_time - last_pipe > pipe_frequency:
        pipe_height = random.randint(150, 400)
        top_pipe = pygame.Rect(SCREEN_WIDTH, 0, PIPE_WIDTH, pipe_height)
        bottom_pipe = pygame.Rect(SCREEN_WIDTH, pipe_height + PIPE_GAP, PIPE_WIDTH, SCREEN_HEIGHT - pipe_height - PIPE_GAP)
        pipes.append(top_pipe)
        pipes.append(bottom_pipe)
        last_pipe = current_time

    # Movimentação dos canos
    for pipe in pipes:
        pipe.x -= 5

    # Remoção de canos fora da tela e atualização de pontuação
    pipes = [pipe for pipe in pipes if pipe.x + PIPE_WIDTH > 0]

    for pipe in pipes:
        if pipe.x + PIPE_WIDTH == bird.x:
            score += 0.5

    # Verificação de colisão
    if bird.y > SCREEN_HEIGHT or bird.y < 0:
        running = False

    for pipe in pipes:
        if bird.colliderect(pipe):
            running = False

    # Desenho na tela
    draw_bird()
    draw_pipes()
    draw_text(f'Score: {int(score)}', font, GREEN, screen, 10, 10)

    pygame.display.flip()
    clock.tick(30)

pygame.quit()
