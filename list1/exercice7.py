pergunta1 = input("Telefonou para vítima ?")
pergunta2 =  input("Esteve no local do crime ?")
pergunta4 = input("Mora perto da vitima ?")
pergunta5 = input("Devia para vitíma ?")
pergunta6 = input("Ja trabalhou para vítima ?")
acertos = 0


if pergunta1 == "s": 
    acertos = acertos + 1
if pergunta2 == "s":
    acertos = acertos + 1
if pergunta4 == "s":
    acertos = acertos + 1 
if pergunta5 == "s":
    acertos = acertos + 1 
if pergunta6 == "s":
     acertos = acertos + 1 

if acertos == 2:
    print("suspeita")
elif acertos == 3 or acertos == 4:
    print("Cúplice")
else :
    print("Cupado")