import csv

peop = filename = r'C:\Users\Lera\Desktop\Николай\5. Знакомство с python\Sem8\Sem88\start\people.csv'


def get_people():
    with open(peop, encoding="utf8") as csvfile:
        reader = csv.reader(csvfile, delimiter=';')
        sp = list(reader)
        return sp


def add(man):
    # # запись в файл (для перезаписи режим 'w')
    with open(peop, 'a', encoding="utf8", newline='') as csvfile:
        writer = csv.writer(csvfile, delimiter=';')
        writer.writerow(man)

def delete(number):
    with open(peop, encoding="utf8") as csvfile:
        reader = csv.reader(csvfile, delimiter=';')
        sp = list(reader)
    if number < len(sp):
        del sp[number]
        with open(peop, 'w', encoding="utf8", newline='') as csvfile:
            writer = csv.writer(csvfile, delimiter=';')
            for row in sp:
                writer.writerow(row)