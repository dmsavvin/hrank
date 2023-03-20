

def convert_sample_to_suit(sample_file_name):
    with open(sample_file_name) as f:
        first_multiple_input = f.readline().rstrip().split()
        n = int(first_multiple_input[0])
        k = int(first_multiple_input[1])
        second_multiple_input = f.readline().rstrip().split()
        r_q = int(second_multiple_input[0])
        c_q = int(second_multiple_input[1])
        obstacles = []
        for _ in range(k):
            obstacles.append(list(map(int, f.readline().rstrip().split())))
    return (n, k, r_q, c_q, obstacles)


QUEENS_ATTACK_TS = [
    (convert_sample_to_suit(
        './hrank/queens_attack_2/tests/fixtures/sample_0.txt'), 9),
    (convert_sample_to_suit(
        './hrank/queens_attack_2/tests/fixtures/sample_1.txt'), 10),
    (convert_sample_to_suit(
        './hrank/queens_attack_2/tests/fixtures/sample_2.txt'), 0),
    (convert_sample_to_suit(
        './hrank/queens_attack_2/tests/fixtures/sample_3.txt'), 110198)
]


if __name__ == '__main__':
    print(QUEENS_ATTACK_TS)
