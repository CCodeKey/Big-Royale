import area_de_batalha as batle
import pygame
import sys

# Inicializa o Pygame
pygame.init()

# Definindo as cores
WHITE = (255, 255, 255)
BLUE = (0, 0, 255)
GREEN = (0, 255, 0)
RED = (255, 0, 0)
GRAY = (128, 128, 128)
MARRON = (100, 49, 15)
CHAO_VERDE = (21, 86, 8)
AGUA = (11, 164, 241)

# Configurando a tela
SCREEN_WIDTH = 800
SCREEN_HEIGHT = 700
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("Big Royale")

# Configurando a fonte
font = pygame.font.Font(None, 74)
global back_button
global button
# Função para desenhar o botão
def draw_button(text, color, x, y, width, height):
    pygame.draw.rect(screen, color, (x, y, width, height))
    text_surface = font.render(text, True, WHITE)
    text_rect = text_surface.get_rect(center=(x + width // 2, y + height // 2))
    screen.blit(text_surface, text_rect)

# Função para criar uma tela
def create_screen(background_color, button_text, button_action):
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            elif event.type == pygame.MOUSEBUTTONDOWN:
                if button.collidepoint(event.pos):
                    return button_action

        screen.fill(background_color)  # Cor de fundo da tela

        # Desenha o botão
        button_width = 240
        button_height = 60
        button_x = SCREEN_WIDTH - button_width - 20  # 20 pixels de margem da borda direita
        button_y = SCREEN_HEIGHT - button_height - 20  # 20 pixels de margem da borda inferior
        
        button = pygame.Rect(button_x, button_y, button_width, button_height)
        draw_button(button_text, GREEN, button.x, button.y, button.width, button.height)

        pygame.display.flip()

# Tela de Batalha
def area_de_batalha_BKP():
    def draw_card(x, y, color):
            pygame.draw.rect(screen, color, (x, y, 70, 100))
    global destino 
    global ponte
    personagem_pos = [410, 550]  # Posição inicial do personagem
    velocidade = 0.1  # Velocidade de movimento
    arrastando = False  # Estado de arrastar o personagem
    destino = None  # Posição destino do personagem
    ponte = None  # Posição da ponte a ser atravessada

    princesa_1_pos = (170, 40)
    princesa_2_pos = (SCREEN_WIDTH - 220, 70)
    ponte1_pos = (195, 366)
    ponte2_pos = (SCREEN_WIDTH - 195, 366)
    
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            elif event.type == pygame.MOUSEBUTTONDOWN:
                # Verifica se o mouse está em uma carta (posição do deck)
                if 460 <= event.pos[0] <= 530 and 570 <= event.pos[1] <= 670:  # posição da carta 1
                    arrastando = True  # Inicia o arraste

            elif event.type == pygame.MOUSEBUTTONUP:
                arrastando = False  # Para o arraste
                # Define o destino para a torre inimiga mais próxima
                if abs(event.pos[0] - princesa_1_pos[0]) < abs(event.pos[0] - princesa_2_pos[0]):
                    destino = list(princesa_1_pos)
                    ponte = ponte1_pos  # Ponte 1 para a princesa 1
                else:
                    destino = list(princesa_2_pos)
                    ponte = ponte2_pos  # Ponte 2 para a princesa 2

    
        if arrastando:
            personagem_pos[0], personagem_pos[1] = pygame.mouse.get_pos()  # Acompanha o mouse

        if ponte:
            if personagem_pos[0] < ponte[0]:  # Movimento horizontal até a ponte
                personagem_pos[0] += velocidade
            if personagem_pos[1] > ponte[1]:  # Movimento vertical até a ponte
                personagem_pos[1] -= velocidade
            if abs(personagem_pos[0] - ponte[0]) < velocidade and abs(personagem_pos[1] - ponte[1]) < velocidade:
                #ponte = None  # Para o movimento quando a ponte é alcançada
                ponte1_pos = (170, 150)
                ponte = ponte1_pos
                if ponte:
                    if personagem_pos[0] < ponte[0]:  # Movimento horizontal até a ponte
                        personagem_pos[0] += velocidade
                    if personagem_pos[1] > ponte[1]:  # Movimento vertical até a ponte
                        personagem_pos[1] -= velocidade
                    if abs(personagem_pos[0] - ponte[0]) < velocidade and abs(personagem_pos[1] - ponte[1]) < velocidade:
                        ponte = None 
                       
                # Depois que o personagem alcança a ponte, move em direção ao destino
                if personagem_pos[0] < destino[0]:  # Movimento horizontal para a torre
                     personagem_pos[0] += velocidade
                if personagem_pos[1] > destino[1]:  # Movimento vertical para a torre
                    personagem_pos[1] -= velocidade
                if abs(personagem_pos[0] - destino[0]) < velocidade and abs(personagem_pos[1] - destino[1]) < velocidade:
                    destino = None  # Para o movimento quando o destino é alcançado



            draw_card(460, 580, RED)  # Exemplo de carta
            pygame.draw.circle(screen, WHITE, (personagem_pos[0], personagem_pos[1]), 20)
            pygame.display.flip()  # Define o destino para onde o personagem deve ir



        def sua_area():
            rei = pygame.draw.circle(screen, WHITE, (410, 550), 30)
            princesa_1 = pygame.draw.rect(screen, BLUE, (170, 470, 50, 60))
            princesa_2 = pygame.draw.rect(screen, BLUE, (SCREEN_WIDTH - 220, 470, 50, 60))

        def adversario():
            rei = pygame.draw.circle(screen, WHITE, (410, 40), 30)
            princesa_1 = pygame.draw.rect(screen, RED, (170, 70, 50, 60))
            princesa_2 = pygame.draw.rect(screen, RED, (SCREEN_WIDTH - 220, 70, 50, 60))

        def deck(): 
            pygame.draw.rect(screen, MARRON, (440, 570, 350, 120))
            cart_4 = pygame.draw.rect(screen, RED, (700, 580, 70, 100))
            cart_3 = pygame.draw.rect(screen, RED, (620, 580, 70, 100))
            cart_2 = pygame.draw.rect(screen, RED, (540, 580, 70, 100))
            cart_1 = pygame.draw.rect(screen, RED, (460, 580, 70, 100))

        def pontes():
            ponte1 = pygame.draw.rect(screen, MARRON, (170, 250, 50, 100))
            ponte2 = pygame.draw.rect(screen, MARRON, (SCREEN_WIDTH - 220, 250, 50, 100))  

        def grama():
            agua = pygame.draw.rect(screen, AGUA, (0, 200, 800, 270))
            area_emcima = pygame.draw.rect(screen, CHAO_VERDE, (0, 0, 800, 270))
            area_embaixo = pygame.draw.rect(screen, CHAO_VERDE, (0, 330, 800, 400))

        grama()
        pontes()
        sua_area()
        deck()
        adversario()
        pygame.display.flip()


def main():
    current_screen = 'home'
    while True:
        if current_screen == 'home':
            current_screen = create_screen(BLUE, "Começar", 'game')
        elif current_screen == 'game':         
            current_screen = batle.area_de_batalha()


main()