n = int(input());
div = 2;

for i in range(2, n):
    if n % i == 0:
        div+=1;

if div == 2:
    print("primo");
else:
    print("não primo")