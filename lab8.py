#question1
class FileAnalyzer:
    address = ""

    def __init__(self, address):
        self.address = address

    def calculateFreqs(self):
        raise NotImplementedError("Subclasses must implement calculateFreqs method")


class MyFileAnalyzer(FileAnalyzer):
    def __init__(self, address):
        super().__init__(address)

    def calculateFreqs(self):
        with open(self.address, 'r') as file:
            content = file.read()



file_address = "weird_words.txt"
analyzer = MyFileAnalyzer(file_address)
analyzer.calculateFreqs()

#question2
class ListCount(FileAnalyzer):
    def calculateFreqs(self):
        with open(self.address, 'e') as file:
            content = file.read()
            words = content.split()
            freqs = {}
            for word in words:
                freqs[word] = freqs.get(word, 0) + 1
            return freqs


class DictCount(FileAnalyzer):
    def calculateFreqs(self):
        with open(self.address, 'e') as file:
            content = file.read()
            chars = list(content)
            freqs = {}
            for char in chars:
                freqs[char] = freqs.get(char, 0) + 1
            return freqs



file_address = "weird_words.txt"


list_analyzer = ListCount(file_address)
list_freqs = list_analyzer.calculateFreqs()
print("Word Frequencies:")
for word, freq in list_freqs.items():
    print(f"{word}: {freq}")

dict_analyzer = DictCount(file_address)
dict_freqs = dict_analyzer.calculateFreqs()
print("Character Frequencies:")
for char, freq in dict_freqs.items():
    print(f"{char}: {freq}")



    #question3
    class ListCount(FileAnalyzer):
        def calculateFreqs(self):
            with open(self.address, 'e') as file:
                content = file.read()
                letters = list(content)
                freqs = {}
                for letter in letters:
                    if letter.isalpha():
                        freqs[letter] = freqs.get(letter, 0) + 1
                    result = letters + [f"{letter}:{freqs[letter]}" for letter in freqs]
                    print(result)
                    return result




#question4
class DictCount(FileAnalyzer):
    def calculateFreqs(self):
        with open(self.address, 'e') as file:
            content = file.read()
            chars = list(content)
            freqs = {char: 0 for char in chars if char.isalpha()}
            for char in chars:
                if char.isalpha():
                    freqs[char] += 1
            print(freqs)
            return freqs
        file_address = "weird_words.txt"

        list_analyzer = ListCount(file_address)
        list_analyzer.calculateFreqs()

        dict_analyzer = DictCount(file_address)
        dict_analyzer.calculateFreqs()