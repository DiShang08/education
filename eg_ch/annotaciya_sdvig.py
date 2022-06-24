def shift_letter(letter: str, shift: int):
    """Функция сдвигает символ letter на shift позиций"""
    return chr(((ord(letter) - 97 + shift) % 26) + 97)


letter = input()
shift = int(input())
print(shift_letter(letter, shift))
