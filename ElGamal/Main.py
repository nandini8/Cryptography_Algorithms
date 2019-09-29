import random
import re

def gen_primes():
    Buf = {}
    q = 2
    while True:
        if q not in Buf:
            yield q
            Buf[q * q] = [q]
        else:
            for p in Buf[q]:
                Buf.setdefault(p + q, []).append(p)
            del Buf[q]
        q += 1

def get_one_prime() -> object:
    #p
    for i in gen_primes():
        Buf = []
        if ((random.SystemRandom.random(i) >0.9) & (i>500 )):
            Buf.append(i)
            return random.choice(Buf)



def primary_primitive_root(input):
    #g
    Buf = random.SystemRandom().randrange(input)
    for i in range(Buf,input):
        if ((i**(input-1))%input == 1):
            return i

def private_key(input):
    #x
    Buf = [i for i in range(1,input)]
    return random.SystemRandom().choice(Buf)

def public_key(prime,g,x):
    #y
    Buf = (g**x) % prime
    if Buf == 1:
        return 3
    else:
        return Buf



def random_k(prime):
    #k
    Buf = [i for i in range(1, prime-1)]
    return random.SystemRandom().choice(Buf)

def encrypt(message,prime,x,g,y):
    Buf = []
    Buf1 = []
    l = list(message)
    for i,index in enumerate(message):
        k = random_k(prime)
        a = (g ** k) % prime
        b = ((y ** k)* ord(l[i])) % prime
        Buf.append(b)
        Buf1.append(a)
    return list(zip(Buf1,Buf))

def decrypt(emessage,prime,key):
    Buf = []
    for i in emessage:
        Buf.append(chr((i[1]*(i[0]**(prime-1-key)))%prime))
    return Buf

def prepare(emessage):
    Buf = []
    Buf1 = []
    ctr = 0
    l = list(emessage)
    result = re.split(r' ',emessage)
    for i in result:
        ctr = ctr + 1
        if (ctr%2 == 0):
            Buf1.append(int(i))
        else:
            Buf.append(int(i))
    return list(zip(Buf,Buf1))

def main():
    a = get_one_prime()
    g = primary_primitive_root(a)
    x = private_key(a)
    y = public_key(a, g, x)

    print("Our prime is: " + str(a))
    print("Our primary primitive root is(g): " + str(g))
    print("Our private key X is: " + str(x))
    print("Our public key Y is: " + str(y))

    decide = input("To encrypt type - 1, to decrypt - 2,both - 3:")

    if (decide == '1'):
        message = input("Type a message:")
        if message == '':
            print('Cant encrypt empty stroke')
        else:
            output = encrypt(message, a, x, g, y)
            print('Encrypted message is: ' + str(output))
    elif (decide == '2'):
        message = input("Type a cypher using space:")
        if message == '':
            print('Cant decrypt empty stroke')
        else:
            print('Decrypted message is: ' + str(decrypt(prepare(message), a, x)))
    elif (decide == '3'):
        message = input("Type a message:")
        if message == '':
            print('Cant decrypt/encrypt empty stroke')
        else:
            output = encrypt(message, a, x, g, y)
            print('Encrypted message is: ' + str(output))
            print('Decrypted message is: ' + str(decrypt(output, a, x)))

if __name__ == ('__main__'):
    main()