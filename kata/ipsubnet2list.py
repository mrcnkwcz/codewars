import ipaddress as ipaddr


def ipsubnet2list(subnet):
    """Generate list all posible ip addresses from a network."""
    try:
        return [str(addr) for addr in ipaddr.IPv4Network(subnet).hosts()]
    except ipaddr.AddressValueError as err:
        print("Subnet is not valid:", err)
