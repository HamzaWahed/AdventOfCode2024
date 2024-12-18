import sys


def monotonic(report):
    return all(x < y for x, y in zip(report, report[1:])) or all(
        x > y for x, y in zip(report, report[1:])
    )


def difference(report):
    for i in range(len(report) - 1):
        diff = abs(report[i + 1] - report[i])
        if diff < 1 or diff > 3:
            return False

    return True


def main():
    reports = []
    count = 0
    with open(sys.argv[1], "r") as f:
        for line in f:
            row = list(map(int, line.split()))
            reports.append(row)

    for i in range(len(reports)):
        if monotonic(reports[i]) and difference(reports[i]):
            count += 1

    print(count)


main()
