
N = int(input("Digite a quantidade de números: "))


menor_valor = 1001  
maior_valor = -1 
soma_valores = 0  

for i in range(N):
    numero = float(input(f"Digite o {i+1}º número entre 0 e 1000: "))
    
    
    if numero < 0 or numero > 1000:
        print("Número fora do intervalo permitido. Tente novamente.")
        continue
    
    
    if numero < menor_valor:
        menor_valor = numero
    if numero > maior_valor:
        maior_valor = numero
    
   
    soma_valores += numero


print(f"Menor valor: {menor_valor}")
print(f"Maior valor: {maior_valor}")
print(f"Soma dos valores: {soma_valores}")
