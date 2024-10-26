
def get_matrix(n, m, value):
    matrix = []
    for i in range(n):
        matrix.append([])
        for j in range(m):
            matrix[i].append(value)
    return matrix


def print_matrix(matr):
    print()
    for i in range(len(matr)):
        print(*matr[i])
    print()


def is_eq(lst):# возвращает элемент если все элементы списка равны и False в противном случае
    eq = lst[0]
    for i in range(1,len(lst)):
        if lst[i] != eq:
            eq = False
            break
    return eq


def is_win(area, fil):# fil - заполнитель
    # Перебор строк
    for i in range(len(area)):

        if is_eq(area[i]) and is_eq(area[i]) != fil:
            return is_eq(area[i])

    # Перебор столбцов
    for j in range(len(area)):
        col = [row[j] for row in area]  # row extraction

        if is_eq(col) and is_eq(col) != fil:
            return is_eq(col)

    # Диагонали

    diag1 = []
    diag2 = []
    for i in range(len(area)):
        for j in range(len(area)):
            if i == j:
                diag1.append(area[i][j])

            if j == len(area)-1 - i:
                diag2.append(area[i][j])
    if is_eq(diag1) and is_eq(diag1) != fil:
        return is_eq(diag1)
    if is_eq(diag2) and is_eq(diag2) != fil:
        return is_eq(diag2)


area = get_matrix(3, 3, '*')
print_matrix(area)

char = 'X'
for i in range(9):
    print(f"Ход {"крестиков" if char == 'X' else "ноликов"}: ")
    r = int(input("строка (1-3): ")) - 1
    c = int(input("столбец (1-3):")) - 1
    if area[r][c] == '*':
        area[r][c] = char
    else:
        print("Ячейка занята! Вы пропускаете ход!")
        i -= 1

    print_matrix(area)
    if is_win(area, '*'):
        print(f"Победили {"крестики " if char == 'X' else "нолики"}")
        break

    char = 'O' if char == 'X' else 'X'
    if i == 8:
        print("победила дружба")