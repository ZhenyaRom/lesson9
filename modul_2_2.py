first = int(input('Введите число: '))
second = int(input('Введите еще число: '))
third = int(input('Введите еще число: '))
if first == second == third:
    print(3)
elif first == second or first == third or second == third:
    print(2)
else:
    print(0)
