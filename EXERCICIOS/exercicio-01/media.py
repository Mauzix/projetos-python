nota1 = float (input ("Digite a primeira nota: "))
nota2 = float (input ("Digite a segunda nota: "))
media = (nota1 + nota2) /2
if media >= 7:
 print( f"parabens sua media foi {media} vc foi aprovado")
elif media <= 5:
 print( f"que pena sua media foi {media} vc foi reprovado")
else:
 print( f"sua media foi {media} vc esta de recuperacao")
