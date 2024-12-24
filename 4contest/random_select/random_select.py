import argparse
from random import uniform
import numpy as np

parser = argparse.ArgumentParser(
    prog = "random_select",
    description = 'This program is needed to study the numpy module'
)

parser.add_argument("file1", type = str)
parser.add_argument("file2", type = str)
parser.add_argument("P", type = float)
args = parser.parse_args()


def read_list(filename):
    list = []
    with open(filename,'r') as fin:
        for line in fin:
            list.extend(int(x) for x in line.split())
    return list

list1 = read_list(args.file1)
list2 = read_list(args.file2)


total_list1 = [elem2 if uniform(0,1) < args.P else elem1 for elem1, elem2 in zip(list1,list2)]
print(total_list1)

freq_in_list2 = np.random.uniform(0, 1, size=len(list2))
mask = np.where(freq_in_list2 < args.P)
mask = mask[0].tolist()

total_list2 = list1.copy()
total_list2 = np.array(total_list2)

list2 = np.array(list2)

total_list2[mask] = list2[mask]
total_list2 = total_list2.tolist()

print(total_list2)
