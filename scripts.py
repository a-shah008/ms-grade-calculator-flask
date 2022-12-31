
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

    f_assignments = str(f_assignments).strip().split(",")
    s_assignments = str(s_assignments).strip().split(",")

    new_f_assignments, new_s_assignments = strip_string(f_assignments, s_assignments)

    return new_f_assignments, new_s_assignments

