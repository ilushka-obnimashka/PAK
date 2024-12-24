import argparse
from importlib.resources import read_text
from mailbox import FormatError
from uuid import NAMESPACE_X500


def read_matrices (path):
    """
    Данная функция либо возвращает две матрицы прочитанные из входного файла c расположением path,
                              либо сообщает об ошибке.

    Функция проверит корректность введенных матриц по следующим критериям :
                                    1) Матрица имеет фиксированную длину строки
    :param path: путь к файлу для чтения
    :return: matrix1, matrix2 - прочитанные матрицы
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
                    raise FormatError ("Не верный формат матрицы")

                current_matrix.append(matrix_line)
                line_number +=1

    return matrix1, matrix2

def check_convolution_operation(matrix1, matrix2):
    """
    Данная функция возвращает результирующую матрицу.
    """
    if len(matrix1) >= len(matrix2) and len(matrix1[0]) >= len(matrix2[0]):
        return True
    else:
        raise ValueError("Размер второй матрицы больше первой.\n"
                         "Операция свертки невозможна")


def convolution_operation(A, B):
    """
    Данная функция выполняет операцию свертки над парой матриц matrix1, matrix2.
    Ищет свертку 1-ой матрицы со 2-ой матрицей. Вторая матрица используется как ядро свертки.

    Свертка (англ. convolution) — операция над парой матриц A(размера nx×ny) и B(размера mx×my),
    результатом которой является матрица C=A∗B размера (nx−mx+1)×(ny−my+1)

    :param matrix1: матрица A(размера nx×ny)
    :param matrix2: матрица B(размера mx×my)
    :return matrix: матрица C=A∗B размера (nx−mx+1)×(ny−my+1)
    """
    nx, ny = len(matrix1), len(matrix1[0])
    mx, my = len(matrix2), len(matrix2[0])

    rowC = nx - mx + 1
    columnC = ny - my + 1

    C = [[0] * columnC for _ in range(rowC)]

    #C[i][j] =∑ (mx−1)(u = 0) ∑(my−1)(v = 0) A[i + u][j + v] * B[u][v]


    for i in range(rowC):
        for j in range(columnC):
            for u in range (mx):
                for v in range(my):
                    C[i][j] += int(A[i+u][j+v]) * int(B[u][v])
    return C

def write_matrix (path, matrix):
    """
    Данная функция записывает результирующую матрицу в файл с путем path.
    :param path: путь к файлу для записи
    :param matrix: матрица для записи
    """
    with open(path, 'w') as output:
        for row in matrix:
            outstr = ' '.join(map(str, row))
            output.write(outstr)
            output.write("\n")



parser = argparse.ArgumentParser(
    prog = 'convolution operation',
    description = 'This program implements the convolution operation'
)
parser.add_argument('input', type = str, help = 'The input file with matrices')
parser.add_argument('output', type = str, help = 'The ooutput file with result matrices')
args = parser.parse_args()

try :
    matrix1, matrix2 = read_matrices(args.input)

    try:
        check_convolution_operation(matrix1, matrix2)
        convolution_operation(matrix1, matrix2)
        write_matrix(args.output, matrix1)

    except ValueError as ve:
        print(f"Error: {ve}")

except FormatError as fe:
    print(f"Error: {fe}")
