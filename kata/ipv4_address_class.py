classes = {
    "0": "A",
    "10": "B",
    "110": "C",
    "1110": "D",
    "1111": "E",
}


def ipv4_address_class(ipv4_addr):
    for pre, c in classes.items():
        if bin(int(ipv4_addr.split(".")[0]))[2:].zfill(8).startswith(pre):
            return c
