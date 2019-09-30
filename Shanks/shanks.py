import math
import collections

def egcd(a, b):
    if a == 0:
        return (b, 0, 1)
    else:
        g, y, x = egcd(b % a, a)
        return (g, x - (b // a) * y, y)

def modinv(a, m):
    g, x, y = egcd(a, m)
    if g != 1:
        raise Exception('modular inverse does not exist')
    else:
        return x % m

def shank(n, a, b):
    L1 = {}
    L2 = {}
    m = math.ceil(math.sqrt(n))
    # print(m)
    x = pow(a,m) % (n+1)
    for j in range(m):
        L1[j] = pow(x, j) % (n+1) * 1.0
    # print(L1)
    for j in range(m):
        # print(modinv(pow(a,j), (n+1)))

        L2[j] = ((b* modinv(pow(a, j), (n+1))) % (n+1))* 1.0
    L1 = sorted(L1.items(), key=lambda kv: kv[1])
    L1 = collections.OrderedDict(L1) 
    L2 = sorted(L2.items(), key=lambda kv: kv[1])
    L2 = collections.OrderedDict(L2)

    pair1 = []
    for i,j in L1.items():
        # print(i, j)
        for x,y in L2.items():
            if j == y:
                pair1.append((i,j))
                pair1.append((x,y))
        # if len(pair1) == 2:
        #     break
    if len(pair1) == 0:
        result = 0
    else:
        result = (m * pair1[0][0] + pair1[1][0]) % n

    return result

if __name__ == '__main__':
    n = int(input("Enter the value of n (n+1 should be a prime): "))
    a = int(input("Enter the value of a: "))
    b = int(input("Enter the value of b: "))

    result = shank(n,a,b)
    if result == 0:
        print("No values found")
    else:
        print(str(a) + '^' + str(result) + ' mod '  + str(n+1) + ' = ' + str(b) + ' mod ' + str(n+1))
    # print("Verification: " + str(pow(a,result)%(n+1), b%(n+1)))
    

    