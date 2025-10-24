# define the main function with optional show_answers argument
def arithmetic_arranger(problems, show_answers=False):
    # check if too many problems are provided
    if len(problems) > 5:
        return 'Error: Too many problems.'

    # initialize lists to hold each line of output
    first_line = []
    second_line = []
    dashes = []
    answers = []

    # loop through each arithmetic problem
    for problem in problems: 
        parts = problem.split()
        first, operator, second = parts

        # check for valid operators
        if operator not in ['+','-']:
            return "Error: Operator must be '+' or '-'."

        # ensure both numbers contain only digits
        if not first.isdigit() or not second.isdigit():
            return 'Error: Numbers must only contain digits.'

        # ensure both numbers are no longer than four digits
        if len(first) > 4 or len(second) >4:
            return 'Error: Numbers cannot be more than four digits.'

        # determine width based on longest operand plus space for operator
        width = max(len(first),len(second)) + 2

        # format each line so numbers are right-aligned
        top = first.rjust(width)
        bottom = operator + second.rjust(width - 1)
        line = '-' * width

        # perform addition or subtraction
        if operator == '+':
            result = str(int(first) + int(second))
        else: 
            result = str(int(first) - int(second))

        # right-align the answer to match the problem width
        answer = result.rjust(width)

        # add formatted strings to their corresponding lists
        first_line.append(top)
        second_line.append(bottom)
        dashes.append(line)
        answers.append(answer)

    # join all parts with four spaces between problems
    arranged = '    '.join(first_line) + '\n' + '    '.join(second_line) + '\n' + '    '.join(dashes)

    # include answers if show_answers is set to true
    if show_answers:
        arranged += '\n' + '    '.join(answers)
        
    return arranged

# example call to test the function
print(f'\n{arithmetic_arranger(["32 + 698", "3801 - 2", "45 + 43", "123 + 49"])}')
