from main import *
import pytest


@pytest.mark.parametrize('shift, expected_result',
                         [(6, 'Эочсф хо: 9.70715; Vo tashkx: 9.70715'),
                          (50, 'Зщвья ащ: 3.14159; Ng lskzcp: 3.14159'),
                          (100, 'Шйтмп рй: 3.14159; Le jqixan: 3.14159'),
                          (33, 'Число пи: 6.47482; Wp ubtily: 6.47482')])
def test_caesar_encryptor(shift, expected_result):
    phrase = 'Число пи: 3.14159; Pi number: 3.14159'
    assert encryption_caesar(phrase, shift) == expected_result


@pytest.mark.parametrize('shift, phrase',
                         [(6, 'Эочсф хо: 9.70715; Vo tashkx: 9.70715'),
                          (50, 'Зщвья ащ: 3.14159; Ng lskzcp: 3.14159'),
                          (100, 'Шйтмп рй: 3.14159; Le jqixan: 3.14159'),
                          (33, 'Число пи: 6.47482; Wp ubtily: 6.47482')])
def test_caesar_decryptor(shift, phrase):
    expected_result = 'Число пи: 3.14159; Pi number: 3.14159'
    assert decryption_caesar(phrase, shift) == expected_result


@pytest.mark.parametrize('shift, phrase',
                         [('privet', 20),
                          ([1, 2, 3], 'privet'),
                          (20, (1, 2, 'a')),
                          ('a', 'a')])
def test_encryptor_type_errors(shift, phrase):
    with pytest.raises(TypeError):
        encryption_caesar(phrase, shift)


@pytest.mark.parametrize('shift, phrase',
                         [('privet', 20),
                          ([1, 2, 3], 'privet'),
                          (20, (1, 2, 'a')),
                          ('a', 'a')])
def test_decryptor_type_errors(shift, phrase):
    with pytest.raises(TypeError):
        decryption_caesar(phrase, shift)