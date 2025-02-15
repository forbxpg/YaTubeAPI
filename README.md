# 🛠️ _`RESTful API` к социальной сети Yatube_

![Django REST Framework](https://img.shields.io/badge/Django%20REST%20Framework-3.15.2-green) ![Python](https://img.shields.io/badge/Python-3.12-blue) ![Django](https://img.shields.io/badge/Django-5.1.6-darkgreen)

## 🚀 Описание проекта

`REST API` для проекта Yatube на Django Rest Framework (DRF), позволяющий пользователям публиковать посты, комментировать их и подписываться на других пользователей.

### 🔑 Реализованные технологии

- 📄 Возможности CRUD операций над `API`
- 💬 Комментирование и просматривание постов
- ✅ Система подписок на других пользователей
- 👀 Просмотр групп с постами
- 🔐 Аутентификация с помощью JWT

## ⚙️ Установка

1. **Клонируйте репозиторий:**

   ```bash
   git clone (https://github.com/forbxpg/api_final_yatube.git)
   ```

2. **Создайте виртуальное окружение и активируйте его:**

   ```bash
   python -m venv env
   source env/bin/activate  # для Linux/Mac
   .\env\Scripts\activate  # для Windows
   ```

3. **Установите зависимости:**

   ```bash
   cd api_final_yatube
   pip install -r requirements.txt
   ```

4. **Выполните миграции:**

   ```bash
   cd yatube_api
   python manage.py makemigrations
   python manage.py migrate
   ```

5. **Создайте суперпользователя:**

   ```bash
   python manage.py createsuperuser
   ```

6. **Запустите сервер разработки:**
   ```bash
   python manage.py runserver
   ```

## 📂 Структура проекта

```plaintext
.
├── api
│   └── templates
        └── redoc.html   # Шаблон для документации к API [ReDoc]
│   ├── apps.py          # Конфигурация приложения API
│   ├── serializers.py   # Сериализаторы моделей
│   ├── views.py         # Представления API
│   ├── urls.py          # Маршруты API
│   └── permissions.py   # Модуль для разрешений к проекту
├── posts
│     └── models.py      # Модели, используемые в БД
├── yatube_api
│     └── settings.py    # Файл с настройками проекта
├── static
│     └── redoc.yaml     # Документация к API
└── requirements.txt     # Список использованных зависимостей
```

## 🖇️ API Эндпоинты

### 🔐 Аутентификация

- **POST** `/api/v1/token/` — Получить JWT-токен
- **POST** `/api/v1/token/refresh/` — Обновить JWT-токен

### 🔍 Публикации [Доступ только для аутентифицированных пользователей]

- **GET** `/api/v1/posts/` — Получить список публикаций
- **POST** `/api/v1/posts/` — Создать новый пост
- **GET** `/api/v1/posts/{post_id}/` — Получить пост по ID
- **PATCH** `/api/v1/posts/{post_id}/` — Обновить пост (только автор)
- **DELETE** `/api/v1/posts/{post_id}/` — Удалить пост (только автор)

### 💬 Комментарии [Доступ только для аутентифицированных пользователей]

- **GET** `/api/v1/posts/{post_id}/comments/` — Список комментариев к посту
- **POST** `/api/v1/posts/{post_id}/comments/` — Добавить комментарий
- **PATCH** `/api/v1/posts/{post_id}/comments/{comment_id}/` — Изменить комментарий (только автор)
- **DELETE** `/api/v1/posts/{post_id}/comments/{comment_id}/` — Удалить комментарий (только автор)

### 👥 Подписки

- **GET** `/api/v1/follow/` — Список подписок
- **POST** `/api/v1/follow/` — Подписаться на пользователя

### 🏷️ Группы

- **GET** `/api/v1/groups/` — Список групп
- **GET** `/api/v1/groups/{group_id}/` — Получить информацию о группе

## ⚡️ Примеры запросов

### 1️⃣ Создание поста

```bash
curl -X POST http://localhost:8000/api/v1/posts/ \
-H "Content-Type: application/json" \
-H "Authorization: Bearer <твой_токен>" \
-d '{"text": "Это база!"}'
```

### 2️⃣ Добавление комментария

```bash
curl -X POST http://localhost:8000/api/v1/posts/1/comments/ \
-H "Content-Type: application/json" \
-H "Authorization: Bearer <твой_токен>" \
-d '{"text": "Не, это баян."}'
```

### 3️⃣ Подписка на пользователя

```bash
curl -X POST http://localhost:8000/api/v1/follow/ \
-H "Content-Type: application/json" \
-H "Authorization: Bearer <твой_токен>" \
-d '{"following": "username"}'
```

## 🛠️ Используемые технологии

- **Django Rest Framework** — Создание CRUD-операций для `API`
- **Djoser** — Аутентификация через `JWT`-токены
- **Base64** — Кодирование изображений для `JSON`

## 🛡️ Разрешения

- **OnlyAuthorPermission** — Изменять и удалять контент может только автор

## 📖 Документация

Для просмотра документации перейдите по адресу:

- `http://localhost:8000/redoc/`

## ✨ Автор

**[Тимур:)](https://github.com/forbxpg)**

🌟 Если проект вам понравился, не забудьте поставить ⭐ на GitHub!
