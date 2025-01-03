def check_report(input_line) -> int:
    num_safe_reports = 0
    
    for list_of_numbers in input_line:
        stack = []
        for i in range(len(list_of_numbers)-1):
            # Check if the list increases by 1-3
            if 0 < list_of_numbers[i+1] - list_of_numbers[i] <= 3:
                stack.append(1)
                if len(stack) == len(list_of_numbers)-1 and sum(stack) == len(list_of_numbers)-1:
                    num_safe_reports += 1

            if 0 < list_of_numbers[i] - list_of_numbers[i+1] <= 3: 
                stack.append(0)
                if len(stack) == len(list_of_numbers)-1 and sum(stack) == 0:
                    num_safe_reports += 1          
    return num_safe_reports


def main():
    input_line = []
    input_file = open('2.input', 'r')
    input_lines = input_file.readlines()
    for line in input_lines:
        list_of_numbers = line.strip().split()
        list_of_numbers = [int(i) for i in list_of_numbers]
        input_line.append(list_of_numbers)
    print(check_report(input_line))
    
if __name__ == '__main__':
    main()  