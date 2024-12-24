import argparse
import random

def bubble_sort(arr):
    for i in range(len(arr)):
        for j in range(len(arr)-1,i,-1):
            if arr[j-1]>arr[j]:
                temp = arr[j-1]
                arr[j-1] = arr[j]
                arr[j] = temp

parser = argparse.ArgumentParser(
    prog = 'bubble_sort',
    description = 'This program is needed to study the argparse module',
)
parser.add_argument('listlength', type = int)
args = parser.parse_args()

numbers = []
for i in range(args.listlength):
    numbers.append(random.random())

bubble_sort(numbers)

for i in numbers:
    print(i)