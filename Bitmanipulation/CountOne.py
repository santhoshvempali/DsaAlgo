# Write a function that takes the binary representation of an unsigned integer and returns 
# the number of '1' bits it has (also known as the Hamming weight).

# Input: n = 00000000000000000000000000001011
# Output: 3

def hamminWeight(n):
    print(n)
    res=0
    while n!=0:
        if n & 1==1:
            res += 1
        n=n>>1
    return res

def hammingWeight(n):
    res=0
    while n:
        res+=n%2
        n=n>>1
    return res

print(hamminWeight(0b00000000000000000000000000001011))
