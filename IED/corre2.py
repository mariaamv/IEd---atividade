Pessoas = []  

def adicionar():
     nome = input ("Digite o seu nome ")
     idade = input ("Qual a sua idade? ")
     cidade = input ("Digite a sua cidade: ")
     Pesssoa =  {"Nome": nome, "idade": idade, "cidade": cidade}  
     
     Pessoas.append(Pesssoa)
     
     while True:
       tem_transporte = input ("\nVocê tem transporte? (sim/não): " ) .strip() .lower()
       if tem_transporte == "sim":
          print("Seviço inelegivel")
          break
       elif tem_transporte == "Não":
           adicionar()
       else:
           print("Opção inválida")    
           break
       print(Pessoas)
       
       
       
       
       
       
       
       
       
       
       
       
       
       
       
       
       
       
       
       
       
       
       
       
      