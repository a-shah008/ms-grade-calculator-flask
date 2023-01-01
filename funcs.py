
def check_formative_weight_num(fw):
    try:
        fw = int(fw)
    except:
        return False
    return True

def check_summative_weight_num(sw):
    try:
        sw = int(sw)
    except:
        return False
    return True

def check_all_inputs(fw, sw):
    proper_formative_inputs = check_formative_weight_num(fw)
    proper_summative_inputs = check_summative_weight_num(sw)
    if proper_formative_inputs == True and proper_summative_inputs == True and int(fw) + int(sw) == 100:
        return True

    return False

def strip_string(f_a, s_a):
    new_f_assignments = []
    new_s_assignments = []

    for i in f_a:
        new_f_assignments.append(str(i).strip())
    for j in s_a:
        new_s_assignments.append(str(j).strip())

    return new_f_assignments, new_s_assignments

def format_assignment_inputs(f_assignments, s_assignments):

    try:
        f_assignments = str(f_assignments).strip().split(",")
        s_assignments = str(s_assignments).strip().split(",")

        new_f_assignments, new_s_assignments = strip_string(f_assignments, s_assignments)

        return new_f_assignments, new_s_assignments
    except:
        return False

def formative_calculation(formative_assignments, formative_weight):
    try:
        numerators = []
        denominators = []
        for assignment in formative_assignments:
            all_nums_separated = list(assignment.split("/"))
            numerators.append(int(all_nums_separated[0]))
            denominators.append(int(all_nums_separated[1]))
        percentage = float(int(sum(numerators)) / int(sum(denominators)))
        final_ans = float(percentage * (float(formative_weight) / 100))
        return final_ans
    except:
        return False

def summative_calculation(summative_assignments, summative_weight):
    try:
        numerators = []
        denominators = []
        for assignment in summative_assignments:
            all_nums_separated = list(assignment.split("/"))
            numerators.append(int(all_nums_separated[0]))
            denominators.append(int(all_nums_separated[1]))
        percentage = float(int(sum(numerators)) / int(sum(denominators)))
        final_ans = float(percentage * (int(summative_weight) / 100))
        return final_ans
    except:
        return False
