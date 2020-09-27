from pprint import pprint


matrix = [[[i] for i in range(10)] for i in range(10)]
matrix[3][4] = ['@']
#pprint(matrix)
similar_matrix_orig = []

def find_pose():
    for i in range(len(matrix)):
        for j in range(len(matrix[i])):
            if matrix[i][j] == ['@']:
                return (i, j)


def give_similar_matrix(pose, end=1, end_2=1):
    similar_matrix = []
    some_matrix = []
    for j in range(pose[0]-end_2, pose[0]+end_2+1):
        for i in range(pose[1]-end, pose[1]+end+1):
            some_matrix.append(matrix[j][i])
        similar_matrix.append(some_matrix.copy())
        some_matrix.clear()

    for i in similar_matrix:
        print(i)


give_similar_matrix(find_pose(), int(input()), int(input()))
# создать матр ицу 3 на 3
