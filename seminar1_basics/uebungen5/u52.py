print("Übung 5.2 - if else")

while True:
    print(); print()
    dividend = int(input("enter the dividend > "))
    divisor = int(input("enter the divisor  > "))

    if divisor == 0:
        print("division by zero not allowed")
        break
    else:
        print(dividend, "/", divisor, "=", dividend / divisor)

    print()

    if divisor == 0: print("division by zero not allowed")
    else: print(dividend, "/", divisor, "=", dividend / divisor)
