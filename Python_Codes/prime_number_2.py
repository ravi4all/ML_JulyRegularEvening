num = int(input("Enter a number : "))

numbers = []

for n in range(num+1, num+50):
    for i in range(2, n):
        if n % i == 0:
            print("Not Prime",n)
            break
    else:
        print("Prime",n)
        break
