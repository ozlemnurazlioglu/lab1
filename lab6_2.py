#question2
def calculate_sum(n):

    global total_sum
    if n == 0:
        return
    else:
        sum = 0
        for k in range(1, n + 1):
            sum += ((-1) ** (k + 1)) / k
        total_sum += sum

        calculate_sum(n - 1)
total_sum = 0
calculate_sum(1)

print("Total Sum:",total_sum)


