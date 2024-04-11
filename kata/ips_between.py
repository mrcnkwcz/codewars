import ipaddress as ipaddr


def ips_between(start, end):
    return int(ipaddr.IPv4Address(end)) - int(ipaddr.IPv4Address(start))
