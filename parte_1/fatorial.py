res = n = int(input());

if n == 0:
    print(1);
else:

    while n > 1:
        res = res * (n-1);
        n-=1;

    print(res);
