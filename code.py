def arithmetic_arranger(problems, show_answers=False):
    
    #This stores and makes a list of the formatted problems to output
    answers = []
    aligned_first_operand = []
    aligned_second_operand = []
    dash = []
    results = []
    #1st problem (length of problems)
    if len(problems) > 5:
        return 'Error: Too many problems.' 
    #Need to split the problem first in parts
    for problem in problems:
        individual_problems = problem.split()
        first_operand = individual_problems[0]
        second_operand = individual_problems[2]
        operator = individual_problems[1]
    
    #Getting the width count of the longest operand
        longest_operand = max(len(first_operand), len(second_operand))
        align = longest_operand + 2
    #Right alignment
        aligned_first_operand.append(first_operand.rjust(align))
        aligned_second_operand.append(operator + " "+second_operand.rjust(longest_operand))
        dash.append("-" * align)
    #2nd problem (only + and - operators accepted)
    #Specify the operators
        if operator != '+' and operator !='-':
            return "Error: Operator must be '+' or '-'."  
    #3rd problem (operands should only contain digits)
        if not first_operand.isdigit() or not second_operand.isdigit():
            return 'Error: Numbers must only contain digits.'     
    #4th problem (operands can only be max 4 digits)
        if len(first_operand) > 4 or len(second_operand) > 4:
            return 'Error: Numbers cannot be more than four digits.'

    #Getting the answers to the sums
        first_operand = int(first_operand)
        second_operand = int(second_operand)
        if operator == "+":
            answer = first_operand + second_operand
        else:
            answer = first_operand - second_operand

    #5th problem: Display format as
    # - operator is on the same line as second operand
    # - single space between operator and longest of two operands
    # - if show_answers = True, display results
    # - numbers should be right aligned
    # - there should be four spaces between each problem

    #to get rid brackets and commas for lists, we need to join the list elements into a single string first.
        top_row = "    ".join(aligned_first_operand)
        bottom_row = "    ".join(aligned_second_operand)
        dash_row = "    ".join(dash)
    #to display the results after applying maths, need to turn is back into string
        if show_answers:
            results.append(str(answer).rjust(align))
    
    if show_answers:
        results_row = "    ".join(results)
        return (f'{top_row}\n{bottom_row}\n{dash_row}\n{results_row}')
    else:
        return (f'{top_row}\n{bottom_row}\n{dash_row}')
    
print (arithmetic_arranger(["32 + 698", "3801 - 2", "45 + 43", "123 + 49"], False))
# print(f'\n{arithmetic_arranger(["32 + 698", "3801 - 2", "45 + 43", "123 + 49"])}')