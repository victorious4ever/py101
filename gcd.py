def gcd(a, b):
    while True:
        #print("computing gcd(", a, ", ", b, ")")
        r = a % b
        if r == 0:
            return b
        a = b
        b = r

i = 2
while i < 20:
    print ("gcd(", 78, ", ", i, ") = ", gcd(78, i))
    i = i + 1