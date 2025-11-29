class Animal:
    def __init__(self, nome) -> None:
        self.nome = nome
        
    def emitir_som(self):
        pass
    
class Mamifero(Animal):
    def amamentar(self):
        return f"{self.nome} esta amamentando."
    
class Ave(Animal):
    def voar(self):
        return f"{self.nome} esta voando."
    
class Morcego(Mamifero, Ave):
    def emitir_som(self):
        return "Morcegos emitem sons ultrasonicos"
        #return super().emitir_som() #Super e uma funcao padrao que chama a funcao da classe mae
    
Morcego = Morcego("Batman")

# Acessando metodos da classe base `Animal`
print(f"Nome do morcego{Morcego.nome}")
print(f"Som do morcego: {Morcego.emitir_som()}")

# Acessando metodos das classes `mamifero` e `Ave`
print(f"Morcego amamentando {Morcego.amamentar()}")
print(f"Morcego voando {Morcego.voar()}")
