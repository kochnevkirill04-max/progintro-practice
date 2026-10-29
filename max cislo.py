list = []

while True:
    vod = input("Číslo (Enter = konec): ")
    if vod=="":
        break
    if not(vod.isdigit()):
        continue
    cislo = int(vod)
    list.append(cislo)


if len(list) == 0:
    print("Nebylo zadáno žádné číslo.")
else:
    maximalni_cislo = list[0]
    for cislo in list:
        if cislo > maximalni_cislo:
            maximalni_cislo = cislo

    print(f"Počet: {len(list)}")
    print(f"Maximum: {maximalni_cislo}")
