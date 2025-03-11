# conversations-about-important-api

Неофициальное API "разговоров о важном", на деле простой парсер.

# Быстрый старт

1. Устанавливаем библиотеку:

``` bash
pip install conversations-about-important-api
```

2. Запустите код ниже:

``` python
"""Пример взаимодествия с библиотекой."""  # noqa: RUF002

import datetime as dt

from conversations_about_important_api import CAIParser


def get_next_date() -> str:
    """Получаем ссылку для парсинга."""
    # Получаем текущую дату
    now = dt.datetime.now()  # noqa: DTZ005

    # Меняем дату на следующий понедельник
    now += dt.timedelta(days=7 - now.weekday())

    # Переводим дату в строку и возвращаем её
    return now.strftime("%d-%m-%Y")


if __name__ == "__main__":
    parser = CAIParser()
    data = parser.get_info(get_next_date())
    print(data)
```

> Выдаёт такой ответ:
> 
> ``` json
> {
>     "title": "Массовый спорт в России",
>     "str_date": "10 марта 2025",
>     "image_url": "https://разговорыоважном.рф/img/2025/10-03-2025.jpg",
>     "plakat_url": "https://разговорыоважном.рф/10-03-2025/plakat.jpg",
>     "videos_urls": [
>         "https://разговорыоважном.рф/10-03-2025/1.mp4",
>         "https://разговорыоважном.рф/10-03-2025/2.mp4",
>         "https://разговорыоважном.рф/10-03-2025/3.mp4",
>         "https://разговорыоважном.рф/10-03-2025/4.mp4",
>         "https://разговорыоважном.рф/10-03-2025/5.mp4"
>     ]
> }
> ```

# Подробнее

1. Создаём и активируем виртуальное окружение (venv):

> Использование виртуального окружения (venv) является лучшей практикой.

``` bash
python3 -m venv venv
. venv/bin/activate
```

> ВАЖНО!
> 
> Вторая команда для Windows выглядит так:
> ``` bash
> venv\Scripts\activate.bat
> ```

2. Устанавливаем библиотеку:

``` bash
pip install conversations-about-important-api
```

3. Далее используйте код из "Быстрого старта" 🤗

Made with ❤️ by [iamlostshe](https://github.com/iamlostshe).
