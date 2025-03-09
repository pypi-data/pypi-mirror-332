import base64
import codecs
import random


class VCry:
    """
    Библиотека VCry для шифрования и дешифрования текста,
    включающая различные методы шифрования.
    """

    def __init__(self):
        """
        Инициализация библиотеки VCry.
        """
        self.ciphers = {
            "base64": self._base64_encode,
            "base85": self._base85_encode,
            "rot13": self._rot13_encode,
            "reverse": self._reverse_encode,
            "caesar": self._caesar_encode,
            "atbash": self._atbash_encode,
            "hex": self._hex_encode,
            "binary": self._binary_encode,
            "urlencode": self._urlencode_encode,
            "ascii85": self._ascii85_encode,
            "zlib": self._zlib_compress,
            "bzip2": self._bzip2_compress,
        }
        self.deciphers = {
            "base64": self._base64_decode,
            "base85": self._base85_decode,
            "rot13": self._rot13_decode,
            "reverse": self._reverse_decode,
            "caesar": self._caesar_decode,
            "atbash": self._atbash_decode,
            "hex": self._hex_decode,
            "binary": self._binary_decode,
            "urlencode": self._urlencode_decode,
            "ascii85": self._ascii85_decode,
            "zlib": self._zlib_decompress,
            "bzip2": self._bzip2_decompress,
        }

    def crypt(self, text: str, method: str, key: int = None) -> str:
        """
        Шифрует текст заданным методом.

        Args:
            text: Текст для шифрования.
            method: Метод шифрования (base64, base85, rot13, reverse, caesar, atbash, hex, binary, urlencode, ascii85, zlib, bzip2).
            key: Ключ для шифрования (например, для шифра Цезаря).

        Returns:
            Зашифрованный текст.

        Raises:
            ValueError: Если указан неверный метод шифрования.
        """
        method = method.lower()
        if method not in self.ciphers:
            raise ValueError(f"Неверный метод шифрования: {method}.  Доступные методы: {', '.join(self.ciphers.keys())}")

        if method == "caesar":
            if key is None:
                raise ValueError("Для шифра Цезаря требуется ключ.")
            return self.ciphers[method](text, key)
        else:
            return self.ciphers[method](text)

    def uncrypt(self, text: str, method: str, key: int = None) -> str:
        """
        Дешифрует текст заданным методом.

        Args:
            text: Текст для дешифрования.
            method: Метод дешифрования (base64, base85, rot13, reverse, caesar, atbash, hex, binary, urlencode, ascii85, zlib, bzip2).
            key: Ключ для дешифрования (например, для шифра Цезаря).

        Returns:
            Дешифрованный текст.

        Raises:
            ValueError: Если указан неверный метод дешифрования.
        """
        method = method.lower()
        if method not in self.deciphers:
            raise ValueError(f"Неверный метод дешифрования: {method}. Доступные методы: {', '.join(self.deciphers.keys())}")

        if method == "caesar":
            if key is None:
                raise ValueError("Для шифра Цезаря требуется ключ.")
            return self.deciphers[method](text, key)
        else:
            return self.deciphers[method](text)

    def cryptall(self, text: str, caesar_key: int = 3, chunk_size: int = 3) -> str:
        """
        Шифрует текст всеми доступными методами по частям (chunks) и объединяет результаты.

        Args:
            text: Текст для шифрования.
            caesar_key: Ключ для шифра Цезаря (по умолчанию 3).
            chunk_size: Размер части текста для каждой итерации шифрования (по умолчанию 3).

        Returns:
            Строка, содержащая зашифрованный текст, полученный путем применения различных методов.
        """
        encrypted_chunks = []
        start = 0
        while start < len(text):
            end = min(start + chunk_size, len(text))  # Определяем конец текущей части
            chunk = text[start:end]  # Извлекаем текущую часть текста

            method = random.choice(list(self.ciphers.keys()))  # Выбираем случайный метод шифрования
            try:
                if method == "caesar":
                    encrypted_chunk = self.crypt(chunk, method, key=caesar_key)
                else:
                    encrypted_chunk = self.crypt(chunk, method)
                encrypted_chunks.append(f"{method}:{encrypted_chunk}") # Сохраняем метод вместе с зашифрованным текстом
            except Exception as e:
                encrypted_chunks.append(f"Ошибка {method}:{e}")  # Записываем ошибку, если шифрование не удалось

            start = end  # Переходим к следующей части текста

        return " ".join(encrypted_chunks)  # Объединяем все зашифрованные части в одну строку, разделяя пробелами

    def uncryptall(self, encrypted_text: str, caesar_key: int = 3) -> str:
        """
        Дешифрует текст, зашифрованный методом cryptall.

        Args:
            encrypted_text: Зашифрованный текст, полученный с помощью cryptall.
            caesar_key: Ключ для шифра Цезаря (по умолчанию 3).

        Returns:
            Дешифрованный текст.
        """
        decrypted_chunks = []
        chunks = encrypted_text.split()  # Разделяем текст на части

        for chunk in chunks:
            try:
                parts = chunk.split(":", 1)
                if len(parts) == 2:  # Проверяем, что есть и метод, и зашифрованный текст
                    method, encrypted_chunk = parts
                    method = method.strip()  # Remove leading/trailing spaces
                    encrypted_chunk = encrypted_chunk.strip()  # Remove leading/trailing spaces

                    if method == "caesar":
                        decrypted_chunk = self.uncrypt(encrypted_chunk, method, key=caesar_key)
                    else:
                        decrypted_chunk = self.uncrypt(encrypted_chunk, method)
                    decrypted_chunks.append(decrypted_chunk)
                else:
                    decrypted_chunks.append("") # Skip parts without ':'

            except Exception as e:
                decrypted_chunks.append("")  # Skip parts with errors

        return "".join(decrypted_chunks)  # Соединяем все дешифрованные части в одну строку


    def _base64_encode(self, text: str) -> str:
        """Шифрование Base64."""
        return base64.b64encode(text.encode('utf-8')).decode('utf-8')

    def _base64_decode(self, text: str) -> str:
        """Дешифрование Base64."""
        try:
            return base64.b64decode(text.encode('utf-8')).decode('utf-8')
        except base64.binascii.Error:
            return "" # or raise the exception if you prefer

    def _base85_encode(self, text: str) -> str:
        """Шифрование Base85."""
        return base64.b85encode(text.encode('utf-8')).decode('utf-8')

    def _base85_decode(self, text: str) -> str:
        """Дешифрование Base85."""
        try:
            return base64.b85decode(text.encode('utf-8')).decode('utf-8')
        except base64.binascii.Error:
            return ""

    def _rot13_encode(self, text: str) -> str:
        """Шифрование ROT13."""
        return codecs.encode(text, 'rot_13')

    def _rot13_decode(self, text: str) -> str:
        """Дешифрование ROT13."""
        return codecs.encode(text, 'rot_13')

    def _reverse_encode(self, text: str) -> str:
        """Шифрование переворотом строки."""
        return text[::-1]

    def _reverse_decode(self, text: str) -> str:
        """Дешифрование переворотом строки."""
        return text[::-1]

    def _caesar_encode(self, text: str, key: int) -> str:
        """Шифрование Цезаря."""
        result = ''
        for char in text:
            if char.isalpha():
                start = ord('a') if char.islower() else ord('A')
                shifted_char = chr((ord(char) - start + key) % 26 + start)
            elif char.isdigit():
                shifted_char = str((int(char) + key) % 10)
            else:
                shifted_char = char
            result += shifted_char
        return result

    def _caesar_decode(self, text: str, key: int) -> str:
        """Дешифрование Цезаря."""
        return self._caesar_encode(text, -key)  # Дешифрование - это просто шифрование с отрицательным ключом

    def _atbash_encode(self, text: str) -> str:
        """Шифрование Атбаш."""
        result = ''
        for char in text:
            if char.isalpha():
                if char.islower():
                    result += chr(ord('a') + ord('z') - ord(char))
                else:
                    result += chr(ord('A') + ord('Z') - ord(char))
            else:
                result += char
        return result

    def _atbash_decode(self, text: str) -> str:
        """Дешифрование Атбаш."""
        return self._atbash_encode(text)  # Атбаш - самообратный шифр


    def _hex_encode(self, text: str) -> str:
        """Шифрование в Hex."""
        return text.encode('utf-8').hex()

    def _hex_decode(self, text: str) -> str:
        """Дешифрование из Hex."""
        try:
            return bytes.fromhex(text).decode('utf-8')
        except ValueError:
            return ""

    def _binary_encode(self, text: str) -> str:
        """Шифрование в Binary."""
        return ''.join(format(ord(i), '08b') for i in text)

    def _binary_decode(self, text: str) -> str:
        """Дешифрование из Binary."""
        try:
            binary_values = [text[i:i+8] for i in range(0, len(text), 8)]
            return ''.join(chr(int(binary, 2)) for binary in binary_values)
        except ValueError:
            return ""

    def _urlencode_encode(self, text: str) -> str:
        """URL-кодирование."""
        import urllib.parse
        return urllib.parse.quote(text)

    def _urlencode_decode(self, text: str) -> str:
        """URL-декодирование."""
        import urllib.parse
        return urllib.parse.unquote(text)

    def _ascii85_encode(self, text: str) -> str:
        """ASCII85-кодирование."""
        return base64.a85encode(text.encode('utf-8')).decode('utf-8')

    def _ascii85_decode(self, text: str) -> str:
        """ASCII85-декодирование."""
        try:
            return base64.a85decode(text.encode('utf-8')).decode('utf-8')
        except base64.binascii.Error:
            return ""

    def _zlib_compress(self, text: str) -> str:
        """Сжатие Zlib."""
        import zlib
        return base64.b64encode(zlib.compress(text.encode('utf-8'))).decode('utf-8')

    def _zlib_decompress(self, text: str) -> str:
        """Разжатие Zlib."""
        import zlib
        try:
            return zlib.decompress(base64.b64decode(text.encode('utf-8'))).decode('utf-8')
        except zlib.error:
            return ""
        except base64.binascii.Error:
            return ""

    def _bzip2_compress(self, text: str) -> str:
        """Сжатие Bzip2."""
        import bz2
        return base64.b64encode(bz2.compress(text.encode('utf-8'))).decode('utf-8')

    def _bzip2_decompress(self, text: str) -> str:
        """Разжатие Bzip2."""
        import bz2
        try:
            return bz2.decompress(base64.b64decode(text.encode('utf-8'))).decode('utf-8')
        except OSError: # bz2.error наследник OSError
            return ""
        except base64.binascii.Error:
            return ""


# Пример использования
if __name__ == '__main__':
    vcry = VCry()

    text = "DESKTOP-0USOIBT.Xdsat"

    # Шифрование всеми методами
    encrypted_text = vcry.cryptall(text, chunk_size=4) # Задаем размер частей 4
    print(f"Зашифровано: {encrypted_text}")

    # Дешифрование
    decrypted_text = vcry.uncryptall(encrypted_text)
    print(f"Дешифровано: {decrypted_text}")