print("Кто из живых существ на первом месте по убийству людей?", "Введите цифру варианта 1 , 2 или 3", sep="\n")
print("Варианты: ","1) собака","2) человек","3) комар", sep="\n")

murd = input("Ваши вариант:")

try:
    murd = int(murd)
except ValueError:
    print("Вы ввели не целое число!")
    exit()
if murd == 1:
    ball1 = 0
    print("Неверный ответ! Собака убивает 10 000 человек в год, занимая 4 место в списке.")
elif murd == 2:
    ball1 = 0
    print("Неверный ответ! Человек убивает 138 000 человек в год, занимая 2 место в списке.")
elif murd == 3:
    ball1 = 2
    print("Верный ответ! Комар убивает 400 000 человек в год, занимая 1 место в списке.")
else:
    print("Вы ввели число либо больше 3 либо меньше 1!")
    exit()

print("Какой цвет глаз самый редкий в мире?", "Введите цифру варианта 1 , 2 или 3", sep="\n")
print("Варианты: ","1) карие","2) зеленые","3) голубые", sep="\n")

eyes = input("Ваши вариант:")

try:
    eyes = int(eyes)
except ValueError:
    print("Вы ввели не целое число!")
    exit()
if eyes == 1:
    ball2 = 0
    print("Неверный ответ! Карие глаза имеют 79% людей.")
elif eyes == 2:
    ball2 = 2
    print("Верный ответ! Голубые глаза имеют 7% людей.")
elif eyes == 3:
    ball2 = 0
    print("Неверный ответ! Голубые глаза имеют 8% людей.")
else:
    print("Вы ввели число либо больше 3 либо меньше 1!")
    exit()

print("Как думаете, сколько цветов у светофоров московского метро?", "Введите цифру варианта 1 , 2 или 3", sep="\n")
print("Варианты: ","1) 3","2) 5","3) 2", sep="\n")

eyes = input("Ваши вариант:")

try:
    eyes = int(eyes)
except ValueError:
    print("Вы ввели не целое число!")
    exit()
if eyes == 1:
    ball3 = 0
    print("Неверный ответ!")
elif eyes == 2:
    ball3 = 2
    print("Верный ответ! Кроме красного, желтого и зеленого светофоры здесь могут гореть синим и лунно-белым.")
elif eyes == 3:
    ball3 = 0
    print("Неверный ответ!")
else:
    print("Вы ввели число либо больше 3 либо меньше 1!")
    exit()

all_ball = ball1 + ball2 + ball3

print("Вы набрали балов:", all_ball)
