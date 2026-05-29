import pygame
import random
import time

# Inicializa a biblioteca PyGame
pygame.init()

# Configurações da Janela
pygame.display.set_caption("BUTANTAN GAME")
largura, altura = 1200, 800
tela = pygame.display.set_mode((largura, altura))
relogio = pygame.time.Clock()

# --- CORES (Padrão RGB) ---
verde_fundo = (34, 139, 34)  # Fundo: Verde escuro/suave
verde_brasil = (0, 255, 0)  # Cobra: Verde vibrante (diferente do fundo)
amarela = (255, 255, 0)  # Cobra: Amarelo
azul = (0, 0, 255)  # Fruta
branca = (255, 255, 255)  # Cabeça e Pontuação
vermelha = (255, 0, 0)  # Game Over

# Parâmetros vitais do jogo
tamanho_quadrado = 20
velocidade_jogo = 15  # Velocidade inicial padrão


def gerar_comida():
    comida_x = round(random.randrange(0, largura - tamanho_quadrado) / float(tamanho_quadrado)) * float(
        tamanho_quadrado)
    comida_y = round(random.randrange(0, altura - tamanho_quadrado) / float(tamanho_quadrado)) * float(tamanho_quadrado)
    return comida_x, comida_y


def desenhar_comida(tamanho, comida_x, comida_y):
    pygame.draw.rect(tela, azul, [comida_x, comida_y, tamanho, tamanho], border_radius=tamanho // 2)


def desenhar_cobra(tamanho, pixels):
    for indice, pixel in enumerate(pixels):
        if indice == len(pixels) - 1:
            # É a cabeça
            cor_atual = branca
        else:
            # Calcula a distância do pedaço até a cabeça para manter o padrão fixo
            distancia_da_cabeca = len(pixels) - 1 - indice

            # Alterna as cores baseado em par ou ímpar
            if distancia_da_cabeca % 2 != 0:
                cor_atual = verde_brasil
            else:
                cor_atual = amarela

        pygame.draw.rect(tela, cor_atual, [pixel[0], pixel[1], tamanho, tamanho], border_radius=tamanho // 2)


def desenhar_pontuacao(pontuacao):
    fonte = pygame.font.SysFont("Helvetica", 35)
    texto = fonte.render(f"Pontos: {pontuacao}", True, branca)
    tela.blit(texto, [1, 1])


def mostrar_mensagem_game_over():
    fonte_go = pygame.font.SysFont("Helvetica", 100, bold=True)
    texto_go = fonte_go.render("A COBRA FUMOU", True, vermelha)
    rect_texto = texto_go.get_rect(center=(largura // 2, altura // 2 - 50))
    tela.blit(texto_go, rect_texto)

    fonte_instrucoes = pygame.font.SysFont("Helvetica", 30)
    texto_instrucoes = fonte_instrucoes.render("Pressione C para Jogar de Novo ou S para Sair", True, branca)
    rect_instrucoes = texto_instrucoes.get_rect(center=(largura // 2, altura // 2 + 50))
    tela.blit(texto_instrucoes, rect_instrucoes)


def selecionar_velocidade(tecla, vel_x_atual, vel_y_atual):
    if tecla == pygame.K_DOWN and vel_y_atual != -tamanho_quadrado:
        return 0, tamanho_quadrado
    elif tecla == pygame.K_UP and vel_y_atual != tamanho_quadrado:
        return 0, -tamanho_quadrado
    elif tecla == pygame.K_RIGHT and vel_x_atual != -tamanho_quadrado:
        return tamanho_quadrado, 0
    elif tecla == pygame.K_LEFT and vel_x_atual != tamanho_quadrado:
        return -tamanho_quadrado, 0

    return vel_x_atual, vel_y_atual


def rodar_jogo():
    fim_jogo = False
    estado_game_over = False

    x = largura / 2
    y = altura / 2

    velocidade_x = 0
    velocidade_y = 0

    tamanho_cobra = 1
    pixels = []

    comida_x, comida_y = gerar_comida()

    # --- ACRESCENTADO --- Define a velocidade inicial desta partida específica
    velocidade_atual = velocidade_jogo

    while not fim_jogo:

        while estado_game_over:
            mostrar_mensagem_game_over()
            pygame.display.update()

            for evento in pygame.event.get():
                if evento.type == pygame.QUIT:
                    fim_jogo = True
                    estado_game_over = False
                if evento.type == pygame.KEYDOWN:
                    if evento.key == pygame.K_s:
                        fim_jogo = True
                        estado_game_over = False
                    if evento.key == pygame.K_c:
                        rodar_jogo()
                        return

        tela.fill(verde_fundo)

        for evento in pygame.event.get():
            if evento.type == pygame.QUIT:
                fim_jogo = True
            elif evento.type == pygame.KEYDOWN:
                velocidade_x, velocidade_y = selecionar_velocidade(evento.key, velocidade_x, velocidade_y)

        x += velocidade_x
        y += velocidade_y

        if x < 0 or x >= largura or y < 0 or y >= altura:
            estado_game_over = True

        pixels.append([x, y])
        if len(pixels) > tamanho_cobra:
            del pixels[0]

        for pixel in pixels[:-1]:
            if pixel == [x, y]:
                estado_game_over = True

        if x == comida_x and y == comida_y:
            tamanho_cobra += 1
            comida_x, comida_y = gerar_comida()
            # --- ACRESCENTADO --- Aumenta o ritmo a cada fruta coletada
            velocidade_atual += 0.5

        desenhar_cobra(tamanho_quadrado, pixels)
        desenhar_comida(tamanho_quadrado, comida_x, comida_y)
        desenhar_pontuacao(tamanho_cobra - 1)

        pygame.display.update()

        # --- MODIFICADO --- Agora o relógio dita o ritmo usando a velocidade progressiva
        relogio.tick(velocidade_atual)


# Inicia o jogo
rodar_jogo()