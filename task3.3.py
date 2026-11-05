
def mean(values):
    s = 0
    for i in values:
        s = s + i/8
    return s

data = [2, 4, 4, 4, 5, 5, 7, 9]
result = mean(data)

print(result)

def find_median(lst):
    n = len(lst)
    if n == 0:
        return None
    s = sorted(lst)
    mid = n // 2
    if n % 2 != 0:
        return s[mid]
    else:
        return (s[mid - 1] + s[mid]) / 2

data = [2, 4, 4, 4, 5, 5, 7, 9]
print(find_median(data)) 



def std_dev(values):
    if len(values) == 0:
        return None

    avg = mean(values)

    s = 0
    for x in values:
        s += (x - avg) ** 2

    return (s / len(values)) ** 0.5
data = [2, 4, 4, 4, 5, 5, 7, 9]
print (std_dev(data))


def min_max(values):
    


data = [2, 4, 4, 4, 5, 5, 7, 9]
print(min_max(data))
