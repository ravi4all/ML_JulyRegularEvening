num = 9551

for i in range(2,num):
    if num % i == 0:
        print("Not prime")
        break
else:
    print("Prime number")


##prime = False
##for i in range(2,num):
##    if num % i == 0:
##        prime = False
##        break
##    else:
##        prime = True
##
##if prime == True:
##    print("Prime Number")
##else:
##    print("Not Prime Number")


##minRange = int(input("Enter min : "))
##maxRange = int(input("Enter max : "))
##
##for num in range(minRange, maxRange+1):
##    for i in range(2, num):
##        if num % i == 0:
##            print("Not Prime", num)
##            break
##    else:
##        print("Prime Number", num)
