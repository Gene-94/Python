import copy

sub1 = [1, 2, 3]
sub2 = [4, 5, 6]
sub3 = [7, 8, 9]

lista1 = ['lista 1', sub1, sub2, sub3, 'fim']

lista2 = copy.copy(lista1)

lista3 = copy.deepcopy(lista1)

print(lista1)
print(lista2)
print(lista3)
### Output:
# ['lista 1', [1, 2, 3], [4, 5, 6], [7, 8, 9], 'fim']
# ['lista 1', [1, 2, 3], [4, 5, 6], [7, 8, 9], 'fim']
# ['lista 1', [1, 2, 3], [4, 5, 6], [7, 8, 9], 'fim']
### todos iguais

lista3[0] = "lista 3"
lista2[0] = "lista 2"
lista1[0] = "lista um"
lista1[0] = "fimfimfim"

print(lista1)
print(lista2)
print(lista3)
### Output:
# ['lista um', [1, 2, 3], [4, 5, 6], [7, 8, 9], 'fimfimfim']
# ['lista 2', [1, 2, 3], [4, 5, 6], [7, 8, 9], 'fim']
# ['lista 3', [1, 2, 3], [4, 5, 6], [7, 8, 9], 'fim']

sub2[0] = "teste_1"
sub2[1] = "teste_2"
sub2[2] = "teste_3"

print(lista1)
print(lista2)
print(lista3)
### Output:
# ['lista um', [1, 2, 3], ['teste_1', 'teste_2', 'teste_3'], [7, 8, 9], 'fimfimfim']
# ['lista 2', [1, 2, 3], ['teste_1', 'teste_2', 'teste_3'], [7, 8, 9], 'fim']
# ['lista 3', [1, 2, 3], [4, 5, 6], [7, 8, 9], 'fim']
### a alteração da sublista afetou a "shalow copy" -> lista2 mas não afetou a "deep copy" -> lista3