list_1 = []
list_2 = []
difference = []


def read_list(filename: str):
    input_size = 0
    with open(filename, "r") as file:
        for line in file:
            num1, num2 = map(int, line.split())
            list_1.append(num1)
            list_2.append(num2)
            input_size = input_size + 1

    return input_size


def find_diff(input_size):
    small_1 = 0
    small_2 = 0
    for _ in range(input_size):
        small_1 = min(list_1)
        small_2 = min(list_2)
        difference.append(abs(small_1 - small_2))
        list_1.remove(small_1)
        list_2.remove(small_2)


def main():
    input_size = read_list("day1-input.txt")
    find_diff(input_size)
    print(sum(difference))


main()
