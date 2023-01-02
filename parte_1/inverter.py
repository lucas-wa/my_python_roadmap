n = int(input("Digite um numero: "))
list = []

while n != 0:
    list.append(n)
    n = int(input("Digite um numero: "))

print()

for idx in range(len(list) - 1, -1, -1):
    print(list[idx])

