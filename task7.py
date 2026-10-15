text = input("Text: ")
letters = {}
print(text)
for i in text:
    if i.isalpha():
        if i in letters:
            letters[i] += 1
        else:
            letters[i] = 1
sorted_letters = sorted(letters.items(), key=lambda x: (-x[1], x[0]))
for letter, count in sorted_letters:
    print(letter, count)  
print("Různých písmen:", len(letters))