def flick_switch(lst):
    f = True
    ans = []
    for l in lst:
        if l == 'flick':
            f = not f
        ans.append(f)
    return ans
