def show_menu():
    print('Выберите действие: 1 - Показать всех сотрудников \n 2 - Добавить сотрудника \n 3 - Удалить сотрудника\n 4 - Выход')
    select = int(input())
    return select

def add_menu():
    print('Введите имя, Фамиию, номер телефона через пробел: ')
    man = input().split()
    return man

def delete_menu():
    print('Введите номер записи для удаения: ')
    number = int(input())
    return number

def show_result(msg):
    print(msg)

def show_people(people):
    print('№\tИмя\tФамиия\tНомер')
    for i,p in enumerate(people):
        print(i,*p, sep = '\t')