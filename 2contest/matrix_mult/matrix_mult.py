import argparse
from mailbox import FormatError



def read_matrices (path):
    """
    Данная функция либо возвращает две матрицы прочитанные из входного файла c расположением path,
                              либо сообщает об ошибке.

    Функция проверит корректность введенных матриц по следующим критериям :
                                    1) Матрица имеет фиксированную длину строки
    :param path:
    :return: matrix1, matrix2
    """
    with open (path, 'r') as input:
        matrix1 = []
        matrix2 = []
        current_matrix = matrix1

        matrix_number = 1
        line_number = 0

        for line in input:
            stripped_line = line.strip()
            if stripped_line == "" :
                current_matrix, matrix_number = matrix2, 2
                line_number = 0
                continue
            else :
                matrix_line = stripped_line.split()
                countrow = len(matrix_line)
                if line_number != 0 and countrow != len(current_matrix[0]):
                    raise FormatError ("Неверный формат матрицы")

                current_matrix.append(matrix_line)
                line_number +=1

    return matrix1, matrix2


def check_multiplication(matrix1, matrix2):
    """

    :param matrix1:
    :param matrix2:
    """
    if len(matrix1[0]) == len(matrix2):
        return True
    else:
        raise ValueError("Количество столбцов 1-й матрицы не совпадает с количеством строк 2-й матрицы.\n"
                         "Умножение невозможно")


def matrix_mult (matrix1, matrix2):

    m = len(matrix1) # количество строк в matrix1
    n = len(matrix2) # количество столбцов в matrix1 и количество строк в matrix2
    p = len(matrix2[0]) #количество столбцов в matrix2

    mult_matrix = [[0] * p  for _ in range(m)]

    for i in range(m):
        for j in range(p):
            for k in range(n):
                mult_matrix[i][j] += int(matrix1[i][k]) * int(matrix2[k][j])
    return mult_matrix

def write_matrix (path, matrix):
    """
    Данная функция записывает результирующую матрицу в файл с путем path.
    :param path:
    :param matrix:
    """
    with open(path, 'w') as output:
        for row in matrix:
            outstr = ' '.join(map(str, row))
            output.write(outstr)
            output.write("\n")


parser = argparse.ArgumentParser(
    prog = 'matrix_mult',
    description = 'This program can multiply matrices'
)
parser.add_argument('inputpath', type = str, help='Path to the input file with matrices')
parser.add_argument('outputpath', type = str, help='Path to the output file with the resulting matrix')
args = parser.parse_args()


try :
    matrix1, matrix2 = read_matrices (args.inputpath)
    try :
        check = check_multiplication(matrix1, matrix2)
        multmatrix = matrix_mult(matrix1, matrix2)
        write_matrix(args.outputpath, multmatrix)

    except ValueError as ve :
        print(f"Ошибка:{ve}")

except FormatError as fe:
    print (f"Ошибка:{fe}")
