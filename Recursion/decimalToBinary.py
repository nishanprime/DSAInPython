def decToBin(dec):
    if dec==0 or dec==1:
        return str(dec)
    return decToBin(dec//2)+str(dec%2)
    return dec
print(decToBin(100))