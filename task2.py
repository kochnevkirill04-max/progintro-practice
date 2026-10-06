sekond = int(input("Zadejte pocet sekund: "))
hours = sekond // 3600
remaining = sekond % 3600
minutes = remaining // 60
sekc = remaining % 60
print(f"{hours}:{minutes:02d}:{sekc:02d}")