import subprocess
import ipaddress

def ping_ip(ip):
    """
    Ping the specified IP address once.
    Return True if the IP is reachable, False otherwise.
    """
    result = subprocess.run(['ping', '-n', '1', '-w', '1000', ip],
                            stdout=subprocess.PIPE, stderr=subprocess.PIPE,
                            text=True, encoding='utf-8')
    return result.returncode == 0

def inspect_apipa_ips():
    base_network = ipaddress.IPv4Network('169.254.0.0/16')

    # Loop through each IP address in the APIPA range (169.254.0.1 to 169.254.255.254)
    for ip in base_network.hosts():
        ip_str = str(ip)
        print(f"Pinging {ip_str}...")

        # Ping the IP address
        if ping_ip(ip_str):
            print('')
            print(f"{ip_str} is reachable. :)")
            print('')
        else:
            print(f"{ip_str} is not reachable. :(")

if __name__ == "__main__":
    inspect_apipa_ips()
