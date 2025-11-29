#loop e uma estrutura de repeticao que permanece enquando um fato for verdadeiro

lista = [1,2,3,4,5]

for elemento in lista:
    print(elemento)
    
tupla = (1,2,3,4,5)

for elemento in tupla:
    print(elemento)
    
pessoa = {"nome": " Joao", "cidade": "Sorocaba"}

for chaves in pessoa.values():
    print(chaves)

for chave, valor in pessoa.items():
    print(f"{chave}: {valor}")
    
# range(): Intervalo numerico 
for element in range(5):
    print(element)
    
for indice in range(0, len(lista)):
    print("Indice: ", indice)
    print("elemento: ", lista[indice])
    if indice == 3:
        lista[indice] = 5
    print("Lista modificada", lista[indice])
    
# enumerate()

lista_enumerate = ["a","b", "c"]
 
for elementos in enumerate(lista_enumerate):
     print(f"{elementos}")