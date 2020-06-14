def compute(case):
    matrix = []
    size = int(input())
    sum = 0
    rows = 0
    columns = 0
    for i in range(0,size):
        matrix.append(input().split(' '))
    # SUM the Diagonal
    for i in range(0,size):
        sum += int(matrix[i][i])
    # Check for Row Duplicates
    for array in matrix:
        if len(array) != len(set(array)):
            rows+=1
    for i in range(0,size):
        column = []
        for j in range(0,size):
            column.append(matrix[j][i])
        if len(column) != len(set(column)):
            columns+=1
    print("Case #{}: {} {} {}".format(case+1,sum,rows,columns))

if __name__ == "__main__":
    cases = int(input())
    for z in range(0,cases):
        compute(z)
