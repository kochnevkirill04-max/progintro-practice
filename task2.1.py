diameters = [25.01, 24.97, 25.06, 25.00, 24.94, 25.03, 25.05, 24.95, 25.10, 24.99]
max_limit = 25.05
min_limit = 24.95
bad = 0
for h in diameters:
    if h <= max_limit and h >= min_limit:
        print(h, "ok")
    elif h > max_limit:
        print(h, "velky")
        bad += 1
    elif h < min_limit:
        print(h, "maly")
        bad += 1
total = len(diameters)
percent = bad / total * 100
print("Zmetků:", bad, "z", total, f"({percent:.1f} %)")