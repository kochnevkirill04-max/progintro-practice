for cislo in range(100, 1000):
    sto = cislo // 100
    des = (cislo // 10) % 10
    jed = cislo % 10
    if cislo == sto ** 3 + des ** 3 + jed ** 3:
        print (f"{cislo} = {sto}^3 + {des}^3 + {jed}^3")
        