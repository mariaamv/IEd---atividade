nomes = []
cidades = {}
transporte = {}

while True:
    continuar = input ("\nDeseja adicionar um usuário? (sim/não): " )
    if continuar != "sim":
        break 
    
    nome = input ("Digite o seu nome: ")
    cidade = input ("Onde você mora? ")
    tem_transporte = input ("Tem transporte? (sim/não): ")

    nomes.append(nome)
    cidades[nome] = cidade

    if tem_transporte == "sim":
        tipo_transporte = input ("Qual o seu transporte? ")
        transporte[nome] = f"Tem transporte: {tipo_transporte}"
    else:
        transporte[nome] = "Não tem transporte"
    
    continuar = input ("Deseja adicionar outro usuário? (sim/não): " )
    if continuar != "sim":
        break  
    
    print("\nNomes registrados:", nomes)
    print("Cidades registradas:", cidades)
    print("Status de transporte:" )
    for nome in nomes:
        print(f"{nome}: {transporte[nome]}")
        
 