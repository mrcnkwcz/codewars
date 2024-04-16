def ipv4_to_binary(ipv4_addr: str) -> str:
    return ".".join(bin(int(o))[2:].zfill(8) for o in ipv4_addr.split("."))
