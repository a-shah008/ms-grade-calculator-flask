
from colorama import Fore, Style
from funcs import check_all_inputs, format_assignment_inputs, formative_calculation, summative_calculation

print("\n\n\n" + Fore.GREEN + "Program successfully started running..." + Style.RESET_ALL + "\n\n\n\n")
Style.RESET_ALL

f_weight, s_weight = 0, 0
input_retrieved = False
while input_retrieved == False:
    f_weight = input("\nEnter formative weight (e.g. 10, 20, 40): ")
    s_weight = input("\nEnter summative weight (e.g. 90, 80, 60): ")
    f_assignments = input("\nEnter your entire list of formative assignments, as [your points]/[max points receivable], separating each item with a comma: ")
    s_assignments = input("\nEnter your entire list of summative assignments, as [your points]/[max points receivable], separating each item with a comma: ")

    proper_inputs = check_all_inputs(f_weight, s_weight)

    if proper_inputs == True:
        break
    else:
        input_retrieved = False
        print("\n\n" + Fore.RED + "Incorrect input(s). Please try again." + Style.RESET_ALL + "\n")


fa, sa = None, None
if format_assignment_inputs(f_assignments, s_assignments):
    fa, sa = format_assignment_inputs(f_assignments, s_assignments)
else:
    print("\n\n" + Fore.RED + "There was an error in our system while processing your input. Please restart the program and try again." + Style.RESET_ALL + "\n")
    quit()

if formative_calculation(fa, f_weight) and summative_calculation(sa, s_weight):
    formative_ans = formative_calculation(fa, f_weight)
    summative_ans = summative_calculation(sa, s_weight)
    final_ans = (formative_ans + summative_ans) * 100
    print("\n\n\n\n\n" + Fore.GREEN + f"{final_ans}" + Style.RESET_ALL)
    print(Fore.GREEN + f"Your Final Grade: {round(final_ans, 2)}%" + Style.RESET_ALL + "\n\n\n")
else:
    print("\n\n" + Fore.RED + "There was an error in our system while processing your input. Please restart the program and try again." + Style.RESET_ALL + "\n")
    quit()


print("\n\n\n" + Fore.GREEN + "Program successfully finished running. No issues encountered." + Style.RESET_ALL + "\n\n")
