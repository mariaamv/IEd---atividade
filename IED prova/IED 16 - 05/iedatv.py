
nomes = []  # Lista de nomes
cidades = {}  # Dicionario para cidades
transporte = {}  # Dicionario para transporte

nome = input("Digite o seu nome: ") # o usuário digita o seu nome
cidade = input("Digite a sua cidade: ") # o usuário digita a sua cidade
tem_transporte = input("Você tem transporte? (sim/não) ") # o usuário responde se tem transporte ou não

nomes.append(nome)  # adiciona o nome à lista de nomes
cidades[nome] = cidade  # adiciona a cidade associada ao nome no dicionário


if tem_transporte == "sim": 
    tipo_transporte = input("Qual o seu transporte? ") # se a resposta for sim, o usuário vai falar qual o transporte.
    transporte[nome] = f"Tem transporte: {tipo_transporte}" # adiciona o tipo de transporte
else:
    transporte[nome] = "Não tem transporte" # caso a resposta seja não

# Dados armazenados
print("\nNomes registrados:", nomes) 
print("Cidades registradas:", cidades)
print("Status de transporte:")
for nome in nomes:
    print(f"{nome}: {transporte[nome]}")
