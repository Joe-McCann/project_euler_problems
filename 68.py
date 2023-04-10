import itertools

nums = list(range(1,10))

for x in itertools.permutations(nums):

    b = [[10,x[0],x[1]], [x[2], x[1], x[3]], [x[4], x[3], x[5]], [x[6], x[5], x[7]], [x[8], x[7], x[0]]]
    s = set([sum(y) for y in b])

    if len(s) > 1:
        continue

    else:
        print(b, s)
