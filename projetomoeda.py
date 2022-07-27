import moeda

n = int(input('Digite um valor:'))
x = int(input('Digite a porcentagem para aumentar o valor n:'))
y = int(input('Digite a porcentagem para diminuir o valor n:'))
print(f'A metade de {n} é {moeda.half(n)}.')
print(f'O dobro de {n} é {moeda.dobro(n)}.')
print(f'Aumentando {n} em {x}% temos {moeda.aumenta(n,x)}.')
print(f'Diminuindo {n} em {y}% temos {moeda.diminui(n,y)}.')