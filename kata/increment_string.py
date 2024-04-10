import re


def increment_string(s):
    pattern = re.compile(r"\d+$")
    match = re.search(pattern, s)
    return (
        re.sub(pattern, str(int(match.group()) + 1).zfill(len(match.group())), s)
        if match
        else s + "1"
    )
