def transpose_matrix(array_2d: list[list[int]]):

    if len(array_2d) == 0:
        return [[0]]
    
    row_size = len(array_2d)
    col_size = len(array_2d[0])

    transposed_matrix = [[0] * row_size for _ in range(col_size)]

    for row in range(row_size):
        for col in range(col_size):
            transposed_matrix[col][row] = array_2d[row][col]

    return transposed_matrix

def test():
    def test_1():
        print("Test 1")
        matrix = [[5, 7, 8], [2, 6, 1], [3, 9, 0]]
        print(transpose_matrix(matrix))

    def test_2():
        print("Test 2")
        matrix = [[5, 7, 8, 0], [2, 6, 1, 7], [3, 9, 0, 5]]
        print(transpose_matrix(matrix))

    def test_3():
        print("Test 3")
        matrix = [[1, 2], [3, 4], [5, 6]]
        print(transpose_matrix(matrix))

    def test_4():
        print("Test 4")
        matrix = [[1]]
        print(transpose_matrix(matrix))

    def test_5():
        print("Test 5")
        matrix = [[1, 2, 3]]
        print(transpose_matrix(matrix))

    def test_6():
        print("Test 6")
        matrix = []
        print(transpose_matrix(matrix))

    test_1()
    test_2()
    test_3()
    test_4()
    test_5()
    test_6()

test()