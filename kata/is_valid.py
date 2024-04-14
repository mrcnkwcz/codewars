def isValid(formula):
    flag = False
    if 7 in formula or 8 in formula:
        flag = True
        if 5 in formula and 6 in formula:
            flag = True
        elif 5 in formula or 6 in formula:
            flag = False
        if (1 in formula and 2 in formula):
            flag = False
        if (3 in formula and 4 in formula):
            flag = False
    return flag
