a = int(input("enter a number "))
for i in (2,a):
    if(a%i==0):
        print("not prime")
        break


else:
    print("a prime number ")