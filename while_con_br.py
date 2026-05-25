# Эта программа запрашивает ввод числа с клавиатуры
# Затем:
# если в числе есть цифры 1 или 5, то программа считает их количество;
# если в числе есть цифра 7, то программа останавливается и выводит текст "В программе есть запрещенная цифра"
# выводится сумма всех цифр и их количество

flag = True
count5 = 0
count1 = 0
sum_num = 0
count = 0
max_num = 0
min_num = 0

while flag == True:

    print("Введите число")
    print()
    print('Если вы хотите прекратить ввод чисел напишите "end"')
    print()

    num = int(input())

    while num != 0:

        last = num % 10

        if last == 5:
            count5 += 1
        if last == 1:
            count1 += 1
        if last == 7:
            print()
            print("В программе есть запрещенная цифра")
            print()
            break
        if 

        sum_num += last
        count += 1

        num //= 10
    else:
        print()
        print(f"Количество цифр - {count}")
        print(f"Сумма цифр - {sum_num}")
        print()
        print(f'Количество цифр "1" - {count1}')
        print(f'Количество цифр "5" - {count5}')
        print()
