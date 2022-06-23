try:
    a = 5
    b = 8
    c = 3

    largest = 0

    if a > b and a > c:
        largest = a
    if b > a and b > c:
        largest = b
    if c > a and c > b:
        largest = c
    elif a==b==c:
        largest=a

    print(largest, "is the largest of three numbers.")

except:
    print(" please enter the vaild numbers !!..")






