#@classmethod
#@staticmetod

class MinhaClasse:
    valor = 10 #atributo da classe
    def __init__(self, nome) -> None:
        self.nome = nome # atributo da instancia 
        
    # Requer uma instancia para ser chamado
    def metodo_instancia(self):
        return f"Metodo de instancia chamado para {self.nome}"
    
    @classmethod #Cria um metodo para a classe inves da instancia, mas precisa se lembrar de adicionar a `cls` como parametro que faz referencia a classe
    def metodo_classe(cls):
        return f"Metodo da classe chamando para valor = {cls.valor} "       
    
    @staticmethod # um metodo que nao recebe a referencia da classe 
    def metodo_estatico(): 
        return f"Metodo estatico chamando "
    
class Carro:
    def __init__(self, marca, modelo, ano) -> None:
        self.marca = marca
        self.modelo = modelo
        self.ano = ano
        
    @classmethod
    def criar_carro(cls, configuracao):
        marca, modelo, ano = configuracao.split(",")
        return cls(marca, modelo, int(ano))
            

class Matematica:
    @staticmethod
    def somar(a, b):
        return a + b

configuracao = "Toyota,Corolla,2010" 
carro1 = Carro.criar_carro(configuracao)  
print(f"Carro modelo: {carro1.modelo}")
 

obj = MinhaClasse("Classe exemplo")
print(obj.nome)
print(obj.metodo_instancia())
print(MinhaClasse.valor) # Nao preciso de uma instancia para ter acesso a ao atributo da classe 
print(MinhaClasse.metodo_classe())

print(f"somar: {Matematica.somar(10,26)}")

