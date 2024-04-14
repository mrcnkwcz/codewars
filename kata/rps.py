def rps(p1, p2):
    if p1 == p2:
        return "Draw!"
    for x in ("scissors", "paper"), ("paper", "rock"), ("rock", "scissors"):
        if p1 == x[0] and p2 == x[1]:
            return "Player 1 won!"
    return "Player 2 won!"
