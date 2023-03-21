

def convert_sample_to_suit(sample_file_name):
    with open(sample_file_name) as f:
        first_multiple_input = f.readline().rstrip().split()
        # n = int(first_multiple_input[0])
        k = int(first_multiple_input[1])
        arr = list(map(int, f.readline().rstrip().split()))
    return (k, arr)


PAIRS_TS = [
    (convert_sample_to_suit(
        './hrank/pairs/tests/fixtures/sample_0.txt'), 3),
    (convert_sample_to_suit(
        './hrank/pairs/tests/fixtures/sample_1.txt'), 0),
]


if __name__ == '__main__':
    print(PAIRS_TS)
