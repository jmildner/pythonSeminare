print("Übung 5.3 - if/elif/else, while")

grade = int(input("enter grade (1-6, end=0) > "))

while grade != 0:
    if grade == 6:
        print("very good")
    elif grade == 5:
        print("good")
    elif grade == 4:
        print("successful")
    elif grade == 3 or grade == 2 or grade == 1:
        print("1, 2, 3 not enough")
    else:
        print("wrong input: ", grade)
    grade = int(input("enter grade (1-6, end=0) > "))
