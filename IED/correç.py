Pessoas = []

while True:
    
    nome = input ("Digite o seu nome: ")
    cidade = input ("Qual a sua cidade? ")
    tem_transporte = ("Você tem transporte? (sim/não) ")
    tipo_de_transporte = None
    
    if tem_transporte == "sim":
        tipo_transporte = {
        "tipo": input ("Qual o seu transporte? ")
        }
        
        Pessoa = {
            "nome": nome,
            "cidade": cidade,
            "transporte": tipo_de_transporte
        }
        
        Pessoas.append(Pessoa)
        
        continuar = input ("\nOutro usuário deseja dizer as suas informações? (sim/não): " )
        if continuar != "sim":
          break 
        
        print("\n Pessoas cadastrados:")
    for i, Pessoa in enumerate(Pessoas):
        print(f"nome:{Pessoa['nome']}")
        print(f"cidade:{Pessoa['cidade']}")
    
    for Pessoa in Pessoas:
        print (Pessoas)