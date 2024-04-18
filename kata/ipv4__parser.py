def ipv4__parser(ip_addr, mask):
    subnet_list = list(
        map(lambda x, y: str(int(x) & int(y)), ip_addr.split("."), mask.split("."))
    )
    host_map = map(lambda x, y: str(int(x) - int(y)), ip_addr.split("."), subnet_list)
    return ".".join(subnet_list), ".".join(host_map)
