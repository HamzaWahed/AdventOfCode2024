list_1 = []
list_2 = []


def read_list(filename: str):
    input_size = 0
    with open(filename, "r") as file:
        for line in file:
            num1, num2 = map(int, line.split())
            list_1.append(num1)
            list_2.append(num2)
            input_size = input_size + 1

    return input_size


def find_similarity(input_size):
    s = 0
    for num in list_1:
        matches = [x for x in list_2 if x == num]
        s += len(matches) * num

    return s


def main():
    input_size = read_list("day1-input.txt")
    s = find_similarity(input_size)
    print(s)


main()
