
while True:
 f = int(input("Zadej číslo: "))
 if f < 0 or f % 2 == 0:
    print("Tohle vůbec nefunguje; napiš něco jiného.")
 else:
   print(f"Super! Cislo {f} je spravne zvolene.")
   for i in range(f):
       print(' ' * (f - i - 1) + '*' * (2 * i + 1))
   
   for i in range(f - 2, -1, -1):
            print(' ' * (f - i - 1) + '*' * (2 * i + 1))

 
