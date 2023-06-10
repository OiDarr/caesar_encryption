# caesar_encryption

## Интерфейс
Включает в себя функции шифратора и дешифратора Цезаря. 

Чтобы зашифровать сообщение, присвойте переменной вызов функции
`encryption_caesar(text: str, shift: int)`, где text - шифруемая
фраза; shift - смещение.

Чтобы расшифровать сообщение, присвойте переменной вызов
функции `decryption_caesar(text: str, shift: int)`, где text - 
зашифрованная фраза; shift - смещение.

## Под капотом
Основная логика работы интерфейса реализована в функции 
`engine(text: str, shift: int)`, именно она распознаёт язык 
символа, выбирает алфавит и осуществляет шифрование. 

Фраза может содержать любые символы, но шифрование применится
только если символ из русского или английского алфавита, или цифра;
знаки препинания, а также незнакомые символы отобразятся в
оригинале.

Число смещения ограничено лишь рамками `int`, то есть может
превосходить мощность алфавитов. Более того выбор высокого числа
смещения сделает шифр надёжнее, ибо в таком случае у 
разных алфавитов будет разное смещение.

Таким образом функция-шифратор `encryption_caesar` просто отдаёт
результат работы `engine`, а дешифратор `decryption_caesar` 
берёт сдвиг `shift` с противоположным знаком и также запускает 
`engine`.

## Тесты
В директории присутствует файл `tests.py`, содержащий в себе
по 4 тестовых кейса на функционал интерфейса, а также
по 4 кейса на `attributeError` для каждой функции.
Кейсы построены таким образом, чтоб целиком покрыть алгоритмы.
