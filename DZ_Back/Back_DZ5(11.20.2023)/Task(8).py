user_sal = input("Введите общую сумму продаж за месяц: ")

salary = 250

try:
    user_sal =  int(user_sal)
except ValueError:
    print("Вы ввели не целое число!")    

salary += user_sal*0.1

print("Ваша полная зарплата: ", salary)