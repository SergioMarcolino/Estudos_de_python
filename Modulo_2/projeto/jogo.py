import random

# personagem: classe mae
# Heroi: controlado pelo usuario
# Inimigo: adversario do usuario

class Personagem:
    def __init__(self, nome, vida, nivel) -> None:
        self.__nome = nome
        self.__vida = vida
        self.__nivel = nivel
        
    def get_nome(self):
        return self.__nome
    
    def get_vida(self):
        return self.__vida

    def get_nivel(self):
        return self.__nivel
    
    def exibir_detalhes(self):
        return f"Nome: {self.get_nome()}\n Vida: {self.get_vida()}\n Nivel: {self.get_nivel()}"
    
    def atacar(self,alvo):
        dano = random.randint(self.get_nivel() * 2, self.get_nivel() * 4 )
        print(f"{self.get_nome()} atacou {alvo.get_nome() } e causou {dano} de dano!")
        alvo.receber_dano(dano)
    
    def receber_dano(self, dano):
        self.__vida -= dano
        if self.__vida <= 0:
            self.__vida = 0
    
class Heroi(Personagem):
    def __init__(self, nome, vida, nivel, habilidade):
        super().__init__(nome, vida, nivel)
        self.__habilidade = habilidade
        
    def exibir_detalhes(self):
        return f"{super().exibir_detalhes()}\n Habilidade: {self.get_habilidade()}"
        
    def get_habilidade(self):
        return self.__habilidade
    
    def ataque_especial(self,alvo):
        dano = random.randint(self.get_nivel() * 5, self.get_nivel() * 8 )
        print(f"{self.get_nome()} usou o ataque especial {self.get_habilidade()} e causou {dano} no {alvo.get_nome()}!")
        alvo.receber_dano(dano)
    
class Inimigo(Personagem):
    def __init__(self, nome, vida, nivel, tipo):
        super().__init__(nome, vida, nivel)
        self.__tipo = tipo
    def get_tipo(self):
        return self.__tipo
    
    def exibir_detalhes(self):
        return f"{super().exibir_detalhes()}\n Tipo: {self.get_tipo()}"
    
    
    
class Jogo:
    """Classe orquestradora do jogo"""
    
    def __init__(self):
        self.heroi = Heroi("Heroi", 100, 5, "Super forca")
        self.inimigo = Inimigo("Morcego", 75, 3, "Voador")

    def iniciar_batalha(self):
        """ Fazer a gestao da bvatalha em turnos """
        
        print("Iniciando a batalha!")
        input("Pressione enter para atacar...")
        while self.heroi.get_vida() > 0 and self.inimigo.get_vida() > 0:
            print("\n Detalhes dos personagens")
            print(self.heroi.exibir_detalhes())
            print(self.inimigo.exibir_detalhes())
            
            escolha = input("Escolha (1 - Ataque Normal, 2 - Ataque Especial):")
            
            if escolha == "1":
                self.heroi.atacar(self.inimigo)
            elif escolha == "2":
                self.heroi.ataque_especial(self.inimigo)
            else: 
                print("Escolha invalida, faca uma escolha valida")
                
            if self.inimigo.get_vida() > 0:
                self.inimigo.atacar(self.heroi)
                
        if self.heroi.get_vida() > 0:
            print("\n O heroi venceu a luta")
        else:
            print("\n Voce foi derrotado")
        
            
            
#Criar instancia do jogo e iniciar a batalha

jogo = Jogo()
jogo.iniciar_batalha()          