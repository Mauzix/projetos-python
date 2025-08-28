nota1 = float (input ("digite nota 1\n"))
nota2 = float (input ("digite nota 2\n"))
media = (nota1 + nota2 ) /2
if nota1 >= 8:
    print("aprovado")
elif media <= 6:
    print ("recuperação")
else:
    print("reprovado")