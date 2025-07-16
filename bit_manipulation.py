#To get bit in ith position
def getBit(num,i):
    return ((num & (1<<i)) != 0)

def setBit(num,i):
    return num | (1<<i)