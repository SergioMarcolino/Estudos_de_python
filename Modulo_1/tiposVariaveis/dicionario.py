#Dicionario no python e uma collection nao ordenado de pares chave e valor 
pessoa = {"nome": "Joao", "idade": 30, "cidade": "Sorocaba"}

print(" Meu dicionario de exemplo: ", pessoa)

#Acessadno valores por chave
print("nome: ", pessoa["nome"])

pessoa["sobrenome"] = "silva"
print(pessoa)

pessoa["idade"] = 31
print(pessoa)

#metodos 

# Removendo um par chave valor
del pessoa["sobrenome"]
print(pessoa)

# keys(), values(), items()

chaves = list(pessoa.keys())
print("chaves do meu dicionario: ", chaves)
print("1a chave do meu dicionario: ", chaves[0])

#values()
valores = pessoa.values()
print(valores)

#items()

itens = list(pessoa.items())
print(itens)
print("primeiro par chave valor:", itens[0])
print("primeiro par chave valor: %s = %s" % (itens[0][0], itens[0][1]))

