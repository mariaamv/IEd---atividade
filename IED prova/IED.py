tarefas = []            # Lista principal de tarefas
historico = []          # Pilha para desfazer tarefas
fila_execucao = []      # Fila para executar tarefas
lista_tarefas = []      # Lista para armazenar tarefas

def salvar_lista_txt(): # Cria a função através do comando "def" para salvar o arquivo em .txt.
    with open("tarefas.txt", "w", encoding="utf-8") as arquivo: # O modo "w" apaga o conteúdo anterior do arquivo, se ele já existir. O parâmetro 'encoding="utf-8"' garante que caracteres especiais (acentos, ç etc.) sejam salvos corretamente
        for tarefa, prio, data in lista_tarefas: # percorre cada item da lista 'lista_tarefas'. Cada item deve ser uma tupla contendo: (tarefa, prioridade, data).
            arquivo.write(f"{tarefa};{prio};{data}\n") # Escreve no arquivo uma linha com os dados da tarefa, separados por ponto e vírgula.

def adicionar_tarefa(tarefa): # Cria uma função através do comando "def" para adicionar tarefas.
    prio = input("Digite a prioridade da tarefa: ") # O usuário vai colocar qual a prioridade da sua tarefa.
    data = input("Digite a data da sua tarefa: ") # O usuário vai decidir o prazo de sua tarefa.
    tarefa_completa = (tarefa, prio, data) # Uma tupla que é imutável, que não pode ser mudada.
    lista_tarefas.append(tarefa_completa) # Adiciona a tarefa completa (com descrição, prioridade e data) à lista de tarefas completas.
    tarefas.append(tarefa) # O append serve para adicionar algo a uma variável.
    historico.append(tarefa) # Essa função permite desfazer a tarefa.
    fila_execucao.append(tarefa) # Essa função permite que as tarefas sejam atendidas uma depois da outra, ou seja, fila.
    salvar_lista_txt() # Chamada da função.
    print(f"Tarefa '{tarefa}' adicionada!\n") # Mostra uma mensagem dizendo que a tarefa foi adicionada.

def desfazer_ultima_tarefa(): # Cria uma função através do comando "def" para desfazer tarefas.
    if historico: # verifica se há tarefas para desfazer.
        ultima = historico.pop() # O pop permite remover a última tarefa do historico.
        tarefas.remove(ultima) # Remove a tarefa da lista principal de tarefas.
        fila_execucao.remove(ultima) # Remove a tarefa da fila de execução.
        print(f"Tarefa '{ultima}' desfeita!\n") # Mostra uma mensagem dizendo que a tarefa foi desfeita.
    else:
        print("Nenhuma tarefa para desfazer.\n") # Essa mensagem é caso não tenha tarefas no historico para serem desfeitas.

def atender_tarefa(): # Cria uma função através do comando "def" para atender uma tarefa, ou seja, remove a primeira tarefa da fila de execução.
    if fila_execucao: # Verifica se há tarefas na fila de execução.
        feita = fila_execucao.pop(0) # Remove a primeira tarefa da fila
        tarefas.remove(feita) # Remove as tarefas que já foram executacadas
        print(f"Tarefa '{feita}' atendida!\n") # Mostra uma mensagem dizendo que a tarefa foi atendida.
    else:
        print("Nenhuma tarefa para atender.\n") # Essa mensagem é caso não tenha tarefas no historico para serem atendidas.

def mostrar_tarefas(): # Cria uma função através do comando "def" para mostrar tarefas que já foram executadas.
    print("\n📋 Lista de Tarefas:") # Essa é uma função para mostrar a lista de tarefas que já foram feitas.
    for i, t in enumerate(lista_tarefas): # Itera sobre a lista de tarefas, com um índice 'i' e a tarefa 't'
      tarefa, prio, data = t # Desempacota a tupla 't' em três variáveis: tarefa, prio (prioridade) e data, e também armazena essa mesma tupla na variável 'tarefa_completa'.
      print(f"{i + 1}. {tarefa} - Prioridade: {prio} - Data: {data}")  # Vai mostrar a tarefa, prioridade e data.
    print()

while True:
    print("1. Adicionar Tarefa") 
    print("2. Desfazer Última Tarefa") 
    print("3. Atender Tarefa (modo fila)") 
    print("4. Mostrar Tarefas") 
    print("5. Sair") 

    opcao = input("Escolha uma opção: ") # Função de escolher uma das opções.

    if opcao == '1':
        tarefa = input("Digite a tarefa: ") # Aqui o usuário digitas a ou as tarefas.
        adicionar_tarefa(tarefa)
    elif opcao == '2':
        desfazer_ultima_tarefa() # Opção de desfazer a tarefa.
    elif opcao == '3':
        atender_tarefa() # Opção de atender a tarefa.
    elif opcao == '4':
        mostrar_tarefas() # Opção de mostrar tarefas.
    elif opcao == '5':
        print("Saindo do programa...") # O programa e o loop está sendo encerrado.
        break
    else:
        print("Opção inválida!\n") # Mensagem para opção incorreta

 