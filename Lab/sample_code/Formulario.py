import time

print("Qual é o seu nome?")
nome = input()
# print("Ola %s, é um prazer " % nome)
# data_nasc = input("Insira a sua data de nascimento (dia/mês/ano): ")
print("Insira a sua data de nascimento (dia/mês/ano): ", end="")
dia_nasc, mes_nasc, ano_nasc = input().split("/")
dia_nasc, mes_nasc, ano_nasc = int(dia_nasc), int(mes_nasc), int(ano_nasc)

print()
print(dia_nasc, "->", type(dia_nasc))
print(mes_nasc, "->", type(mes_nasc))
print(ano_nasc, "->", type(ano_nasc))



# Como calcular a idade com base na data de nascimento?
print()
print("---Current time---")
print("Current time in seconds passed since 1970:", time.time())
print(time.localtime(time.time()))
ano_curr = time.localtime(time.time())
print(ano_curr.tm_year)
# method 1
System_time1 = time.asctime(time.localtime(time.time()))
print("\nAsctime function output:", System_time1)
# method 2
System_time2 = time.ctime(time.time())
print("\nCtime function output:", System_time2)

idade = ano_curr.tm_year - ano_nasc
if ano_curr.tm_mon < mes_nasc:
    idade = idade - 1
elif ano_curr.tm_mon == mes_nasc:
    if ano_curr.tm_mday < dia_nasc:
        idade = idade - 1

if idade < 0:
    print("\nData de nascimento introduzida invalida !")
else:
    print()
    if ano_curr.tm_mday == dia_nasc and ano_curr.tm_mon == mes_nasc:
        print("Feliz Aniversário %s !!!" % nome)
    print("Idade atual:", idade)
###
