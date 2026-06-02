# 🚀 QA GURU Homework 16
## Pytest: Parameterization, Skip, Indirect & Fixtures

Автоматизированные UI-тесты для проверки перехода на страницу авторизации GitHub с использованием различных подходов параметризации в Pytest.

---

## 📌 Задание

Реализованы следующие сценарии:

- Поиск кнопки **Sign in** на GitHub
- Переход на страницу авторизации
- Проверка отображения поля ввода логина
- Параметризация размеров окна браузера
- Отдельные сценарии для desktop и mobile версий сайта
- Демонстрация различных подходов работы с параметрами в Pytest

---

## 🛠 Используемый стек

<p align="center">
<img src="https://img.shields.io/badge/Python-3776AB?style=for-the-badge&logo=python&logoColor=white">
<img src="https://img.shields.io/badge/Pytest-0A9EDC?style=for-the-badge&logo=pytest&logoColor=white">
<img src="https://img.shields.io/badge/Selenium-43B02A?style=for-the-badge&logo=selenium&logoColor=white">
<img src="https://img.shields.io/badge/Selene-5A29E4?style=for-the-badge">
<img src="https://img.shields.io/badge/Chrome-4285F4?style=for-the-badge&logo=googlechrome&logoColor=white">
</p>

---

## 📂 Структура проекта

```text
home_16
│
├── tests
│   ├── conftest.py
│   ├── test_github_skip.py
│   ├── test_github_indirect.py
│   └── test_github_fixtures.py
│
├── requirements.txt
├── pytest.ini
└── README.md
```

---

## ▶️ Запуск проекта

Установка зависимостей:

```bash
pip install -r requirements.txt
```

Запуск всех тестов:

```bash
pytest -v
```

---

## ✅ Подход №1 — Skip

Файл:

```text
tests/test_github_skip.py
```

Особенности:

- Один набор параметров для desktop и mobile
- Неподходящие размеры окна пропускаются через `pytest.skip()`

Результат:

```text
3 passed
3 skipped
```

---

## ✅ Подход №2 — Indirect

Файл:

```text
tests/test_github_indirect.py
```

Особенности:

- Используется параметризация через `indirect=True`
- Размер окна передаётся в фикстуру

Результат:

```text
3 passed
```

---

## ✅ Подход №3 — Separate Fixtures

Файл:

```text
tests/test_github_fixtures.py
```

Особенности:

- Отдельная фикстура для desktop
- Отдельная фикстура для mobile
- Максимально читаемая структура тестов

---

## 📖 Сравнение подходов

### Skip

Преимущества:

- Простая реализация
- Хорошо показывает работу параметров

Недостатки:

- Появляются skipped тесты
- Выполняются лишние проверки

---

### Indirect

Преимущества:

- Гибкая настройка параметров
- Хорошая масштабируемость

Недостатки:

- Сложнее для новичков
- Менее очевидная логика передачи параметров

---

### Separate Fixtures

Преимущества:

- Читаемый код
- Простое разделение сценариев

Недостатки:

- Возможное дублирование кода
- Больше фикстур при расширении проекта

---

## 🎯 Проверяемый сценарий

### Desktop

1. Открыть GitHub
2. Найти кнопку Sign in
3. Перейти на страницу авторизации
4. Проверить отображение поля логина

### Mobile

1. Открыть GitHub
2. Открыть мобильное меню
3. Перейти на страницу авторизации
4. Проверить отображение поля логина

---

## 👨‍💻 Автор

Leonid Chaliy

QA GURU — Homework #16