# Declaration

full_name = "Sergio Marcolino" # this variable is String, String is the variable value for text


# formatting
print("Nome completo (1a forma): ", full_name)
print("Nome completo (2a forma): " + full_name) # when used + there is no space 
print("Nome completo (3a forma): " + "Sergio" + " " + "Marcolino")
print("Nome completo (4a forma): " + "Sergio", "Marcolino")
print("Nome completo (5a forma): ", full_name )
print("Nome completo (6a forma): %s "  % full_name )
print(f"Nome completo (7a forma): {full_name}" )



nome = "Sergio"
sobrenome = "Marcolino"


nome_completo = "Sergio marcolino"

nome.upper()

nome.lower()

nome[0]
nome.count("S")

nome.find("S")

nome.encode()

nome.encode().decode()

nome.replace("S", "L")

telefone = "(19) 99188-0219"
telefone_replace = telefone.replace("(", "" ).replace(")", ""). replace("-", "")

print(telefone_replace)

texto = "-".join(nome)
print(texto)

print(full_name.split(" "))

n = "xSergiox"
print(n.strip("x"))
print(n.rstrip("x"))

print(nome_completo.startswith("Se"))

print("Se" in nome_completo)
print("Se" not in nome_completo)