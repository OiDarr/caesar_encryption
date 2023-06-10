def engine(text: str, shift: int) -> str:
    latin_upper = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
    latin_lower = 'abcdefghijklmnopqrstuvwxyz'
    cyrillic_upper = 'АБВГДЕЁЖЗИЙКЛМНОПРСТУФХЦЧШЩЪЫЬЭЮЯ'
    cyrillic_lower = 'абвгдеёжзийклмнопрстуфхцчшщъыьэюя'
    digits = '0123456789'

    result = ''
    for symbol in text:
        alphabet = None
        if symbol in latin_upper:
            alphabet = latin_upper
        elif symbol in latin_lower:
            alphabet = latin_lower
        elif symbol in cyrillic_upper:
            alphabet = cyrillic_upper
        elif symbol in cyrillic_lower:
            alphabet = cyrillic_lower
        elif symbol in digits:
            alphabet = digits

        if alphabet:
            index = alphabet.find(symbol)
            local_shift = shift

            while local_shift >= len(alphabet):
                local_shift -= len(alphabet)
            while local_shift < 0:
                local_shift += len(alphabet)

            if local_shift + index >= len(alphabet):
                result += alphabet[local_shift+index-len(alphabet)]
            elif local_shift + index < 0:
                result += alphabet[len(alphabet)+(local_shift+index)]
            else:
                result += alphabet[local_shift+index]
        else:
            result += symbol

    return result


def encryption_caesar(text: str, shift: int) -> str:
    return engine(text, shift)


def decryption_caesar(text: str, shift: int) -> str:
    return engine(text, shift*-1)
