columns = []
rows = []
table_data = {}

def create_column(name):
    if name not in columns:
        columns.append(name)
        print_table()
    else:
        print("Имя уже использовано")

def create_row(name):
    if name not in rows:
        rows.append(name)
        print_table()
    else:
        print("Имя уже использовано")

def edit_cell():
    if not columns or not rows:
        print("Сначала создайте столбцы и строки")
        return
    
    print("Доступные столбцы:", ", ".join(columns))
    col = input("Введите имя столбца: ")
    if col not in columns:
        print("Нет такого столбца")
        return
    
    print("Доступные строки:", ", ".join(rows))
    row = input("Введите имя строки: ")
    if row not in rows:
        print("Нет такой строки")
        return
    
    value = input(f"Введите значение для [{col}][{row}]: ")
    table_data[(col, row)] = value
    print_table()

def print_table():
    if not columns or not rows:
        print("Таблица пуста")
        return
    
    col_width = max(len(str(item)) for item in [*columns, *rows, *table_data.values()] if item) + 2
    if col_width < 5:
        col_width = 5
    
    header = " " * col_width + "|" + "|".join([f"{col:^{col_width}}" for col in columns]) + "|"
    separator = "-" * col_width + "+" + "+".join(["-" * col_width for _ in columns]) + "+"
    
    print(separator)
    print(header)
    print(separator)
    
    for row in rows:
        row_cells = [f"{row:<{col_width}}|"]
        for col in columns:
            cell_value = str(table_data.get((col, row), ""))
            row_cells.append(f"{cell_value:^{col_width}}")
        print("|".join(row_cells) + "|")
        print(separator)

while True:
    print("\nМеню:")
    print("1 - Создать столбец")
    print("2 - Создать строку")
    print("3 - Редактировать ячейку")
    print("4 - Показать таблицу")
    print("0 - Выход")
    
    com = input("Выберите действие: ")
    
    if com == '1':
        create_column(input("Введите имя столбца: "))
    elif com == '2':
        create_row(input("Введите имя строки: "))
    elif com == '3':
        edit_cell()
    elif com == '4':
        print_table()
    elif com == '0':
        break
    else:
        print("Некорректный ввод, попробуйте снова")
