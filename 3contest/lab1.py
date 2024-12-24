"""
Реализовать два класса Pupa и Lupa. И класс Accountant.

Класс Accountant должен уметь одинаково успешно работать и с экземплярами класса Pupa и с экземплярами класса Lupa.
У класса Accountant должен быть метод give_salary(worker). Который, получая на вход экземпляр классов Pupa или Lupa,
вызывает у них метод take_salary(int).
Необходимо придумать как реализовать такое поведение.
Метод take_salary инкрементирует внутренний счётчик у каждого экземпляра класса на переданное ему значение.

При этом Pupa и Lupa два датасайнтиста и должны работать с матрицами.
У них есть метод do_work(filename1, filename2).
Pupa считывают из обоих переданных ему файлов по матрице и поэлементно их суммируют.
Lupa считывают из обоих переданных ему файлов по матрице и поэлементно их вычитают.

Работники обоих типов выводят результат своих трудов на экран.
"""

class Matrix :
    @staticmethod
    def read_matrices (filename):
        """
        Данный метод возвращает прочитанную матрицу из файла filename.
        Также может сообщить об ошибке, неверного формата матрицы
        :param filename: имя файла откуда будет производиться чтение матрицы
        :return: matrix
        """
        with open(filename, 'r') as input:

            matrix = []
            line_number = 0

            for line in input:

                stripped_line = line.strip()
                matrix_line = stripped_line.split()
                countrow = len(matrix_line)

                if line_number != 0 and countrow != len(matrix[0]):
                    raise Exception("Неверный формат матрицы")
                matrix.append(matrix_line)
                line_number +=1
        return matrix

    @staticmethod
    def matrix_add(matrix1, matrix2):
        """
        метод позволяет складывать две матрицы. В слуачае некоректных данных сообщает об ошибке.
        :param matrix1: 1-aя матрица
        :param matrix2: 2-aя матрица
        :return: результирующая матрица
        """

        if len(matrix1) != len(matrix2) or len(matrix1[0]) != len(matrix2[0]):
            raise ValueError("Размеры матриц не совпадают.\n"
                             "Сложение невозможно")

        m = len(matrix1)  # количество строк в matrix1
        p = len(matrix1[0])  # количество столбцов в matrix1
        resmatrix = [[0] * p for _ in range(m)]

        for i in range(len(matrix1)):
            for j in range(len(matrix1[0])):
                resmatrix[i][j] = int(matrix1[i][j]) + int(matrix2[i][j])

        return resmatrix

    @staticmethod
    def matrix_mult(matrix1, matrix2):
        """
        метод позволяет усножать две матрицы. В слуачае некоректных данных сообщает об ошибке.
        :param matrix1: 1-aя матрица
        :param matrix2: 2-aя матрица
        :return: результирующая матрица
        """

        if len(matrix1[0]) != len(matrix2):
            raise ValueError("Количество столбцов 1-й матрицы не совпадает с количеством строк 2-й матрицы.\n"
                             "Умножение невозможно")

        m = len(matrix1)  # количество строк в matrix1
        n = len(matrix2)  # количество столбцов в matrix1 и количество строк в matrix2
        p = len(matrix2[0])  # количество столбцов в matrix2

        mult_matrix = [[0] * p for _ in range(m)]

        for i in range(m):
            for j in range(p):
                for k in range(n):
                    mult_matrix[i][j] += int(matrix1[i][k]) * int(matrix2[k][j])
        return mult_matrix

    @staticmethod
    def write_matrix(matrix):
        """
        Данная функция записывает матрицу в консоль.
        :param path:
        :param matrix:
        """
        for row in matrix:
            outstr = ' '.join(map(str, row))
            print(outstr)
        print()


class GoodWorker (Matrix) :
    """"""
    def __init__(self):
        self.salary = 0

    def take_salary(self, value):
        self.salary += value

    def read_matrices(self, filename1, filename2):
        try:
            self.matrix1 = super().read_matrices(filename1)
        except Exception as Ex:
            print(f"{Ex} 1")
            return

        try:
            self.matrix2 = super().read_matrices(filename2)
        except Exception as Ex:
            print(f"{Ex} 2")
            return


class Pupa (GoodWorker) :

    def do_work(self, filename1, filename2):
        super().read_matrices(filename1, filename2)
        try:
            if (hasattr(self,'matrix1') and hasattr(self,'matrix2') ):
                self.resmatrix = super().matrix_add(self.matrix1, self.matrix2)
        except ValueError as ve:
            print(f"Ошибка:{ve}")
            return

        if hasattr(self, 'resmatrix'):
            super().write_matrix(self.resmatrix)



class Lupa (GoodWorker):

    def do_work(self, filename1, filename2):
        super().read_matrices(filename1, filename2)
        try :
            if (hasattr(self,'matrix1') and hasattr(self,'matrix2') ):
                self.resmatrix = super().matrix_mult(self.matrix1, self.matrix2)
        except ValueError as ve :
            print(f"Ошибка:{ve}")
            return

        if hasattr(self, 'resmatrix'):
            super().write_matrix(self.resmatrix)

class Accountant:
    def give_salary(self, worker, value):
        worker.take_salary(value)

pupa = Pupa()
lupa = Lupa()
accountant = Accountant()

print(f"pupa salary: {pupa.salary}")
print(f"lupa salary: {lupa.salary}")

pupa.do_work("1.txt", "2.txt")
lupa.do_work("1.txt", "2.txt")
accountant.give_salary(pupa, 10+10)
accountant.give_salary(lupa, 10*10)

print(f"pupa salary: {pupa.salary}")
print(f"lupa salary: {lupa.salary}")
