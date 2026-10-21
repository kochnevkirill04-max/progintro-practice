count = 0
for i in range(1, 101):
    if i < 2 :
        continue
    for j in range(2, int(i**0.5) + 1):
        if i % j == 0:
            break
    else:
        print(i,end=" ")
        count += 1

        print()
print("\nPočet prvočísel:", count)