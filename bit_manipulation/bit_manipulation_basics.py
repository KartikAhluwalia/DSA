#To get bit in ith position
def getBit(num,i):
    return int((num & (1<<i)) != 0)

#To set a bit at ith position
def setBit(num,i):
    return num | (1<<i)

#Clear bit at ith positon
def clearBit(num,i):
    mask = ~(1<<i)
    return num & mask

N = 70
first = print(getBit(N,1))
second = print(setBit(N,3))
third = print(clearBit(N,2))
