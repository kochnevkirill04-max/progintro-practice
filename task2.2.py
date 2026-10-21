count = 0

for year in range(1890,2031):
    if year % 4 == 0 and (year % 100 != 0 or year % 400 == 0):
        print(year, end=" ")
        count += 1
        if count % 10 == 0:
            print()

print("\nPočet přestupných let:", count)