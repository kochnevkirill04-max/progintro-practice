# from textkit.core import normalize_whitespace, count_words

# for i in range(3):
#     text = input(f"Zadejte text №{i + 1}: ")

#     normalized_text = normalize_whitespace(text)
#     word_count = count_words(normalized_text)

#     print(f"Normalizovaný text: {normalized_text}")
#     print(f"Počet slov: {word_count}")

# from textkit.core import word_frequencies, most_common_words

# text = "Pes, kočka a pes!"

# print(word_frequencies(text))
# print(most_common_words(text))
# print(most_common_words(text, 2))

# from textkit import count_words, most_common_words
# text = input("Zadejte text: ")
# print("Počet slov:", count_words(text))
# print("Nejčastější slova:", most_common_words(text, 3))


from pathlib import Path

from textkit import count_words, most_common_words, read_text, write_text


input_path = Path(input("Zadejte cestu k textovému souboru: "))
output_path = Path("report.txt")

try:
    text = read_text(input_path)

    total_words = count_words(text)
    common_words = most_common_words(text)

    report = f"Počet slov: {total_words}\n"
    report += "Nejčastější slova:\n"

    if common_words:
        for word, count in common_words:
            report += f"{word}: {count}\n"
    else:
        report += "Slov není.\n"

    write_text(output_path, report)

    print(report)
    print(f"Report uložen do: {output_path.resolve()}")

except FileNotFoundError as error:
    print(f"Chyba: soubor nebo složka nenalezeny: {error.filename}")

except UnicodeError:
    print("Chyba kódování: potřebujete textový soubor v UTF-8.")

except OSError as error:
    print(f"Chyba při práci se souborem: {error}")