def figonachi():
    t = 0
    a = 0
    b = 1
    print (b)
    while t <= 30:
        c = a+b
        a = b
        b = c
        print (c)
        t = t + 1

print (figonachi())