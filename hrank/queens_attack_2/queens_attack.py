'''
See exercise description at
https://www.hackerrank.com/challenges/queens-attack-2/problem
'''


def _has_direction(vector, direction):
    dot_product = vector[0] * direction[0] + vector[1] * direction[1]
    vector_length_squared = vector[0] ** 2 + vector[1] ** 2
    direction_length_squared = direction[0] ** 2 + direction[1] ** 2
    cos_squared = (dot_product ** 2
                   // (vector_length_squared * direction_length_squared))
    return dot_product > 0 and cos_squared == 1


def _dist(obst):
    return max(abs(obst[0]), abs(obst[1])) - 1


def queens_attack(n, k, r_q, c_q, obstacles):
    directions = {
        'UP-LEFT': (1, -1),
        'UP': (1, 0),
        'UP-RIGHT': (1, 1),
        'RIGHT': (0, 1),
        'DOWN-RIGHT': (-1, 1),
        'DOWN': (-1, 0),
        'DOWN-LEFT': (-1, -1),
        'LEFT': (0, -1)
    }
    up, right, down, left = (n - r_q, n - c_q, r_q - 1, c_q - 1)
    attackable = {
        'UP-LEFT': min(up, left),
        'UP': up,
        'UP-RIGHT': min(up, right),
        'RIGHT': right,
        'DOWN-RIGHT': min(down, right),
        'DOWN': down,
        'DOWN-LEFT': min(down, left),
        'LEFT': left
    }
    for obst in map((lambda x: (x[0] - r_q, x[1] - c_q)), obstacles):
        for dir in directions:
            if (_has_direction(obst, directions[dir])
                    and _dist(obst) < attackable[dir]):
                attackable[dir] = _dist(obst)
                break
    return sum(attackable.values())
