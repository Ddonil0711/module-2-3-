my_list = [42, 69, 322, 13, 0, 99, -5, 9, 8, 7, -6, 5]
a = 0
while True:
    number = int(input('введите число: '))
    if a < len(my_list) and number > 0:
        print(number)
    else:
        break
