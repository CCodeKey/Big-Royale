import pygame
import sys
# Tela de Batalha

SCREEN_WIDTH = 800
SCREEN_HEIGHT = 700
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("Big Royale")

WHITE = (255, 255, 255)
BLUE = (0, 0, 255)
GREEN = (0, 255, 0)
RED = (255, 0, 0)
GRAY = (128, 128, 128)
MARRON = (100, 49, 15)
CHAO_VERDE = (21, 86, 8)
AGUA = (11, 164, 241)
BLACK = (0,0,0)



# Configurações e classes para o jogo
class Elixir_:
    def __init__(self, valor=10):
        self.valor = valor

    def getElixir(self):
        return self.valor
    
    def setElixir(self, valorNovo):
        self.valor = valorNovo

def mostrar_elixir(texto):
            text = texto
            font2 = pygame.font.Font(None, 48)
            text_surface = font2.render((f"ELIXIR - {text}"), True, BLACK)  # Renderiza o texto
            screen.blit(text_surface, (20, 660)) 

class CampoDeBatalha:
    def __init__(self):
        self.objetos_no_campo = []

    def aplicar_efeito(self, carta):
        # Exemplo: adiciona um personagem ao campo de batalha baseado nos atributos da carta
        print(f"Aplicando {carta.nome} no campo de batalha")
        # Pode adicionar o objeto no campo aqui:
        self.objetos_no_campo.append(carta.atributos['tipo_personagem'])

    def atualizar(self):
        # Lógica para atualizar o estado dos objetos no campo (ex: movimento)
        for obj in self.objetos_no_campo:
            print(f"Atualizando {obj} no campo de batalha")

# Exemplo de inicialização de cartas e campo de batalha



class Torre:
    def __init__(self, vida, posicao, estilo):
        self.vida = vida
        self.posicao = posicao
        self.estilo = estilo

    def desenhar(self, screen):      
       #pygame.draw.rect(screen, BLUE, (170, 470, 50, 60))
        if self.estilo == "azul":
            cor = (0, 0, 255)  # Azul
            pygame.draw.rect(screen, cor, (self.posicao[0], self.posicao[1], 50, 60))
        elif self.estilo == "branco":
            cor = WHITE
            pygame.draw.circle(screen, cor, (self.posicao[0], self.posicao[1]), 30)  
        elif self.estilo == "vermelho":
            cor = (255, 0, 0)  # Vermelho
            pygame.draw.rect(screen, cor, (self.posicao[0], self.posicao[1], 50, 60))
        else:
            cor = (128, 128, 128)  # Cinza padrão
            pygame.draw.rect(screen, cor, (self.posicao[0], self.posicao[1], 50, 60))
        # Desenha um retângulo como a torre na posição (x, y)
        
    
class Carta:
    def __init__(self, nome, custo_elixir):
        self.nome = nome
        self.custo_elixir = custo_elixir
       


    
    def desenhar(self, screen, x, y):
        # Exibe a carta na tela como um retângulo com o nome
        pygame.draw.rect(screen, (255, 0, 0), (x, y, 70, 100))  # Cor vermelha para o exemplo
        font = pygame.font.Font(None, 24)
        text_surface = font.render(self.nome, True, (255, 255, 255))  # Texto branco
        screen.blit(text_surface, (x + 5, y + 40))  # Mostra o nome da carta
    
    # def usar(self, campo_de_batalha, elixir):
    #     if elixir >= self.custo_elixir:
    #         elixir -= self.custo_elixir  # Desconta o elixir
    #         print(f"{self.nome} usada! Custo: {self.custo_elixir} Elixir restante: {elixir}")
            
    #         campo_de_batalha.aplicar_efeito(self)
            # instancias = Elixir_(valor=elixir)
            # instancias.setElixir(elixir)
            # print("ELIXIR - ",instancias.getElixir())
            # mostrar_elixir(f"ELIXIR - {str(instancias.getElixir())}")

            # AQUI
    def usar(self, elixir_atual):
        if elixir_atual >= self.custo_elixir:
                elixir_atual -= self.custo_elixir  # Desconta o elixir
                print(f"{self.nome} usada! Custo: {self.custo_elixir}. Elixir restante: {elixir_atual}")
        else:
            print("Elixir insuficiente!")

        return elixir_atual  # Retorna o elixir atualizado

class Personagem:
    def __init__(self, posicao, velocidade):
        self.posicao = posicao
        self.velocidade = velocidade

    def mover_para(self, destino):
        # Código para mover o personagem para o destino
        pass


def area_de_batalha():
    def draw_card(x, y, color):
            pygame.draw.rect(screen, color, (x, y, 70, 100))

    global destino 
    global ponte
    global elixir_instancia
    personagem_pos = [410, 550]  # Posição inicial do personagem
    velocidade = 0.1  # Velocidade de movimento
    arrastando = False  # Estado de arrastar o personagem
    destino = None  # Posição destino do personagem
    ponte = None  # Posição da ponte a ser atravessada

    princesa_1_pos = (170, 40)
    princesa_2_pos = (SCREEN_WIDTH - 220, 70)
    ponte1_pos = None
    ponte2_pos = None
    
    elixir_instancia = Elixir_()  # Instância do Elixir, com valor inicial 10
    elixir_atual = elixir_instancia.getElixir()
    campo_de_batalha = CampoDeBatalha() 
    print(elixir_atual)

    
    # Carta_1 = Carta("Cavaleiro", 5, {"tipo_personagem": "guerreiro", "forca": 10, "vida": 100})



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
                elixir_atual = Carta_1.usar(elixir_atual)
                print(elixir_atual)
                elixir_instancia.setElixir(elixir_atual)
                

        draw_card(460, 580, RED)  # Exemplo de carta
        pygame.display.flip()

        if arrastando:
            personagem_pos[0], personagem_pos[1] = pygame.mouse.get_pos()  # Acompanha o mouse
            pygame.draw.circle(screen, WHITE, (personagem_pos[0], personagem_pos[1]), 20)
            pygame.display.flip()
            ponte1_pos = (195, 366)
            ponte2_pos = (SCREEN_WIDTH - 195, 366)
            ponte = ponte2_pos
            # instanci = Elixir_()  # Crie uma instância da classe Elixir_ com valor inicial 10
            # Carta_1.usar(campo_de_batalha, instanci.getElixir())  # Usando a carta e atualizando o elixir
            
            # campo_de_batalha.atualizar()
            Carta_1 = Carta("Cavaleiro", 5)


            
            
        mostrar_elixir(elixir_instancia.getElixir()) 

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

            pygame.draw.circle(screen, WHITE, (personagem_pos[0], personagem_pos[1]), 20)
            pygame.display.flip()
    
        
              # Define o destino para onde o personagem deve ir



        # def sua_area():
        #     rei = pygame.draw.circle(screen, WHITE, (410, 550), 30)
        #     princesa_1 = pygame.draw.rect(screen, BLUE, (170, 470, 50, 60))
        #     princesa_2 = pygame.draw.rect(screen, BLUE, (SCREEN_WIDTH - 220, 470, 50, 60))

        # def adversario():
        #     rei = pygame.draw.circle(screen, WHITE, (410, 40), 30)
        #     princesa_1 = pygame.draw.rect(screen, RED, (170, 70, 50, 60))
        #     princesa_2 = pygame.draw.rect(screen, RED, (SCREEN_WIDTH - 220, 70, 50, 60))

        # def deck(): 
        #     pygame.draw.rect(screen, MARRON, (440, 570, 350, 120))
        #     cart_4 = pygame.draw.rect(screen, RED, (700, 580, 70, 100))
        #     cart_3 = pygame.draw.rect(screen, RED, (620, 580, 70, 100))
        #     cart_2 = pygame.draw.rect(screen, RED, (540, 580, 70, 100))
        #     cart_1 = pygame.draw.rect(screen, RED, (460, 580, 70, 100))

        def pontes():
            ponte1 = pygame.draw.rect(screen, MARRON, (170, 250, 50, 100))
            ponte2 = pygame.draw.rect(screen, MARRON, (SCREEN_WIDTH - 220, 250, 50, 100))  

        def grama():
            agua = pygame.draw.rect(screen, AGUA, (0, 200, 800, 270))
            area_emcima = pygame.draw.rect(screen, CHAO_VERDE, (0, 0, 800, 270))
            area_embaixo = pygame.draw.rect(screen, CHAO_VERDE, (0, 330, 800, 400))
        
        font = pygame.font.Font(None, 30)
        def mostrar_vida_das_torres(texto, x, y, cor=BLACK):
            text_surface = font.render(texto, True, cor)  # Renderiza o texto
            screen.blit(text_surface, (x, y)) 

        

        grama()
        pontes()


        rei_vc = Torre(vida=300, posicao=(410, 550), estilo="branco")
        princesa_1_vc = Torre(vida=200, posicao=(170, 470), estilo="azul")
        princesa_2_vc = Torre(vida=200, posicao=(SCREEN_WIDTH - 220, 470), estilo="azul")

        rei_vc.desenhar(screen)
        princesa_1_vc.desenhar(screen)
        princesa_2_vc.desenhar(screen)

        rei_adv = Torre(vida=300, posicao=(410, 40), estilo="branco")
        princesa_1_adv = Torre(vida=200, posicao=(170, 70), estilo="vermelho")
        princesa_2_adv = Torre(vida=200, posicao=(SCREEN_WIDTH - 220, 70), estilo="vermelho")

        rei_adv.desenhar(screen)
        princesa_1_adv.desenhar(screen)
        princesa_2_adv.desenhar(screen)

        rei_vc_vida = mostrar_vida_das_torres(str(rei_vc.vida), 393, 544, BLACK)
        princesa_1_vc_vida = mostrar_vida_das_torres(str(princesa_1_vc.vida), 176, 490, WHITE)
        princesa_2_vc_vida = mostrar_vida_das_torres(str(princesa_2_vc.vida), SCREEN_WIDTH - 214, 490, WHITE)

        rei_adv_vida = mostrar_vida_das_torres(str(rei_adv.vida), 393, 32, BLACK)
        princesa_1_adv_vida = mostrar_vida_das_torres(str(princesa_1_adv.vida), 176, 90, WHITE)
        princesa_2_adv_vida = mostrar_vida_das_torres(str(princesa_2_adv.vida), SCREEN_WIDTH - 214, 90, WHITE)


        

        

        # Exemplo de carta
        # Carta_1 = Carta("Cavaleiro", 5, {"tipo_personagem": "guerreiro", "forca": 10, "vida": 100})

        # Usando a carta
        # elixir = Carta_1.usar(campo_de_batalha, elixir)  # Usando a carta e atualizando o elixir
        # campo_de_batalha.atualizar()  # Atualizando o campo de batalha com a nova carta
# Usando a carta e atualizando o elixir
        # instancia = Elixir_()  # Crie uma instância da classe Elixir_ com valor inicial 10



        # mostrar_elixir(f"ELIXIR - {str(instancia.getElixir())}")
        # #mostrar_elixir(f"ELIXIR - {str(instancia.getElixir())}")  # Usando a carta e atualizando o elixir
        # campo_de_batalha.atualizar() 
        # print("seu elixir agora -", instancia.getElixir())
        pygame.display.flip()


  