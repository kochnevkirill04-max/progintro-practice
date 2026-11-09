total_lines = 0
non_empty_lines = 0
characters = 0

try:
    with open("poznamky.txt", "r", encoding="utf-8") as f:
        for line in f:
            total_lines += 1

            line = line.rstrip("\n")
            characters += len(line)

            if line.strip() != "":
                non_empty_lines += 1
                print(non_empty_lines, line)

    print("\nall strings:", total_lines)
    print(" non-empty strings:", non_empty_lines)
    print(" characters (excluding newlines):", characters)

except FileNotFoundError:
    print("poznamky.txt не найден.")