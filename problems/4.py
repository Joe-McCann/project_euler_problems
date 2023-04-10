def isPallindrome(a):
    stra = str(a)
    index = -1
    for i in stra:
        if i != stra[index]:
            return False
        index -=1
    return True

biggest = 0
num = []

for i in range(100, 1000):
    for j in range(100, 1000):
        if isPallindrome(i * j):
            if(i*j > 100000):
                num.append(i*j)
            if (i * j) > biggest:
                biggest = i * j

for pal in set(num):
    print(pal)
print(len(set(num)))
print(biggest)
