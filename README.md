# Дипломная работа.
## Сайт (https://www.kinopoisk.ru/)

## Шаблон для автоматизации тестирования на python

### Шаги
1. Клонировать проект `git clone https://github.com/dagoryal/QA_Diplom.git`
2. Установить все зависимости `pip install -r requirements.txt`
3. Запустите тесты с помощью Allure с генерацией папки с результатами:
 ''' pytest --alluredir=./results '''
4. Сгенерировать отчет: 
''' allure generate results -o final-report '''
5. Открыть отчёт в браузере:
''' allure open final-report '''

### Стек:
- pytest
- selenium
- requests
- _sqlalchemy_
- allure
- config
- json

### Структура:
- QA_Diplom - Папка с тестами и файлами, относящимися к финальной работе.
- ./test - Содержит тестовые сценарии.
- ./pages - Содержит классы для описания различных страниц.
- requirements.txt - Список зависимостей проекта.
- readme.md - Документация проекта.

### Полезные ссылки
- [Подсказка по markdown](https://www.markdownguide.org/basic-syntax/)
- [Генератор файла .gitignore](https://www.toptal.com/developers/gitignore)
- [Про pip freeze](https://pip.pypa.io/en/stable/cli/pip_freeze/)
