CatBot
======

CatBot - присылает фото кошек

Установка
---------

Создайте виртуалтьное окружение и активируйте его. Затем выполните в нем:
.. code-block:: text
    pip install -r requirements.text

Положите картинки с кошками в папку images. Файлы должны иметь расширение .jpg

Настройка
---------

Создайте файл settings.py и добавьте туда следующие настройки:

.. code-block:: python

API_KEY = "Ваш ключ API, полученный от BotFather"

USER_EMOJI = [":smiley_cat:", ":smiling_imp:", ":panda_face:", ":dog:"]

Запуск
------

В активированном виртуальном окружении выполните:
.. code-block:: text
    python bot.py