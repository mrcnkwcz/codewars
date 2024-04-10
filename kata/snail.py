def snail(snail_map):
    ans = []
    while snail_map:
        ans += snail_map.pop(0)
        snail_map = list(zip(*snail_map))[::-1]
    return ans
