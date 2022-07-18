def shift_letter(letter: str, shift: int):
    """Функция сдвигает символ letter на shift позиций"""
    return chr(((ord(letter) - 97 + shift) % 26) + 97)


def caesar_cipher(text: str, sdvig: int):
    """Шифр цезаря"""
    new_text = ''
    for i in range(len(text)):
        if text[i].isalpha():
            new_text += shift_letter(text[i], shift=sdvig)
        else:
            new_text += text[i]

    return new_text
