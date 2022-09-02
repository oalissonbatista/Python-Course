s = 0
for k in range (1, 500 + 1):
    if k % 2 != 0 and k % 3 == 0:
        s = s + k
print (s)