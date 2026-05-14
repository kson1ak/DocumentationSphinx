import os
import sys
# 1. Добавляем путь к вашему коду (чтобы Sphinx увидел weather.py)
sys.path.insert(0, os.path.abspath('../..'))

# -- Настройки проекта --
project = 'Weather API'
copyright = '2026, Sofia'
author = 'Sofia'

# -- Общая конфигурация --
# 2. Добавляем необходимые расширения для Google Style и автодокументации
extensions = [
    'sphinx.ext.autodoc',
    'sphinx.ext.napoleon',  # Читает Google Style docstrings
    'sphinx.ext.viewcode'   # Добавляет ссылки на исходный код в документации
]

templates_path = ['_templates']
exclude_patterns = ['_build', 'Thumbs.db', '.DS_Store']

language = 'ru'

# -- Настройки HTML вывода --
# 3. Меняем 'alabaster' на 'sphinx_rtd_theme'
html_theme = 'sphinx_rtd_theme'

html_static_path = ['_static']