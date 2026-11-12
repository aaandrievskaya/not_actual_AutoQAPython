import random
import time

# ################################2.1###################################
# функция с match-case


def get_day_name(day: int) -> str:
    match day:
        case 1:
            return "Понедельник"
        case 2:
            return "Вторник"
        case 3:
            return "Среда"
        case 4:
            return "Четверг"
        case 5:
            return "Пятница"
        case 6:
            return "Суббота"
        case 7:
            return "Воскресенье"
        case _:
            return "Неверный день недели"


# список и цикл
numbers = list(range(1, 10))  # девять чисел: 1…9
max_value = numbers[0]

for n in numbers:
    if n > max_value:
        max_value = n
print(f"Максимум: {max_value}")  # 9
# max(), sorted() и сортировка «чтобы взять последний» здесь не используются

# цикл с break
for n in list(range(1, 8)):
    print(n)
    if n == 5:
        break

# List comprehension
words = [f"str{i}" for i in range(10)]
print(words)  # ['str0', 'str1', ..., 'str9']

long_words = [word for word in words if len(word) > 5]
print(long_words)

# #####################самостоятельная работа############################


def simulate_load():
    STEPS_COUNT = 10
    UP_INT_LIMIT = 100
    LOW_INT_LIMIT = 0
    LOAD_THRESHOLD = 85  # порог нагрузки
    PAUSE_SECONDS = 0.2
    for i in range(STEPS_COUNT):
        load_value = random.randint(LOW_INT_LIMIT, UP_INT_LIMIT)
        if load_value > LOAD_THRESHOLD:
            print(f"Предупреждение: нагрузка {load_value} превышает порог!")
        else:
            print(f"Нагрузка {load_value}, все ОК.")
        time.sleep(PAUSE_SECONDS)


simulate_load()


# ################################2.2###################################
# класс с init и метод
class Car:
    def __init__(self, brand: str, model: str, year: int):
        self.brand = brand
        self.model = model
        self.year = year

    def print_car_info(self) -> None:
        print(f"{self.brand} {self.model} ({self.year})")


car1 = Car("Toyota", "Camry", 2022)
car2 = Car("BMW", "X5", 2023)
car3 = Car("Lada", "Vesta", 2021)

car1.print_car_info()
car2.print_car_info()
car3.print_car_info()


# класс и функция со ссылочным типом
# Изменился исходный объект, так как в функцию на изменение имени
# передается ссылка на исходный объект, к тому же копии мы даже не создавали
class Lead:
    def __init__(self, name: str):
        self.name = name


def change_name(lead: Lead, new_name: str) -> None:
    lead.name = new_name  # меняем атрибут объекта


lead = Lead("Иван")
print(lead.name)  # Иван

change_name(lead, "Пётр")
print(lead.name)  # Пётр  ← изменение видно снаружи функции!


# Класс + list comprehension
class Student:
    def __init__(self, name: str, age: int, grades: list[float]):
        self.name = name
        self.age = age
        self.grades = grades

    def get_avg_grade(self) -> float:
        if not self.grades:
            return 0.0
        return sum(self.grades) / len(self.grades)


students = [
    Student("Анна", 20, [4.5, 5.0, 4.8]),
    Student("Борис", 21, [3.2, 4.0, 3.8]),
    Student("Вера", 19, [4.9, 5.0, 4.7]),
    Student("Андрей", 22, [4.6, 4.0, 4.9]),
]

MIN_AVG = 4.1
good_students = [s for s in students if s.get_avg_grade() > MIN_AVG]

for student in good_students:
    print(f"{student.name}: {student.get_avg_grade():.2f}")
