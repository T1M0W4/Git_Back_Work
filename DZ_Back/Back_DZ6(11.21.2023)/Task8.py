print("Тест на устранения проблемы в армии", "В части сломалась какая то хреновина!", sep="\n")
print("Варианты решений:","1) починить","2) свалить на рядового","3) купить новую хреновину","(Введите цифру 1 или 2 или 3, чтобы выбрать вариант)", sep="\n")

sold = input("Ваши действия:")

try:
    if sold == "1":
        ball = 0
        print("Блядь не трогай ничего")