import math

def height(N):
    return math.ceil(math.log2(N+1) - 1)

if __name__ =="__main__":
    print(height(6))