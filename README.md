Использовал [wemake-django-template](https://github.com/wemake-services/wemake-django-template), чуть-чуть переделал под себя и упростил

# Локальная разработка
## Требуется poetry
1. Установить зависимости и создать .env файл на основе .env.template:
```console
$ make install
```
2. Запустить приложение локально:
```console
$ make runserver
```

3. Запустить фейковую миграцию для movies и другие инишиал миграции:
```console
$ make fakemigrate
```
4. Создать суперюзера для админки:
```console
$ make createsuperuser
```

# Разработка в докере (dev версия)
1. Запустить приложение:
```console
$ make up-dev
```
2. Запустить фейковую миграцию для movies и другие инишиал миграции:
```console
$ make dev-fakemigrate
```
3. Создать суперюзера для админки:
```console
$ make dev-createsuperuser
```
4. Посмотреть текущие логи:
```console
$ make dev-logs
```
5. Остановить приложение:
```console
$ make down
```

# Prod версия
1. Запустить приложение:
```console
$ make up-prod
```
2. Запустить фейковую миграцию для movies и другие инишиал миграции:
```console
$ make prod-fakemigrate
```
3. Создать суперюзера для админки:
```console
$ make prod-createsuperuser
```
4. Посмотреть текущие логи:
```console
$ make prod-logs
```
5. Остановить приложение:
```console
$ make down
```

# Техническое задание

В качестве второго задания предлагаем расширить проект «Панель администратора»: запустить приложение через WSGI/ASGI, настроить отдачу статических файлов через Nginx и подготовить инфраструктуру для работы с Docker. Для этого перенесите в репозиторий код, который вы написали в первом спринте, и выполните задания из папки `tasks`.

Задание предполагает выполнение трёх последовательных подзадач:

1. Реализовать API на Django, который возвращает список фильмов.
2. Запустить Django-приложение в Docker.
3. Настроить работу приложения с помощью Nginx + uWSGI.

Для каждого задания есть небольшая теоретическая часть, которая поможет разобраться с необходимыми деталями для решения задач. Подзадачи нужно сдавать все сразу, чтобы сократить количество циклов проверки вашего кода. Так вы сможете получить обратную связь на всю вашу работу сразу.

## Используемые технологии

- Приложение запускается под управлением сервера WSGI/ASGI.
- Для отдачи [статических файлов](https://nginx.org/ru/docs/beginners_guide.html#static) используется **Nginx.**
- Виртуализация осуществляется в **Docker.**

## Основные компоненты системы

1. **Cервер WSGI/ASGI** — сервер с запущенным приложением.
2. **Nginx** — прокси-сервер, который является точкой входа для web-приложения.
3. **PostgreSQL** — реляционное хранилище данных. 

## Схема сервиса

![all](images/all.png)

## Требования к проекту

1. Приложение должно быть запущено через WSGI/ASGI.
2. Все компоненты системы находятся в Docker.
3. Отдача статических файлов осуществляется за счёт Nginx.

## Рекомендации к проекту

1. Для работы с WSGI/ASGI-сервером база данных использует специального юзера.
2. Для взаимодействия между контейнерами используйте docker compose.
