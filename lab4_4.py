

d = {}
for i in range(1, 31):
    d[i] = (i-1) * i

print(d)


d={}
for i in range(1, 31):
    d[i] = (i-1) * i
    print(i,":",d[i])


d = {}
for i in range(1, 31):
    d[i] = (i-1) * i

sum = 0
for value in d.values():
    sum += value

print("The sum of all values in the dictionary is:", sum)


d={}
for i in range(1, 31):
    d[i] = (i-1) * i
user_input = int(input("Enter a number: "))
if user_input in d:
    print("Key-value is deleting:",d[user_input])
    del d[user_input]
    print("Key-value pair has been deleted.")
else:
    print("The number you entered does not exist in the dictionary.")


