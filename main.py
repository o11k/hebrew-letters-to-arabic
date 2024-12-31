import sys


LETTERS = {
    'א': 'ا',
    'ב': 'ب',
    'ג': 'غ',  # Dubious
    'ד': 'د',
    'ה': 'ه',
    'ו': 'و',
    'ז': 'ز',
    'ח': 'ح',
    'ט': 'ط',
    'י': 'ي',
    'כ': 'ك',
    'ך': 'خ',
    'ל': 'ل',
    'מ': 'م',
    'ם': 'م',
    'נ': 'ن',
    'ן': 'ن',
    'ס': 'س',
    'ע': 'ع',
    'פ': 'ب',  # Dubious
    'ף': 'ف',
    'צ': 'ص',
    'ץ': 'ص',
    'ק': 'ق',
    'ר': 'ر',
    'ש': 'ش',
    'ת': 'ت',
}


def convert_string(s: str) -> str:
    return "".join(LETTERS.get(letter, letter) for letter in s)


if __name__ == "__main__":
    for line in sys.stdin:
        print(convert_string(line.strip()))
