def saudacao(nome):
    print(f"ola, {nome}")

print("\n Chamando a funcao:")

nome = input("\n Qual o seu nome")
saudacao(nome)

# Funcao com retorno

def quadrado(numero):
    resultado = numero ** 2
    return resultado 

print("\n Chamando funcao quadrado")

resultado_quadrado = quadrado(3)
print("\n Resultado da funcao quadrado", resultado_quadrado)

# Funcao com multiplos parametros 

def soma(numero1, numero2):
    resultado = numero1 + numero2
    return resultado

print("Chamada da funcao soma", soma(2,5))