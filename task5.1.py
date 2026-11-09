
def text_statistics(path):
    l = []
    f = open(path, 'r', encoding='utf-8')
    i = 0
    d = {"lines": 0,"longest_line": 0}
    for line in f:
        k = 0
        s = 0
        i = i + 1
        s = len(line.split())
        k = len(line.replace(" ",""))
        d["lines"] += 1
        print('Line', i, 'has', s, 'words' 'and', k, 'characters' )

        if len(line) > d["longest_line"]:
            d["longest_line"] = len(line)
            longest_line = line

    f.close()


    return i, d["longest_line"]


result = text_statistics('text.txt')

print("longest line:", result[1])
print("Number of lines:", result[0])
