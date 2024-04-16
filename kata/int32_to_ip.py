# https://docs.python.org/3/library/ipaddress.html
import ipaddress as ipaddr


def int32_to_ip(int32):
    return str(ipaddr.IPv4Address(int32))
