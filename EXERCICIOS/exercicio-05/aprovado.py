nota1 = float (input("digite sua primeira nota"))
nota2= float (input ("digite sua segunda nota"))
nota3 = float (input ("digite sua terceira nota"))
nota4 = float (input ("digite sua quarta nota"))
media = (nota1 + nota2 + nota3 + nota4) /4
if media >= 8:
    print (f"voce passou com media {media} parabens")
elif media >=4:
    print (f"que pena você ta de recuperação com media {media}")
else :
    print (f"tenta na proxima")