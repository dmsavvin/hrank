'''
See exercise description at
https://www.hackerrank.com/challenges/larrys-array/problem

Math reference
https://math.stackexchange.com/questions/415970/how-to-determine-the-parity-
of-a-permutation-by-its-cycle-decomposition
'''


def larry_s_array(A):

    n = len(A)

    c = 0  # amount of cycles in permutation A
    A_ = list(range(1, n + 1))  # sorted A

    # calculate amount of cycles in the permutation A
    for i in range(n):
        if A_[i] > n:
            continue
        c += 1
        A_[i] += n  # mark as visited
        j = A[i] - 1
        while A_[j] <= n:
            temp = A[j] - 1
            A_[j] += n  # mark as visited
            j = temp

    # Parity of the number of inversion in the permutation is an invariant for
    # the given transformation. For the sorted array parity == 1.
    pairity = (-1) ** (n - c)

    if pairity == 1:
        return 'YES'
    else:
        return 'NO'
