Slovo = str(input("Zadejte slovo: "))
length = len(Slovo)

print(f"Pocet znaku: {length}")
print(f"První znak: {Slovo[0]} \n Poslední znak: {Slovo[-1]}")
print(f"Velkými písmeny: {Slovo.upper()}")
print(f"Pozpátku: {Slovo [::-1]}")
print(f"Palindrome: {Slovo == Slovo [::-1]}")