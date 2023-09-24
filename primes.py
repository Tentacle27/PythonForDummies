# Calculate prime numbers

for x in range(1, 100):
    # print("testing for prime", x)
    isPrime: bool = True

    for y in range (1, x+1):
        # print(x, "/", y, "=", x / y)
        # print(x, "%", y, "=", x % y)
        if x == 1:
            isPrime: bool = False
        else:
            if x != y:
                if y > 1 :
                    if x % y == 0:
                        isPrime:bool = False

    if isPrime:
        print(x)
