n = int(input("Please enter a number between 3 and 9 : "))

if n < 3 or n > 9:
    print("Invalid input! Number should be between 3 and 9 ")
else:

    for i in range(1, n + 1):
        print("*" * i)


    for i in range(n - 1, 0, -1):
        print("*" * i)
