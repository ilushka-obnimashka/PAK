import argparse

def calculation_of_pascal_triangle(height):
    bincoef = [[0] * (height) for _ in range(height)] 

    for i in range (height):
        for j in range (height):
            if j == 0 or i == j :
                bincoef [i][j] = 1
            else:
                bincoef[i][j]=bincoef[i-1][j-1]+bincoef[i-1][j]

    return bincoef

def print_pascal_triangle(height, bincoef):
    
    for currentheight in range (height):
        print ((height-currentheight-1) * "  ", end = "")
        for i in range (currentheight+1):
            print(f"{bincoef[currentheight][i]}  ", end = "")
        print()
    return

    

parser = argparse.ArgumentParser(
    prog = 'pascal_triangle',
    description = 'This program is needed to study the argparse module',
)
parser.add_argument('N', type = int)
args = parser.parse_args()

print_pascal_triangle(args.N, calculation_of_pascal_triangle(args.N))







