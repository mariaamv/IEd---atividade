
tarefas = []            # Lista principal de tarefas
historico = []          # Pilha para desfazer tarefas
fila_execucao = []      # Fila para executar tarefas

def adicionar_tarefa(tarefa): # Cria uma função através do comando "def" para adicionar tarefas.
    tarefas.append(tarefa) # O append serve para adicionar algo a uma variável.
    historico.append(tarefa) # Essa função permite desfazer a tarefa.
    fila_execucao.append(tarefa) # Essa função permite que as tarefas sejam atendidas uma depois da outra, ou seja, fila.
    print(f"Tarefa '{tarefa}' adicionada!\n") # Mostra uma mensagem dizendo que a tarefa foi adicionada.

def desfazer_ultima_tarefa(): # Cria uma função através do comando "def" para desfazer tarefas.
    if historico: # verifica se há tarefas para desfazer.
        ultima = historico.pop() # o pop permite remover a última tarefa do historico.
        tarefas.remove(ultima) # Remove a tarefa da lista principal de tarefas.
        fila_execucao.remove(ultima) # Remove a tarefa da fila de execução.
        print(f"Tarefa '{ultima}' desfeita!\n") # Mostra uma mensagem dizendo que a tarefa foi desfeita.
    else:
        print("Nenhuma tarefa para desfazer.\n") # Essa mensagem é caso não tenha tarefas no historico para serem desfeitas.

def atender_tarefa(): # cria uma função através do comando "def" para atender uma tarefa, ou seja, remove a primeira tarefa da fila de execução.
    if fila_execucao: # Verifica se há tarefas na fila de execução.
        feita = fila_execucao.pop(0) # remove a primeira tarefa da fila
        tarefas.remove(feita) # remove as tarefas que já foram executacadas
        print(f"Tarefa '{feita}' atendida!\n") # Mostra uma mensagem dizendo que a tarefa foi atendida.
    else:
        print("Nenhuma tarefa para atender.\n") # essa mensagem é caso não tenha tarefas no historico para serem atendidas.

def mostrar_tarefas(): # cria uma função através do comando "def" para mostrar tarefas que já foram executadas.
    print("\n📋 Lista de Tarefas:") # Essa é uma função para mostrar a lista de tarefas que já foram feitas.
    for i, t in enumerate(tarefas): # Itera sobre a lista de tarefas, com um índice 'i' e a tarefa 't'
        print(f"{i + 1}. {t}") # Mostra o índice e a tarefa na tela.
    print()

while True:
    print("1. Adicionar Tarefa")
    print("2. Desfazer Última Tarefa")
    print("3. Atender Tarefa (modo fila)")
    print("4. Mostrar Tarefas")
    print("5. Sair")

    opcao = input("Escolha uma opção: ")

    if opcao == '1':
        tarefa = input("Digite a tarefa: ")
        adicionar_tarefa(tarefa)
    elif opcao == '2':
        desfazer_ultima_tarefa()
    elif opcao == '3':
        atender_tarefa()
    elif opcao == '4':
        mostrar_tarefas()
    elif opcao == '5':
        print("Saindo do programa...")
        break
    else:
        print("Opção inválida!\n")

 