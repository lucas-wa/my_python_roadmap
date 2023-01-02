n = input();
nI = int(n);
res = "não";

prev = nI % 10;
nI = nI // 10;
act = nI % 10;

for i in range(len(n)):
    if act == prev:
        res = "sim";
        break;
    
    prev = act;
    nI = nI // 10;
    act = nI % 10;
    
print(res);