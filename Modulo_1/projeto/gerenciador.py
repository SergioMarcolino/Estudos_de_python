def adicionar_tarefa(tarefas, nome_tarefa):
    
    tarefa = {"tarefa": nome_tarefa, "completada": False}
    tarefas.append(tarefa)
    
    return print(f"A tarefa {nome_tarefa} foi adicionada com sucesso")

def ver_tarefas(tarefas):
    print("\n Lista de tarefas: ")
    
    for indice, tarefa in enumerate(tarefas, start=1):
        status = "fi" if tarefa["completada"] else ""
        nome_tarefa = tarefa["tarefa"]
        print(f"{indice}. [{status}] {nome_tarefa}")

def atualizar_nome_tarefa(tarefas,indice, novo_nome_tarefa):
    indice_tarefa_ajustado = int(indice_tarefa) - 1
    if indice_tarefa_ajustado >=0 and indice_tarefa_ajustado < len(tarefas):
        tarefas[indice_tarefa_ajustado]["tarefa"] = novo_nome_tarefa 
        print(f"Tarefa {indice} atualizada para {novo_nome_tarefa}")
    else:
        print("Indice de tarefa invalido")
    return

def completar_tarefa(tarefas, indice):
    indice_tarefa_ajustado = int(indice) - 1
    tarefas[indice_tarefa_ajustado]["completada"] = True
    print(f"Tarefa {indice} marcada como completada")
    return
def deletar_tarefas_completadas(tarefas):
    for tarefa in tarefas:
        if tarefa["completada"] == True:
            tarefas.remove(tarefa)
    print("Tarefas deletadas ")
    return

tarefas = []

while True:
    print("\n Menu do Gerenciador de lista de tarefas:")
    print("1. Adicionar tarefa")
    print("2. ver tarefas")
    print("3. Atualizar tarefa")
    print("4. Completar tarefa")
    print("5. Deletar tarefas completadas")
    print("6. Sair")

    escolha = input("Digite a sua escolha: ")
    if escolha == "1":
        nome_tarefa = input("Digite o nome da tarefa que deseja adicionar: ")
        adicionar_tarefa(tarefas,nome_tarefa)
    elif escolha == "2":
        ver_tarefas(tarefas)
    elif escolha == "3":
        ver_tarefas(tarefas)
        indice_tarefa = input("\n escolha o indice da tarefa que deseja aletrar. ")  
        novo_nome_tarefa = input("Qual sera o novo nome da tarefa? ") 
        atualizar_nome_tarefa(tarefas,indice_tarefa, novo_nome_tarefa)
    elif escolha == "4":
        ver_tarefas(tarefas)
        indice_tarefa = input("Digite o numero da tarefa que deseja completar ")
        completar_tarefa(tarefas,indice_tarefa)
    elif escolha == "5":
        ver_tarefas(tarefas)
        deletar_tarefas_completadas(tarefas)

    elif escolha == "6":
        break
    
print("Programa finalizado")
