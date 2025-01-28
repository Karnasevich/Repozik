########################################
_int = 5
_float = 3.14
_str = "string"
_bool = True
print(_int, type(_int))
print(_float, type(_float))
print(_str, type(_str))
print(_bool, type(_bool))
print('########################################################')
#########################################
x = 15
y = 4
z = 8

summa = x + y
riznitsa = x - y
umnozh = x * y
dilennya = x / y
stepen = x ** y

okruzh = round(dilennya, 2)
abs_value = abs(-x)

mod = x % y

serednye = (x + y + z) / 3

print("Сума:", summa)
print("Різниця:", riznitsa)
print("Множення:", umnozh)
print("Ділення:", dilennya)
print("Степінь:", stepen)
print("Округлене ділення:", okruzh)
print("Абсолютне значення:", abs_value)
print("Модуль:", mod)
print("Середнє арифметичне:", serednye)
print('########################################################')
#################################################\
name = "Бубнов Олексій Володимирович"
age = 30

formatted_string = f"Мене звати {name}, і мені {age} років. \nЯ орав на весь буфет на Карнасевича, \nбо він присягнув на вірність Сатані, \nа я як праведник маю очистити землю від зла"

print(formatted_string)
print('########################################################')
num = int(input("Введіть число: "))

if num % 2 == 0:
    print("Число парне")
else:
    print("Число непарне")

num2 = int(input("Введіть число для перевірки діапазону: "))

if 10 <= num2 <= 50:
    print("Число в діапазоні від 10 до 50")
else:
    print("Число не входить в діапазон від 10 до 50")
    
print('########################################################')

for i in range(1, 11):
    print(i)

sum_numbers = 0
i = 1
while i <= 100:
    sum_numbers += i
    i += 1

print("Сума чисел від 1 до 100:", sum_numbers)

