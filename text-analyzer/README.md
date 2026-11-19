# Text Analyzer

Knihovna textkit slouží k analýze textu a práci s textovými soubory.

## Příklad použití

```python
from textkit import count_words, most_common_words

text = "Pes, kočka a pes!"

print(count_words(text))
# 4

print(most_common_words(text))
# [('pes', 2), ('a', 1), ('kočka', 1)]
```