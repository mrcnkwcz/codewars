import ipaddress


def network_cidr(ipv4_addr: str, net_mask: str) -> str:
    net = ".".join(map(lambda x, y: x & y, ipv4_addr.split("."), net_mask.split(".")))
    return ipaddress.IPv4Network(net).exploded
