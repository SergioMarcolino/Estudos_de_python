#POO, pega o conceito da realidade para levalo ao programa


# Classe exemplo

class Pessoa:
    def __init__(self, nome, idade) -> None: # Construtor
        self.nome = nome 
        self.idade = idade
    
    def saudacao(self):
        return f"Ola, meu nomoe e {self.nome} e eu tenho {self.idade} anos"

# Objetos, instancias da classe 
pessoa1 = Pessoa("Sergio", 22) # Instancia da classe pessoa criada
mensagem = pessoa1.saudacao()
print(mensagem)

pessoa2 = Pessoa("Kau", 20)
mensagem = pessoa2.saudacao()
print(mensagem)