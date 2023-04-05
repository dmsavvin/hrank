'''
See exercise description at
https://www.hackerrank.com/challenges/queens-on-board/problem

The general idea is as follows:

Start with some sub board represented by row number of the first row
and under threat subset of the sub board. For the original board row
number = 0, under threat subset is empty.

Find all available (= queens should not be under threat) queens
arrangements for the first row of the sub board.

If the first row of the sub board is the last row of the original board
then the amount of the available queens arrangements (found above) is the
answer, else:

For each available queens arrangement find amount of ways to place queens
on the sub board started from the first_row + 1 given the updated under
threat subset (take into account additional queens from the chosen
arrangement). Here we ether get the memorized value or use recursive call
and then memorize the result.

Sum of the found amounts less 1 (to account for the empty board) it the
answer
'''


def line_to_intervals(line: str) -> tuple:
    '''Converts line from the board to a collection of intervals.

    Collection of intervals is stored as a list of tuples. Interval represents
    region of the line without obstacles bounded by obstacles or the line ends.

    Example:
      '..' -> ((0, 1))
      '...##..' -> ((0, 2), (5, 6))
      '##...#.#...' -> ((2, 4), (6, 6), (8, 10))
    '''
    begin = 0
    end = 0
    intervals = []
    while end < len(line):
        if line[end] == '#' and line[begin] == '#':
            end += 1
            begin = end
        elif line[end] == '.':
            end += 1
        else:
            intervals.append((begin, end - 1))
            end += 1
            begin = end
    else:
        if begin < len(line) and line[begin] == '.':
            intervals.append((begin, end - 1))
    return intervals


def get_line_queens_arrangements(row: int, intervals: tuple) -> tuple:
    '''Generate all possible arrangements of the queens for a given line.

    Line represents as row - line position in the board and the collection of
    the intervals that are generated from the line.

    Queen's position is stored as a tuple (i, j) where i and j are row and
    column within the board. Queens arrangement is stored as a frozenset of the
    queen's positions.

    Example:
      line: '...##..#'
      args: row = x, intervals = ((0, 2), (5, 6))
      result: ({}, {(x, 0)}, {(x, 1)}, {(x, 2)},
               {(x, 5)}, {(x, 0), (x, 5)}, {(x, 1), (x, 5)}, {(x, 2), (x, 5)},
               {(x, 6)}, {(x, 0), (x, 6)}, {(x, 1), (x, 6)}, {(x, 2), (x, 6)},
               )
    '''
    number_of_intervals = len(intervals)
    intervals_begins = [i for i, _ in intervals]
    intervals_lengths = [j - i + 1 for i, j in intervals]
    queens_columns = [0 for _ in intervals]
    queens_arrangements = []

    # Each interval has no more than 1 queen. Queen's column (element of
    # queens_columns) value can be 0, 1, 2, ..., len(interval). 0 is treated as
    # an absence of the queen in the given interval.
    while queens_columns != intervals_lengths:
        arrangement = frozenset((row, column + offset - 1)
                                for column, offset
                                in zip(queens_columns, intervals_begins)
                                if column > 0)
        queens_arrangements.append(arrangement)
        for i in range(number_of_intervals):
            queens_columns[i] = ((queens_columns[i] + 1)
                                 % (intervals_lengths[i] + 1))
            if queens_columns[i] != 0:
                break
    arrangement = frozenset((row, column + offset - 1)
                            for column, offset
                            in zip(queens_columns, intervals_begins)
                            if column > 0)
    queens_arrangements.append(arrangement)
    return tuple(queens_arrangements)


def get_all_queens_arrangements(board: list) -> list:
    '''Generate all possible queens arrangements for all lines in the board.

    Queens arrangements are stored in the list structure where each element
    referees to the queens arrangements for a particular line from the board.
    Index of the element and the index of the corresponding line within the
    board are the same.

    Example:
      board: ['...##..#',
              '...#####'
              ]
      result: [0]: ({}, {(0, 0)}, {(0, 1)}, {(0, 2)},
                    {(0,5)}, {(0,0), (0,5)}, {(0,1), (0,5)}, {(0,2), (0,5)},
                    {(0,6)}, {(0,0), (0,6)}, {(0,1), (0,6)}, {(0,2), (0,6)},
                    )
              [1]: ({}, {(1, 0)}, {(1, 1)}, {(1, 2)})
    '''
    queens_arrangements = []
    for row, line in enumerate(board):
        intervals = line_to_intervals(line)
        queens_arrangements.append(get_line_queens_arrangements(row,
                                                                intervals))
    return queens_arrangements


def get_under_threat_for_cells(board: list) -> dict:
    '''For each free cell in the board generates collection of the cells that
    are under threat if a queen will be placed in the given cell.

    Returns:
      The dict where keys are the cells without obstacles and the values are
      the frozensets of cells which are under threat if a queen will be placed
      in the position corresponding to key.
    '''
    under_threat_for_cells = dict()
    R = len(board)
    C = len(board[0])
    for i, j in ((i, j) for i in range(R)
                 for j in range(C) if board[i][j] != '#'):
        ut = set()
        directions = [[i, j, 1, 0],
                      [i, j, 1, 1],
                      [i, j, 0, 1],
                      [i, j, -1, 1],
                      [i, j, -1, 0],
                      [i, j, -1, -1],
                      [i, j, 0, -1],
                      [i, j, 1, -1]
                      ]
        ut.add((i, j))
        while directions:
            for d in directions:
                d[0] += d[2]
                d[1] += d[3]
                if 0 <= d[0] < R and 0 <= d[1] < C \
                   and board[d[0]][d[1]] != '#':
                    ut.add((d[0], d[1]))
                else:
                    d[0] = -1
            directions = [d for d in directions if d[0] != -1]
        under_threat_for_cells[(i, j)] = frozenset(ut)
    return under_threat_for_cells


def get_under_threat_for_arrangement(arrangements: list,
                                     under_threat_for_cells: dict) -> dict:
    '''For each queens arrangements generated from each board line generate
    frozenset of cells which are under threat given the queens arrangement.

    Returns:
      The dict where keys are all possible queens arrangements given the
      collection of lines in the board and the values are frozensets of cells
      which are under threat given the queens arrangement from the key.
    '''
    under_threat_for_arrangement = dict()
    for arrangements_for_row in arrangements:
        for arrangement in arrangements_for_row:
            ut = frozenset()
            for queen_position in arrangement:
                ut = ut | under_threat_for_cells[queen_position]
            under_threat_for_arrangement[arrangement] = ut
    return under_threat_for_arrangement


def queensBoard(board):
    MAX_RES = 10 ** 9 + 7
    last_row = len(board) - 1
    arrangements = get_all_queens_arrangements(board)
    under_threat_for_cells = get_under_threat_for_cells(board)
    under_threat_for_arrangements = \
        get_under_threat_for_arrangement(arrangements, under_threat_for_cells)

    # Keys are the tuples of the following kind:
    # (
    #  board row number,
    #  subset of the sub board (started from the number from the key) which is
    #      under threat given the queens placed above
    # )
    # Values are amounts of ways to place queens on the sub board started from
    # the row from the key and given the under threat subset from the key.
    memo = dict()

    def count(first_row, under_threat):
        '''Counts amount of ways to place queens on the sub board started from
        the row (row included) and given the under_threat - subset of sub board
        which is under threat given the queens placed above the row.
        '''
        available_arrangements = [arr for arr
                                  in arrangements[first_row]
                                  if not (arr & under_threat)]
        if first_row == last_row:
            return len(available_arrangements)
        res = 0
        new_first_row = first_row + 1
        for arr in available_arrangements:
            new_under_threat = frozenset(cell for cell
                                         in under_threat
                                         | under_threat_for_arrangements[arr]
                                         if cell[0] >= new_first_row)
            if (new_first_row, new_under_threat) in memo:
                arr_count = memo[(new_first_row, new_under_threat)]
            else:
                arr_count = count(new_first_row, new_under_threat)
                memo[(new_first_row, new_under_threat)] = arr_count
            res = (res + arr_count) % MAX_RES
        return res

    # Subtract 1 to account for the board without queens that is not allowed
    return (count(0, frozenset()) - 1) % MAX_RES
