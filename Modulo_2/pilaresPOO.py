#Primeiro pilar Heranca, fazer com que uma classe filha receba atributos ou funcoes da classe mae
print("\m Exemplo de heranca:")
class Animal:
    def __init__(self, nome) -> None:
        self.nome = nome
    def andar(self):
        print(f"O animal {self.nome} andou")
        return
    def emitir_som(self1): # classe generica 
        pass
    
class Cachorro(Animal):
    def emitir_som(self1):
        return "Au, au" # Polimorfismo, uso de uma funcao da classe mae que se modifica para sua classe filha 
    
class Gato(Animal):
    def emitir_som(self1):
        return "Miau!"

dog = Cachorro("Rex")
cat = Gato("Lex")

print("\n Exemplo de polimorfismo")

animais = [dog, cat]
for animal in animais:
    print(f"{animal.nome} faz: {animal.emitir_som()}")

print("\n Exemplos de encapsulamento")

class ContaBancaria:
    def __init__(self, saldo) -> None:
        self.__saldo = saldo # Encapsulamento, Atributo privado, usasse __ underline duplo para tornalo privado
        
    def depositar(self, valor):
        if valor > 0:
            self.__saldo += valor
            
    def sacar(self, valor):
        if valor > 0 and valor <= self.__saldo:
            self.__saldo -= valor
    
    def consultar_saldo(self):
        return self.__saldo

conta = ContaBancaria(1000)
print(f"Saldo da conta bancaria: {conta.consultar_saldo()}")
conta.depositar(20)
print(f"Saldo da conta bancaria: {conta.consultar_saldo()}")
conta.sacar(1000)
print(f"Saldo da conta bancaria: {conta.consultar_saldo()}")


#Abstracao, seve para ser um molde as outras classes
print("\n Exemplo da abstracao")
from abc import ABC, abstractmethod

class Veiculo(ABC):
    
    @abstractmethod
    def ligar(self):
        pass
    @abstractmethod
    def desligar(self):
        pass
    
class Carro(Veiculo):
    def __init__(self) -> None:
       pass
   
    def ligar(self):
        return "Carro ligado"
    
    def desligar(self):
        return "Carro desligado"
   
carro_amarelo = Carro()

print(carro_amarelo.desligar())
 
 
