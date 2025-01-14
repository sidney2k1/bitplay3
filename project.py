def max1(number):
    count=0
    while(number):
        number=number&(number>>1)
        count+=1
    return count
number=int(input("Enter a number"))
print("The total number of consecutive ones are:",max1(number))
