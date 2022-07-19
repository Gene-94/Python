prim_nome = "Yevheniy"
seg_nome = "Kushnirenko"
nome = prim_nome + seg_nome
print(nome)
print(prim_nome + seg_nome)
print("Yevheniy" + "Kushnirenko")
print("Yevheniy", "Kushnirenko")
num=12
print("Yevheniy"+str(num))

print("O comprimento do meu nome é", len("Yevheniy"), "letras")
# print("O comprimento do meu nome é"+len("Yevheniy")+"letras") -> expressão invalida, soma inteiros com strings
print("O comprimento do meu nome é de "+str(len("Yevheniy"))+" letras")

a = 16
b = 35

print("São", a, ":", b, "horas")
# print("São"+a+":"+b+"horas") -> invalido pois são do tipo inteiro
print("São %d:%d horas" % (a, b))

print("repetir output: %d - %d - %d" % (a, a, a))


s = "Isto é uma string"
print(s[0])
print(s[-1])
print(s[7:10])
print(s[0:-1])
print(s[0:-1:3])
print(s[0::1])

print("\n")

print("Hello")
print("world")

print("Hello", end=" - ")
print("world")

print("Hello", end="")
print("world")

print("one", "two", "three", "four", "etc")
print("one", "two", "three", "four", "etc", sep=";")
print("one", "two", "three", "four", "etc", sep="\n")
