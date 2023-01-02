n = input();
nI = int(n);
sum = 0;

for j in range(len(n)):
    sum += nI % 10;
    nI = nI // 10;

print(sum);
