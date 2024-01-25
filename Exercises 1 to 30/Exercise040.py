# Crie um programa que leia duas notas de um aluno e calcule sua média, mostrando uma mensagem no final, de acordo com a média atingida:
# - Média abaixo de 5.0: REPROVADO
# - Média entre 5.0 e 6.9: RECUPERAÇÃO
# - Média 7.0 ou superior: APROVADO


n1 = float(input("Input First grade: "))
n2 = float(input("Input Second grade: "))
avarage = (n1 + n2)/2

if avarage < 5: 
    print(f"Sua média foi {avarage}, você está reprovado!")
elif avarage <= 5 < 7:
    print(f"Sua média foi {avarage}, você está de recuperação!")
else:
    print(f"Sua média foi {avarage}, você está aprovado!")