import sys
from colorama import Fore, Style
from scripts import check_all_inputs, format_assignment_inputs

print("\n\n\n" + Fore.GREEN + "Program successfully started running..." + Style.RESET_ALL + "\n\n\n\n")
Style.RESET_ALL

input_retrieved = False
while input_retrieved == False:
    f_weight = input("Enter formative weight (e.g. 10, 20, 40): ")
    s_weight = input("Enter summative weight (e.g. 90, 80, 60): ")
    f_assignments = input("Enter your entire list of formative assignments, as [your points]/[max points receivable], separating each item with a comma: ")
    s_assignments = input("Enter your entire list of summative assignments, as [your points]/[max points receivable], separating each item with a comma: ")

    proper_inputs = check_all_inputs(f_weight, s_weight)

    if proper_inputs == True:
        break
    else:
        input_retrieved = False
        print("\nIncorrect input(s). Please try again.\n")

fa, sa = format_assignment_inputs(f_assignments, s_assignments)




print("\n\n\n" + Fore.GREEN + "Program successfully finished running. No issues encountered." + Style.RESET_ALL + "\n\n")
