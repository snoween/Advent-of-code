# Total distance between two columns of numbers
def total_distance(col1: list[int], col2: list[int]) -> int:
    total_distance: int = 0

    col1.sort()
    col2.sort()

    for element in range(len(col1)):
        element_distance: int = abs(col1[element] - col2[element])
        total_distance += element_distance

    return total_distance


def main():
    col1: list[int] = []
    col2: list[int] = []

    input_file = open("2024/1.input", "r")
    input_lines = input_file.readlines()

    for line in input_lines:
        column = line.rstrip().split(" ")
        col1.append(int(column[0]))
        col2.append(int(column[3]))
    input_file.close()

    print(total_distance(col1, col2))

if __name__ == "__main__":
    main()

