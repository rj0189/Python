def checkPrime(num):
    for i in range(2,num):
        if(num%i==0):
            print('It is Not Prime Number')
            break
    else:
        print('It is a Prime Number')

def calTriangle(length,bridth):
    area=0.5*length*bridth
    print('Area Of Triangle:',area)
    peri=2*(length+bridth)
    print('Perimeter Of Triangle:',peri)

def sumOfDigit(number):
    sum=0
    while number!=0:
        digit=number%10
        number=number//10
        sum+=digit
    print('Sum of digit:',sum)


num=int(input('Enter Number for check Prime Number:'))
checkPrime(num)

len=int(input('Enter Lenghth of Triangle:'))
bridth=int(input('Enter Width of Triangle:'))
calTriangle(len,bridth)

number=int(input('Enter Number for sum of digit:'))
sumOfDigit(number)
