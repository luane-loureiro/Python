A, B, C, D = map(int,imput().split())

if B > C and D > A and (C + D) > (A + B) and C > 0 and D > 0 & A % 2 == 0:
    print("Números aceitos")

else
    print("Números não aceitos")