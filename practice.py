class numeric:
    def oddoreven(self):
        num = int(input("Enter number: "))

        if num % 2 == 0:
            print("Even")
        else:
            print("Odd")

    def posorneg(self):
        num = int(input("Enter number: "))

        if num > 0:
            print("Positive")
        elif num < 0:
            print("Negative")
        else:
            print("Zero")

    def factorial(self):
        num = 5
        fact = 1

        for i in range(1, num + 1):
            fact = fact * i

        print(fact)

    def prime(self):
        num = 13

        flag = True

        for i in range(2, num):
            if num % i == 0:
                flag = False
                break

        if flag:
            print("Prime")
        else:
            print("Not Prime")

    def febnoci(self):
        a = 0
        b = 1
        d=int(input("enter range"))

        for i in range(d):
            print(a, end=" ")
            c = a + b
            a = b
            b = c

    def palindrome(self):
        num = int(input("enter minimum three digit number"))
        temp = num
        rev = 0

        while num > 0:
            digit = num % 10
            rev = rev * 10 + digit
            num //= 10

        if temp == rev:
            print("Palindrome")
        else:
            print("Not Palindrome")

    def amstrong(self):
        num = int(input("enter any number"))
        temp = num
        total = 0

        while num > 0:
            digit = num % 10
            total += digit ** 3
            num //= 10

        if temp == total:
            print("Armstrong")
        else:
            print("Not Armstrong")

    def largest(self):
        a = int(input("enter 'a' value "))
        b = int(input("enter 'b' value "))
        c = int(input("enter 'c' value "))

        largest = a

        if b > largest:
            largest = b

        if c > largest:
            largest = c

        print(largest)

obj = numeric()

choice = int(input("1.odd or even \n 2.positive or negative \n 3.foctorial \n 4.prime number \n 5.febinoci"
                   "\n 6.palindrome \n 7.armstrong number \n 8.largest three number"))

if choice ==1:
    obj.oddoreven()
elif choice==2:
    obj.posorneg()
elif choice==3:
    obj.factorial()
elif choice==4:
    obj.prime()
elif choice==5:
    obj.febnoci()
elif choice==6:
    obj.palindrome()
elif choice==7:
    obj.amstrong()
elif choice==8:
    obj.largest()