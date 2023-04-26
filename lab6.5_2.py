def palindromes(list):

    palindromes = []
    for string in list:
        if string == string[::-1]:
            palindromes.append(string)
    return palindromes

a=["cat", "dog", "lion", "bird"]
b=palindromes(a)
print(b)