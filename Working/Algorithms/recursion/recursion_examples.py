def countdown(n):
    if n<=0:    # base case (kicker)
        print("Blastoff")
    else:
        print(n)
        countdown(n-1)


def factorial(n):
    if n<=1:
        return 1
    else:
        return n * factorial(n-1)

print(factorial(5))

def printn(mystring, n):
    if n == 0:
        return None
    else:
        printn(mystring, (n-1))
        print(mystring)
printn("yeet", 4)