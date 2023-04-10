import importantFunctions as impf
import time

N = 10**7
primes = set(impf.generatePrimes(N))

mini = 10_000
mval = 1
start = time.time()
for i in range(2, N):
    if i in primes:
        continue
    tot = impf.totient(i)
    T = "".join(sorted(str(tot)))
    if T == "".join(sorted(str(i))):
        print(i, tot)
        if i/tot < mini:
            mini = i/tot
            mval = i
            print("NEW MINIMUM")

print(mval, mini)
print(f"Completed in {time.time()-start} seconds")