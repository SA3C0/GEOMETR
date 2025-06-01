# Geometry Library

**Geometry Library** — простая и расширяемая библиотека на Python для работы с геометрическими фигурами: кругами и треугольниками. Она позволяет вычислять площади, визуализировать фигуры и проверять треугольники на прямоугольность.

---

# 📦 Возможности

- Вычисление площади круга.
- Вычисление площади треугольника по трём сторонам.
- Проверка, является ли треугольник прямоугольным.
- Визуализация фигур с помощью `matplotlib`.
- Фабрика `figure_factory` для создания фигуры по строковому имени.
- Модульная архитектура, удобная для расширения новыми фигурами.
- Полноценные юнит-тесты.

---

## 🔧 Установка

```bash
git clone https://github.com/your_username/geometry_lib.git
cd geometry_lib         # Перейти в папку с проектом
python -m venv .venv    # Создать виртуальное окружение
# Активировать виртуальное окружение:
.venv\Scripts\activate    # Windows
# или
source .venv/bin/activate # Linux/macOS

pip install -r requirements.txt  # Установить зависимости
pip install -e .                 # Установить библиотеку в editable режиме
```
(Примечание: Использование -e (editable mode) позволяет вносить изменения в библиотеку без переустановки. Если установить без -e, библиотеку можно удалить из исходников, и она останется доступна в виртуальном окружении.)

## 🚀 Использование

```python
from geometry import Circle, Triangle, figure_factory

# Прямое использование классов
circle = Circle(5)
print("Площадь круга:", circle.area())
circle.draw()

triangle = Triangle(3, 4, 5)
print("Площадь треугольника:", triangle.area())
print("Прямоугольный?", triangle.is_right())
triangle.draw()

# Использование фабрики
shape = figure_factory("circle", 7)
print("Площадь фигуры через фабрику:", shape.area())
```

### 🧪 Тестирование

Запуск всех юнит-тестов:

```bash
python -m unittest discover tests
```

### 🗂 Структура проекта

geometry_lib/
│
├── geometry/                  # Основной код библиотеки
│   ├── __init__.py            # Импорты классов и фабрики
│   ├── base.py                # Абстрактный базовый класс Figure
│   ├── circle.py              # Класс Circle
│   ├── triangle.py            # Класс Triangle
│   ├── factory.py             # Функция figure_factory
│   └── utils.py               # Вспомогательные функции
│
├── tests/                     # Модульные тесты
│   ├── test_circle.py
│   ├── test_triangle.py
│   ├── test_factory.py
│   └── __init__.py
│
├── requirements.txt           # Зависимости (matplotlib)
├── setup.py                   # Установка пакета через pip
└── README.md                  # Этот файл


### 📚 Описание компонентов

Класс Circle(radius: float) содержит методы: 
area() — возвращает площадь круга
draw() — визуализирует круг через matplotlib. 

Класс Triangle(a: float, b: float, c: float) содержит методы: 
area() — вычисляет площадь треугольника по формуле Герона
is_right() — проверяет, является ли треугольник прямоугольным
draw() — визуализирует треугольник.

Функция figure_factory(shape: str, * args) создаёт объект круга по строке "circle", radius или треугольника по строке "triangle", a, b, c.

### 📌 Зависимости

-Python 3.7+
-matplotlib