
import math

def prime(x):
    factors = False
    if x > 3:
        for i in range(2,-(x//-2)):
            if x%i == 0:
                factors = True
    return not factors

def reversible(x):
    return int(str(x)[::-1])

def reversible_prime():
    total = []
    x = 0
    while len(total) < 50:
        if prime(x):
            primesq = x*x
            rprimesq = reversible(primesq)
            if rprimesq != primesq:
                x2 = math.sqrt(rprimesq)
                if x2%1 == 0:
                    if prime(int(x2)):
                        total.append(primesq)
        x += 1
    return sum(total)

print(reversible_prime())