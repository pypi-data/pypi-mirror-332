# vcry.py
class VCry:
    def __init__(self):
        self.cipher_methods = {
            "caesar": self._caesar_cipher,
            "reverse": self._reverse_cipher,
            "atbash": self._atbash_cipher,
            "keyword": self._keyword_cipher,
            "vigenere": self._vigenere_cipher,
            "rail_fence": self._rail_fence_cipher,
            "rot13": self._rot13_cipher,
            "substitution": self._substitution_cipher, #добавили метод шифрования заменой
            # Можно добавить больше методов...
        }

    def crypt(self, text, method, key=None):
        """
        Шифрует текст, используя указанный метод.

        Args:
            text: Текст для шифрования.
            method: Название метода шифрования (ключ из self.cipher_methods).
            key: Ключ, если метод требует его.

        Returns:
            Зашифрованный текст, или None, если метод не найден.
        """
        method = method.lower()  # Приводим к нижнему регистру для регистронезависимости
        if method in self.cipher_methods:
            return self.cipher_methods[method](text, key, encrypt=True)
        else:
            print(f"Ошибка: Метод шифрования '{method}' не найден.")
            return None

    def uncrypt(self, text, method, key=None):
        """
        Дешифрует текст, используя указанный метод.

        Args:
            text: Текст для дешифрования.
            method: Название метода дешифрования (ключ из self.cipher_methods).
            key: Ключ, если метод требует его.

        Returns:
            Дешифрованный текст, или None, если метод не найден.
        """
        method = method.lower()
        if method in self.cipher_methods:
            return self.cipher_methods[method](text, key, encrypt=False)
        else:
            print(f"Ошибка: Метод шифрования '{method}' не найден.")
            return None

    # --- Методы шифрования (внутренние) ---

    def _caesar_cipher(self, text, key=3, encrypt=True):
        """Шифр Цезаря."""
        try:
            key = int(key)
        except (ValueError, TypeError):
            print("Ошибка: Ключ для шифра Цезаря должен быть целым числом.")
            return None

        result = ""
        for char in text:
            if char.isalpha():
                start = ord('a') if char.islower() else ord('A')
                shift = key if encrypt else -key
                shifted_char = chr((ord(char) - start + shift) % 26 + start)
            else:
                shifted_char = char
            result += shifted_char
        return result

    def _reverse_cipher(self, text, key=None, encrypt=True): # Параметр key не используется, но оставлен для совместимости
        """Шифр обратной записи."""
        return text[::-1]

    def _atbash_cipher(self, text, key=None, encrypt=True): # key не используется, совместимость
        """Шифр Атбаш."""
        result = ""
        for char in text:
            if char.isalpha():
                if char.islower():
                    result += chr(ord('z') - (ord(char) - ord('a')))
                else:
                    result += chr(ord('Z') - (ord(char) - ord('A')))
            else:
                result += char
        return result

    def _keyword_cipher(self, text, key, encrypt=True):
        """Шифр ключевого слова."""
        if not key:
            print("Ошибка: Для шифра ключевым словом необходимо ключевое слово.")
            return None

        key = key.lower()
        alphabet = "abcdefghijklmnopqrstuvwxyz"
        key_alphabet = ""
        for char in key + alphabet:
            if char.isalpha() and char not in key_alphabet:
                key_alphabet += char

        result = ""
        for char in text:
            if char.isalpha():
                is_upper = char.isupper()
                char = char.lower()
                if encrypt:
                    index = alphabet.find(char)
                    if index != -1:
                        new_char = key_alphabet[index]
                    else:
                        new_char = char  # Если символ не в алфавите (например, цифра)
                else:
                    index = key_alphabet.find(char)
                    if index != -1:
                        new_char = alphabet[index]
                    else:
                        new_char = char
                result += new_char.upper() if is_upper else new_char
            else:
                result += char
        return result

    def _vigenere_cipher(self, text, key, encrypt=True):
        """Шифр Виженера."""
        if not key:
            print("Ошибка: Для шифра Виженера необходим ключ.")
            return None

        key = key.lower()
        result = ""
        key_index = 0
        for char in text:
            if char.isalpha():
                start = ord('a') if char.islower() else ord('A')
                key_char = key[key_index % len(key)]
                key_shift = ord(key_char) - ord('a')
                shift = key_shift if encrypt else -key_shift
                shifted_char = chr((ord(char) - start + shift) % 26 + start)
                key_index += 1
            else:
                shifted_char = char
            result += shifted_char
        return result

    def _rail_fence_cipher(self, text, key=3, encrypt=True):
        """Шифр "железнодорожной изгороди"."""
        try:
            key = int(key)
            if key <= 1:
                print("Ошибка: Ключ для шифра 'железнодорожной изгороди' должен быть больше 1.")
                return None
        except (ValueError, TypeError):
            print("Ошибка: Ключ для шифра 'железнодорожной изгороди' должен быть целым числом.")
            return None

        if encrypt:
            rails = [""] * key
            rail_index = 0
            direction = 1  # 1 - вниз, -1 - вверх

            for char in text:
                rails[rail_index] += char
                rail_index += direction

                if rail_index == key:
                    rail_index = key - 2
                    direction = -1
                elif rail_index == -1:
                    rail_index = 1
                    direction = 1

            return "".join(rails)
        else:  # Дешифрование
            rails = [""] * key
            rail_index = 0
            direction = 1
            rail_lengths = [0] * key

            for _ in text:
                rail_lengths[rail_index] += 1
                rail_index += direction
                if rail_index == key:
                    rail_index = key - 2
                    direction = -1
                elif rail_index == -1:
                    rail_index = 1
                    direction = 1

            index = 0
            for i in range(key):
                rails[i] = text[index: index + rail_lengths[i]]
                index += rail_lengths[i]

            result = ""
            rail_index = 0
            direction = 1
            rail_positions = [0] * key

            for _ in range(len(text)):
                result += rails[rail_index][rail_positions[rail_index]]
                rail_positions[rail_index] += 1
                rail_index += direction

                if rail_index == key:
                    rail_index = key - 2
                    direction = -1
                elif rail_index == -1:
                    rail_index = 1
                    direction = 1

            return result
    def _rot13_cipher(self, text, key=None, encrypt=True):
        """Шифр ROT13."""
        return self._caesar_cipher(text, key=13, encrypt=encrypt)

    def _substitution_cipher(self, text, key, encrypt=True):
        """Шифр простой замены."""
        if not key:
            print("Ошибка: Для шифра простой замены необходим ключ (алфавит замены).")
            return None

        alphabet = "abcdefghijklmnopqrstuvwxyz"
        if len(key) != len(alphabet):
            print("Ошибка: Длина ключа должна совпадать с длиной алфавита (26).")
            return None

        key = key.lower()
        result = ""
        for char in text:
            if char.isalpha():
                is_upper = char.isupper()
                char = char.lower()
                if encrypt:
                    index = alphabet.find(char)
                    if index != -1:
                        new_char = key[index]
                    else:
                        new_char = char  # Если символ не в алфавите (например, цифра)
                else:
                    index = alphabet.find(char) #индексы для алфавита который передал пользователь
                    if index != -1:
                        new_char = key[index]
                    else:
                        new_char = char
                result += new_char.upper() if is_upper else new_char
            else:
                result += char
        return result