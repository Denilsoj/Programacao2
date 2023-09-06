
nome = input("Digite o nome (maior que 3 caracteres): ")
idade = int(input("Digite a idade (entre 0 e 150): "))
salario = float(input("Digite o salário (maior que zero): "))
sexo = input("Digite o sexo ('f' ou 'm'): ")
estado_civil = input("Digite o estado civil ('s', 'c', 'v', 'd'): ")

if len(nome) <= 3:
    print("Nome deve ter mais de 3 caracteres.")
elif idade < 0 or idade > 150:
    print("Idade fora do intervalo permitido.")
elif salario <= 0:
    print("Salário deve ser maior que zero.")
elif sexo not in ['f', 'm']:
    print("Sexo deve ser 'f' ou 'm'.")
elif estado_civil not in ['s', 'c', 'v', 'd']:
    print("Estado civil deve ser 's', 'c', 'v' ou 'd'.")
else:
    print("Informações válidas. Obrigado por fornecer os dados.")
