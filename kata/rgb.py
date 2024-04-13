def rgb(r, g, b):
    return "".join(
        map(
            lambda color: hex(color)[2:].zfill(2).upper() if color > 0 else "00",
            map(lambda color: color if color < 256 else 255, (r, g, b)),
        )
    )
