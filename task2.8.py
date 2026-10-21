import random
a = []
for i in range(1,6):
    a.append(int(random.randrange(100)))

print(a,'   ',len(a))

for j in range(len(a)):
    for i in range(j + 1, len(a)):
        if a[i] < a[j]:
            a[i], a[j] = a[j], a[i]
           
print(a)     