# spell_book_api
API-сервис для менеджмента заклинаний настольно-ролевой игры D&amp;D 5 редакции

## Разворачивание проекта

1. Клонируем репозиторий
```shell
git clone git@github.com:zhdanovaekaterina/spell_book_api.git
```

2. Редактируем конфиги
```shell
cp .config/.env.example .config/.env
nano .config/.env  # конфиг для боевого окружения
cp .config/.env.test.example .config/.env.test
nano .config/.env.test  # конфиг для тестового окружения
```

3. Поднимаем контейнеры
```shell
docker compose up --build -d  # если есть образ, флаг --build не нужен
```

4. Выдаем права директории с миграциями

```shell
sudo chmod -R 777 migrations/versions
```

5. Актуализируем базу
```shell
docker compose run app alembic upgrade head
```

6. Копируем хуки для гита и выдаем права
```shell
cp -r .config/git-hooks/. .git/hooks/
chmod -R 755 .git/hooks/
```

## Тестирование

Для тестирования собран отдельный контейнер test-app, который полностью повторяет рабочее окружение, но не имеет зависимостей. Собирать и запускать его можно отдельно.

Контейнер достаточно собрать один раз, код и тесты для него берутся с хоста
```shell
docker compose build test-app
```

Для запуска тестов достаточно выполнить
```shell
docker compose run --rm test-app
```

Также настроен запуск тестов по коммиту - при падении тестов, коммит не зафиксируется.
