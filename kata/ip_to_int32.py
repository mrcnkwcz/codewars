# https://docs.python.org/3/library/ipaddress.html
import ipaddress as ipaddr


def ip_to_int32(ip):
    return int(ipaddr.ip_address(ip))
