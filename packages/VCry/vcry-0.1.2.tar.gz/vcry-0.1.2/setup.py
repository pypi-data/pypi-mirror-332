# setup.py
from setuptools import setup, find_packages
import os

setup(
    name='VCry',  # Имя вашего пакета (как он будет называться в pip)
    version='0.1.2',  # Номер версии (начните с чего-то вроде 0.1.0)
    description='A simple library for encryption/decryption with multiple ciphers.',
    long_description=open('README.md').read() if os.path.exists('README.md') else '', # Добавляем описание из README.md, если он есть
    long_description_content_type='text/markdown', # Указываем тип описания
    author='ViniLog',  # Ваше имя
    author_email='Xdsateam2@example.com',  # Ваша почта
    url='https://vcom-team.netlify.app/', # Ссылка на репозиторий на GitHub (если есть)
    packages=['VCry'],  # Автоматически находит все пакеты в проекте
    install_requires=[],  # Зависимости от других пакетов (если есть)
    classifiers=[
        'Development Status :: 3 - Alpha',  # Статус разработки (Alpha, Beta, Production/Stable)
        'Intended Audience :: Developers',
        'Topic :: Security :: Cryptography',
        'License :: OSI Approved :: MIT License', # Выберите подходящую лицензию
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.7',
        'Programming Language :: Python :: 3.8',
        'Programming Language :: Python :: 3.9',
        'Programming Language :: Python :: 3.10',
    ],
    python_requires='>=3.6',  # Минимальная версия Python
)