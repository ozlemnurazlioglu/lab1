divided = {'Tony': 41, 'Rhodey': 43, 'Nat': 35}
we_fall = {'Steve': 39, 'Clint': 35, 'Wanda': 28}

united_we_stand = divided.copy()
united_we_stand.update(we_fall)

print("Name Age")
for name, age in united_we_stand.items():
    print(name,age)


print("*******************")
del united_we_stand['Nat']
print("Name Age")
for name, age in united_we_stand.items():
    print(name,age)


print("*******************")
print("Name Age")
for name, age in sorted(united_we_stand.items()):
    print(name, age)
#LAB4-5d

print("*******************")
max_age = max(united_we_stand.values())
min_age = min(united_we_stand.values())

print("Maximum age:", max_age)
print("Minimum age:", min_age)