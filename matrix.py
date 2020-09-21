from pprint import pprint


matrix = [[[i]for i in range(10)] for i in range(10)]
matrix[3][4] = ['A']
pprint(matrix)
