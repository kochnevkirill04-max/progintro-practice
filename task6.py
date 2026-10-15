total_bytes = 0
text = input("Text: ")
for i in text:
    byte_count = len(i.encode("utf-8"))
    print(i, ' ', f"U+{ord(i):04X}", ' ',' ', byte_count)
    total_bytes += byte_count
print("All characters:",len(text))
print("Total bytes:", total_bytes)
