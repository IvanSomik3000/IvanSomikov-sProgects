numbers = []

def added(num):
    numbers.append(int(num))

def find_second():
    add = 0
    for i in range(len(numbers)):
        add = add + numbers[i]
    result = add / len(numbers)
    return result

while True:
    command = input("Введите оценку или f для вывода среднего балла: ")
    if command != 'f':
        try:
            added(command)
            print("Оценки:", numbers)
        except ValueError:
            print("Введите ОЦЕНКУ или f для вывода среднего балла.")
    else:
        if len(numbers) == 0:
            print("Не написано оценок.")
        else:
            print("Средняя: ", find_second())
        break
