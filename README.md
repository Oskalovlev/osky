# Osky

![Osky Workflow](https://github.com/Oskalovlev/osky/actions/workflows/develop-push_workflow.yml/badge.svg)

## Описание
База проекта универсальна и подходит для разных сфер услуг. Цель - постоянный рефакторинг в процессе роста навыков.

### Дополнение
Личный демонстрационный проект для отработки навыков и внедрения новых технологий, если они уместны.


## Стек технологий
![Python](https://img.shields.io/badge/python-3670A0?style=for-the-badge&logo=python&logoColor=ffdd54)
![FastAPI](https://img.shields.io/badge/fastapi-109989?style=for-the-badge&logo=FASTAPI&logoColor=white)
![Postgres](https://img.shields.io/badge/postgres-%23316192.svg?style=for-the-badge&logo=postgresql&logoColor=white)
![Docker](https://img.shields.io/badge/Docker-2CA5E0?style=for-the-badge&logo=docker&logoColor=white)
![Grafana](https://img.shields.io/badge/Grafana-F2F4F9?style=for-the-badge&logo=grafana&logoColor=orange&labelColor=F2F4F9)
![Prometheus](https://img.shields.io/badge/Prometheus-000000?style=for-the-badge&logo=prometheus&labelColor=000000)

<details><summary><h2>Структура проекта</h2></summary>
    <details><summary><h4>Структура базы данных</h4></summary>
        <img src="/docs/db_.jpg"/>
    </details>
    <details><summary><h4>Структура репозитория</h4></summary>
        <img src="/docs/rep_.jpg"/>
    </details>
    <details><summary><h4>Специфика ендпойнтов в OpenAPI</h4></summary>
        <img src="/docs/openapi_.jpg"/>
    </details>
    <details><summary><h4>Документация Redoc</h4></summary>
        <img src="/docs/doc_.jpg"/>
    </details>
</details>

---

<details><summary><h2>Адрес проекта</h2></summary>

*(запускается локально)*

    http://127.0.0.1:8000/

*(запуск на сервере)*

    https://:8000/

> /admin/ # Адрес админки проекта

> /docs/ # Документация

**Handlers**

```sh
api/
```
</details>

---

<details><summary><h2>Подготовка проекта к запуску</h2></summary>

#### `3` пункт для локального запуска. `4` пункт для ведения разработки

1. *Склонируйте репозиторий и перейдите в него*:

    ```sh
    git clone https://github.com/Oskalovlev/osky.git
    ```
    ```sh
    cd osky/
    ```
---
2. *Для работы с PostgreSQL*:

    * Создайте в директории `infra/` файл `.env` командой:

        ```sh
        touch infra/.env
        ```
        > Заполните переменные по примеру файла `.env.example`
---
3. *Создайте и активируйте виртуальное окружение Poetry*:

    <details><summary><h4>Установка Poetry(Если не установлено)</h4></summary>

   Для Linux, macOS, Windows (WSL):
   ```bash
   curl -sSL https://install.python-poetry.org | python3 -
   ```
   Для Windows (Powershell):
   ```bash
   (Invoke-WebRequest -Uri https://install.python-poetry.org -UseBasicParsing).Content | py -
   ```

   * В macOS и Windows сценарий установки предложит добавить папку с исполняемым файлом Poetry в переменную PATH. Сделайте это, выполнив следующую команду (не забудьте поменять {USERNAME} на имя вашего пользователя):

        - macOS:
            ```bash
            export PATH="/Users/{USERNAME}/.local/bin:$PATH"
            ```
        - Windows:
            ```bash
            $Env:Path += ";C:\Users\{USERNAME}\AppData\Roaming\Python\Scripts"; setx PATH "$Env:Path"
            ```
        > Проверить установку:
            ```bash
            poetry --version
            ```
        * Установка автодополнений bash (опционально):
            ```bash
            poetry completions bash >> ~/.bash_completion
            ```
    </details>

    <details><summary><h4>Запуск виртуального окружения</h4></summary>

    - Создать файл .toml:
     ```bash
          poetry init
     ```
   > Соглашаясь на все стандартные значения, если нет другого варианта

    - Создание виртуального окружения:
      ```bash
          poetry env use python
      ```
    - Установка зависимостей:
      ```bash
          poetry install --with dev,test
      ```
    - Запуск оболочки и активация виртуального окружения (из папки проекта):
      ```bash
          poetry shell
      ```
    - Проверка активации виртуального окружения:
      ```bash
          poetry env list
      ```
    </details>

    <details><summary><h4>Потенциальные проблемы</h4></summary>

   *a. виртуальное окружение Poetry недоступно при выборе интерпретатора*

   С высокой вероятностью виртуальное окружение создалось вне папки проекта. Командой ниже можно удостовериться, что окружение будет создано внутри пути проекта:
   ```bash
   poetry config virtualenvs.in-project true
   ```
   Если проект уже был создан, придется пересоздать окружение:
   ```bash
   poetry env list  # вывести имя текущего окружения
   poetry env remove <current environment>  # удалить текущее окружение
   poetry install  # создаст новое окружение с уже с учетом нового конфига virtualenvs.in-project true
   ```

   *b. путь к Poetry не прописан / приходится указывать заново при переоткрытии проекта в редакторе*

   В зависимости от типа используемой оболочки, найдите и откройте bashrc / zshrc файл:
   ```bash
   nano ~/.zshrc
   ```
   Если в файле нет этой строки, добавьте ее и сохраните изменения (не забудьте указать свой {USERNAME}):
   ```bash
   export PATH="/Users/{USERNAME}/.local/bin:$PATH"
   ```
    </details>

---

4. *Настройте pre-commit*:
   `pre-commit` установится автоматически, после ввода команды зависимостей, можно проверить:
   ```bash
     pre-commit --version
   ```

    Для работы нужно ввести команду:
   ```bash
     pre-commit install
   ```

    Теперь `pre-commit` рабатывает автоматически при коммитах.
    > Исправленные `black'ом` файлы нужно добавить:
      ```bash
        git add .
      ```
</details>

---

<details><summary><h2>Для запуска в Docker-контейнере используйте инструкцию</h2></summary>

1. *Запустите сборку контейнеров*:

    ```sh
    docker compose -f infra/docker-compose.yaml up -d --build
    ```
2. *Для остановки контейнеров*:
    ```sh
    docker compose -f infra/docker-compose.yaml stop
    ```
3. *Для удаления контейнеров*:
    ```sh
    docker compose -f infra/docker-compose.yaml down (-v опционально, удалит связи)
    ```
</details>

---

<details><summary><h2>Для локального запуска используйте инструкцию</h2></summary>

1. *Выполните миграции*:

    * Инициализируйте миграции Alembic (опционально)
        ```sh
            alembic init
        ```

    * Создайте миграции (будут созданы с сортировкой по дате, но лучше добавить комментарий)
        ```sh
            alembic revision --autogenerate
        ```

    * Примените миграции
        ```sh
            alembic upgrade head
        ```

2. *Локальный запуск*:

    ```sh
        poetry run task app (в активном Poetry окружением)
    ```
</details>

---


### Автор

- Оскалов Лев (*Telegram*: [@oskalov](https://t.me/oskalov), **Github**: [Oskalovlev](https://github.com/Oskalovlev))
