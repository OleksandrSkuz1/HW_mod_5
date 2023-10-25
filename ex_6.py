CYRILLIC_SYMBOLS = "абвгдеёжзийклмнопрстуфхцчшщъыьэюяєіїґ"
TRANSLATION = ("a", "b", "v", "g", "d", "e", "e", "j", "z", "i", "j", "k", "l", "m", "n", "o", "p", "r", "s", "t", "u",
               "f", "h", "ts", "ch", "sh", "sch", "", "y", "", "e", "yu", "ya", "je", "i", "ji", "g")

# Створюємо словник для транслітерації за допомогою zip
TRANS = dict(zip(CYRILLIC_SYMBOLS, TRANSLATION))


def translate(text):
    # Переведемо рядок, використовуючи словник TRANS
    translated_text = ''.join([TRANS.get(char.lower(), char) for char in text])
    return translated_text

# Приклад використання
print(translate("Дмитро Короб"))  # Dmitro Korob
print(translate("Олекса Івасюк"))  # Oleksa Ivasyuk