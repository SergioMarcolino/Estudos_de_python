# Eventos que ocorrem durante o programa e pode iompedir do programa rodar
print("exemplo de captura de execoes")
try:
    numero = int(input("digite um numero "))
    resultado = 10 / numero

except ValueError as e:
    print(f"Erro de Value error {e}")
    raise ValueError("Tipo de variaveis incompativeis")
except Exception as e:
    print(f"Erro: {e}")
else: 
        print(resultado)
finally: 
    print("Operacao finalizada")

