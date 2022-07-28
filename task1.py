while True:
    try:
        day = input ('Введите число, обозначающее день недели: ')
        if 1 <= int(day) <= 7:
            break
        else:
            raise ValueError
    except ValueError:
        print("\nЧисло не соответствует дню недели\n")


if 6 <= int(day) <= 7:
    print (f'{day} - выходной')
else:
    print ('рабочий')