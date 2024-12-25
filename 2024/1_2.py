# Total similarity values between two columns of numbers
def similarity_score(col1:list[int], col2:list[int]) -> int:
    total_similarity_score: int = 0

    for element in col1:
        count_occurrences: int = col2.count(element)
        similarity_score: int = element * count_occurrences
        total_similarity_score += similarity_score

    return total_similarity_score


def main():
    col1: list[int] = []
    col2: list[int] = []

    input_file = open('2024/1.input', 'r')
    input_lines = input_file.readlines()

    for line in input_lines:
        column_of_numbers = line.strip().split()
        col1.append(int(column_of_numbers[0]))    
        col2.append(int(column_of_numbers[1]))

    input_file.close()
    print(similarity_score(col1, col2))


if __name__ == '__main__':
    main()
    