def cakes(recipe, available):
    p = []
    for pos, n in recipe.items():
        if not available.get(pos) or n > available.get(pos):
            return 0
        p.append(available.get(pos) // n)
    return min(p)
