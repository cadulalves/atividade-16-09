numeros = []
numeros.append(10)
numeros.append(20)
numeros.append(30)
numeros.insert(1, 15)
print(numeros)
############################
lista = [5, 10, 15, 20, 25]
lista.remove(10)
lista.pop()
lista.pop(0)
print(lista)
############################
valores = [8, 3, 10, 1, 7]
print(f"Lista original: {valores}")

valores.sort()
print(f"Lista ordenada (crescente): {valores}")

valores.sort(reverse=True)
print(f"Lista ordenada (decrescente): {valores}")

valores.reverse()
print(f"Lista invertida: {valores}")
##############################
notas = [7.5, 8.0, 6.5, 9.0, 5.5]

quantidade_notas = len(notas)
maior_nota = max(notas)
menor_nota = min(notas)

print(f"Quantidade de notas: {quantidade_notas}")
print(f"Maior nota: {maior_nota}")
print(f"Menor nota: {menor_nota}")
