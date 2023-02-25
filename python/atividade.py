'''Faça um programa para leitura de três notas parciais de um aluno e sua disciplina. 
Oprograma deve calcular a médida alcançada por aluno e apresentar:

a) A mensagem "Aprovado", se a média for maior ou igual a 7, com aa respectiva média alcançada;
b) A mensagem "Reprovado", se a média for menor do que 7, com a respectiva média alcançad;
c) A mensagem "Aprovada" com Distinção, se a média for igual a 10.'''


print('Média das notas')
num1 = float(input('Nota 1:'))
num2 = float(input('Nota 2:'))
num3 = float(input('Nota 3:'))

soma = (num1 + num2 + num3) / 3
print("Sua media é",round(soma,2))

if soma < 7:
    print("Reprovado!")
elif soma == 10:
    print("Aprovado com Distinção")
else:
    print("Aprovado")