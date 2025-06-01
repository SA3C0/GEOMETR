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
```csharp
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
README.md                  # Этот файл
```

### 📚 Описание компонентов

## Описание компонентов

В библиотеке реализованы следующие классы и функции:

```python
class Circle:
    def __init__(self, radius: float):
        """
        Инициализация круга с радиусом radius.
        """
        pass

    def area(self) -> float:
        """
        Возвращает площадь круга.
        """
        pass

    def draw(self):
        """
        Визуализирует круг с помощью matplotlib.
        """
        pass


class Triangle:
    def __init__(self, a: float, b: float, c: float):
        """
        Инициализация треугольника со сторонами a, b, c.
        """
        pass

    def area(self) -> float:
        """
        Возвращает площадь треугольника по формуле Герона.
        """
        pass

    def is_right(self) -> bool:
        """
        Проверяет, является ли треугольник прямоугольным.
        """
        pass

    def draw(self):
        """
        Визуализирует треугольник с помощью matplotlib.
        """
        pass


def figure_factory(shape: str, *args):
    """
    Фабричная функция для создания фигур по имени.
    Параметры:
    - shape: 'circle' или 'triangle'
    - args: параметры фигуры (радиус для круга, три стороны для треугольника)

    Возвращает объект класса Circle или Triangle.
    """
    pass
```

### 📌 Зависимости

-Python 3.7+
-matplotlib