


def reverseInteger(n):
    sum=0
    sign=1
    num=n
    if n<0:             #checking sign
        sign=-1         #for using while loop temperorialy changing the sign
        num*=-1
    while num>0:        #calculating th reverse
        rem=num%10
        sum=sum*10+rem
        num=num//10
    if -2147483648<sum<2147483648:                   #Checking range
        return sum* sign
    else:
        return 0