name = str(raw_input("Please introduce yourself :- "))
char_count = 0
word_count = 1

name_words = name.rsplit(" ")

name_chars = list(name.replace(" ", ""))

print("Number of words in your sentence", len(name_words))
print("Number of characters in your sentence", len(name_chars))

for i in name:
    char_count = char_count + 1
    if (i == " "):
        word_count = word_count + 1


print("Number of words in your sentence", word_count)
print("Number of characters in your sentence (including spaces)", char_count)
