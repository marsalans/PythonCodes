import math


def rev():
    str1 = "program"
    i = len(str1)
    i -= 1
    str2 = ""
    while i >= 0:
        str2 = str2 + str1[i]
        i -= 1
    print(str2)


def hollowSquare():
    size = int(input("Input size: "))
    for i in range(0, size):
        for j in range(0, size):
            if(i != 0 and i != size - 1):
                if(j != 0 and j != size - 1):
                    print('  ', end=' ')
                else:
                    print('* ', end=' ')
            else:
                print('* ', end=' ')
        print('\n')


def square():
    for j in range(5):
        print('* ' * 5)


def check():
    cYes = 0
    c = input("Enter string 1: ")
    d = input("Enter string 2: ")

    for i in c:
        for j in d:
            if (i == j):
                cYes += 1
            else:
                pass

    if (cYes > 0):
        print("yes")
    else:
        print("no")


def checkPrime():
    val = int(input("Enter a number: "))
    i = 2
    flag = 0
    if (val == 1):
        print("Neither prime nor composite")
    elif (val == 2):
        print("Prime number")
    else:
        while i < val:
            if(val % i == 0):
                flag = 0
                break
            else:
                flag = 1
            i += 1
        if(flag == 1):
            print("Prime number")
        else:
            print("Not a prime number")


def listPrime():
    val = int(input("Enter number till you want to print prime numbers: "))
    for num in range(2, val):
        for i in range(2, num):
            if (num % i == 0):
                break
        else:
            print(num)


def primeFactors(val):
    i = 2
    count = 0
    pFactors = []
    powerVal = []
    while i <= val:
        while val % i == 0:
            pFactors.append(i)
            val = val / i
            count += 1
        if (count > 0):
            powerVal.append(count)
            count = 0
        i += 1

    # print(powerVal)
    return sorted(set(pFactors)), powerVal


def findLCM():
    val1 = int(input("Enter 1st number: "))
    val2 = int(input("Enter 2nd number: "))
    ans = primeFactors(val1)
    ans2 = primeFactors(val2)
    print(ans)
    print(ans2)


findLCM()
