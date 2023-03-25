

def convert_sample_to_suit(sample_file_name):
    with open(sample_file_name) as f:
        n = int(f.readline().strip())
        _ = int(f.readline().strip())
        matrix = []
        for _ in range(n):
            matrix.append(list(map(int, f.readline().rstrip().split())))

    return matrix


CONNECTED_CELLS_TS = [
    (convert_sample_to_suit(
        './hrank/connected_cells_in_grid/tests/fixtures/sample_0.txt'), 5),
    (convert_sample_to_suit(
        './hrank/connected_cells_in_grid/tests/fixtures/sample_1.txt'), 10),
    (convert_sample_to_suit(
        './hrank/connected_cells_in_grid/tests/fixtures/sample_2.txt'), 0),
    (convert_sample_to_suit(
        './hrank/connected_cells_in_grid/tests/fixtures/sample_3.txt'), 9),
]
