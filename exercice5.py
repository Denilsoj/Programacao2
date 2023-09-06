
numero = int(input("Digite um número inteiro: "))


if numero <= 1:
    print("Número não é primo.")
else:
    
    contador_divisores = 0

    
    for i in range(2, numero):
        if numero % i == 0:
            contador_divisores += 1
            break  
    
    if contador_divisores == 0:
        print(f"{numero} é um número primo.")
    else:
        print(f"{numero} não é um número primo.")
