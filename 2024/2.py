col1 = []
col2 = []



input_file = open('2024/1.input', 'r')
input_lines = input_file.readlines()
for line in input_lines:
    column_of_numbers = line.strip().split()
    col1.append(int(column_of_numbers[0]))    
    col2.append(int(column_of_numbers[1]))

input_file.close()

def similarity_score(col1, col2):
    total_similarity_score = 0

    for element in col1:
        count_occurrences = col2.count(element)
        similarity_score = element * count_occurrences
        total_similarity_score += similarity_score

    return total_similarity_score

print(similarity_score(col1, col2))   