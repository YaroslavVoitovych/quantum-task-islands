from islands_counter import islands_counter

def test_1():
    # Inputs
    M = 9
    N = 10
    A = [
        [0 for i in range(N)] for j in range(M)
    ]
    A[0][-1] = 1
    A[5][0] = 1
    A[6][0] = 1
    A[-1][1] = 1
    A[-1][2] = 1
    A[-1][3] = 1
    A[-2][2] = 1
    A[6][-1] = 1
    A[2][3] = 1
    A[3][3] = 1
    A[4][3] = 1
    A[4][2] = 1
    A[4][4] = 1
    A[4][5] = 1
    A[3][4] = 1
    A[3][5] = 1
    A[2][5] = 1
    A[5][6] = 1
    A[6][6] = 1
    assert islands_counter(A, N, M) == 6

def test_2():
    N = 3
    M = 3
    A = [[0, 1, 0],
         [0, 0, 0],
         [0, 1, 1]]
    assert islands_counter(A, N, M) == 2

def test_3():
    N = 10
    M = 10
    A = [
        [1 for i in range(N)] for j in range(M)
    ]
    assert islands_counter(A, N, M) == 1

def test_4():
    M = 3
    N = 4
    A = [[0, 0, 0, 1],
        [0, 0, 1, 0],
        [0, 1, 0, 0]]
    assert islands_counter(A, N, M) == 3

def test_5():
    M = 3
    N = 4
    A = [[1, 1, 1, 1],
        [0, 0, 0, 1],
        [1, 1, 1, 1]]
    assert islands_counter(A, N, M) == 1

def test_6():
    M = 3
    N = 4
    A = [[1, 1, 1, 1],
        [1, 0, 0, 1],
        [1, 1, 1, 1]]
    assert islands_counter(A, N, M) == 1

