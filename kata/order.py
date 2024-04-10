import re


def order(sentence):
    ans = {}
    for s in sentence.split():
        try:
            match = re.search(r"(\d)", s).group()
            ans[match] = s
        except AttributeError:
            continue
    return " ".join([ans[k] for k in sorted(ans.keys())])
