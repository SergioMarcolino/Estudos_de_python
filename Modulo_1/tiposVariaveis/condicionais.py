#Condicionais if, elif, else

#exemplo de if 

idade = int(input("Quantos anos voce tem?"))
print("Exemplo maior de 18")
if idade >= 18:
    print("Maior de 18")

elif idade >= 12:
    print("Voce e adolescente")
    
else:
    print("Menor de 18")
