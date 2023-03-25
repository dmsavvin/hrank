'''
See exercise description at
https://www.hackerrank.com/challenges/connected-cell-in-a-grid/problem
'''


def _get_1d_from_2d(_2d, dim):
    return _2d[0] * dim[1] + _2d[1]


def _get_2d_from_1d(_1d, dim):
    return _1d // dim[1], _1d % dim[1]


def _find(p, id):
    while id[p] != p:
        p = id[p]
    return p


def _union(p, q, id, sz, max_size):
    p_root = _find(p, id)
    q_root = _find(q, id)
    if p_root == q_root:
        return max_size
    if sz[p_root] >= sz[q_root]:
        big, small = p_root, q_root
    else:
        big, small = q_root, p_root
    id[small] = big
    sz[big] += sz[small]
    if sz[big] > max_size:
        max_size = sz[big]
    return max_size


def _get_neighbors(_2d, dim):
    directions = ((1, 0),
                  (1, 1),
                  (0, 1),
                  (-1, 1),
                  (-1, 0),
                  (-1, -1),
                  (0, -1),
                  (1, -1)
                  )
    for dir in directions:
        neighbor_row = _2d[0] + dir[0]
        neighbor_col = _2d[1] + dir[1]
        if 0 <= neighbor_row < dim[0] and 0 <= neighbor_col < dim[1]:
            yield neighbor_row, neighbor_col


def connected_cells_in_grid(matrix):
    dim = (len(matrix), len(matrix[0]))
    id = [i for i in range(dim[0] * dim[1])]
    sz = [matrix[i][j] for i in range(dim[0]) for j in range(dim[1])]
    max_size = 0
    for _1d in range(dim[0] * dim[1]):
        r, c = _get_2d_from_1d(_1d, dim)
        if not matrix[r][c]:
            continue
        if not max_size:
            max_size = 1
        for r_n, c_n in _get_neighbors((r, c), dim):
            _1d_n = _get_1d_from_2d((r_n, c_n), dim)
            if matrix[r_n][c_n]:
                max_size = _union(_1d, _1d_n, id, sz, max_size)
    return max_size
