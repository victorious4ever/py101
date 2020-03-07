x = 979
i = 1
while i < x:
    i = i + 1
    z = x % i
    if z == 0:
        print("%s is composite" % x)
        print(i)
        break
    if i == x - 1:
        print("%s is prime" %x)
        break
