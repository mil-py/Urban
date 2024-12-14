class Figure:
    sides_count = 0

    def __init__(self, color, sides):
        r, g, b = color
        if self.__is_valid_color(r, g, b):
            self.__color = list(color)
        if self.__is_valid_sides(sides):
            self.__sides = list(sides).copy()
            self.sides_count = len(sides)
        self.filled = False

    def get_color(self):
        return self.__color

    def __is_valid_color(self, r, g, b):
        if (isinstance(r, int) and
                isinstance(g, int) and
                isinstance(b, int) and
                r in range(256) and
                g in range(256) and
                b in range(256)):
            return True
        else:
            return False

    def __is_valid_sides(self, sides):
        if len(sides) != self.sides_count:

            return False
        else:
            for s in sides:
                if not (isinstance(s, int) and s > 0):
                    return False
        return True

    def set_color(self, r, g, b):
        if self.__is_valid_color(r, g, b):
            self.__color[0] = r
            self.__color[1] = g
            self.__color[2] = b

    def get_sides(self):
        return self.__sides

    def set_sides(self, *new_sides):

        if self.__is_valid_sides(new_sides):
            self.__sides = list(new_sides).copy()

    def __len__(self):
        return sum(self.__sides)


class Circle(Figure):
    def __init__(self, color, circ_len):
        self.sides_count = 1
        super().__init__(color, [circ_len])
        self.__radius = self.get_sides()[0] / 3.1416 / 2

    def get_square(self):
        return round((self.__radius * 2) ** 2 / 4, 2)


class Triangle(Figure):
    def __init__(self, color, sides):
        self.sides_count = 3
        super().__init__(color, sides)

    def get_square(self):
        p = self.__len__() / 2
        a, b, c = self.get_sides()

        s = (p * (p - a) * (p - b) * (p - c)) ** 0.5
        return round(s, 2)


class Cube(Figure):
    def __init__(self, color, side_len):
        self.sides_count = 12
        super().__init__(color, [side_len for i in range(12)])

    def get_volume(self):
        return self.get_sides()[0] ** 3


circle1 = Circle((200, 200, 100), 10)  # (Цвет, стороны)
cube1 = Cube((222, 35, 130), 6)

# Проверка на изменение цветов:
circle1.set_color(55, 66, 77)  # Изменится
print(circle1.get_color())
cube1.set_color(300, 70, 15)  # Не изменится
print(cube1.get_color())

# Проверка на изменение сторон:
cube1.set_sides(5, 3, 12, 4, 5)  # Не изменится
print(cube1.get_sides())
circle1.set_sides(15)  # Изменится
print(circle1.get_sides())

# Проверка периметра (круга), это и есть длина:
print(len(circle1))

# Проверка объёма (куба):
print(cube1.get_volume())

tr = Triangle((99,99,99), (3,4,5))
print(tr.get_square())
