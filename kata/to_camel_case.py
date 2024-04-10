import re


def to_camel_case(text):
    if text:
        pattern = re.compile(r"([a-zA-Z]+)")
        matches = re.findall(pattern=pattern, string=text)
        return matches.pop(0) + "".join([m.capitalize() for m in matches])
    return ""
