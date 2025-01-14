def divide(divident,divisor):
    sign=(-1 if( (divident<0)^(divisor<0)) else 1)
    divident=abs(divident)
    divisor=abs(divisor)
    quotientnumber=0
    tempnumber=0
    for i in range(31,-1,-1):
        if (tempnumber+(divisor<<i)<=divident):
            tempnumber+=divisor<<i
            quotientnumber|=1<<i
    if sign==-1:
        quotientnumber=-quotientnumber
    return quotientnumber
divident=int(input("Enter a number:"))
divisor=int(input("Enter the number:"))
print("result=",divide(divident,divisor))
