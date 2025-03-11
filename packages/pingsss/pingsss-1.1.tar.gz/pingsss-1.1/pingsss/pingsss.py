# pingsss/pingsss.py
from colorama import init, Fore
import subprocess
import ipaddress
import argparse
import concurrent.futures
import json

# Initialize colorama
init()

def ping_host(host):
    """
    Ping a host and return True if it's reachable, False otherwise.
    """
    try:
        subprocess.check_output(['ping', '-c', '1', str(host)])
        return host, True
    except subprocess.CalledProcessError:
        return host, False

def parse_ip_range(ip_range):
    """
    Parse an IP range (e.g., 192.168.100.1-20) and return a list of IP addresses.
    """
    try:
        start_ip, end_ip = ip_range.split('-')
        start_ip = ipaddress.ip_address(start_ip)
        end_ip = ipaddress.ip_address(start_ip.packed[:3] + bytes([int(end_ip)]))

        return [ipaddress.ip_address(start_ip.packed[:3] + bytes([i])) for i in range(int(start_ip.packed[3]), int(end_ip.packed[3]) + 1)]
    except ValueError as e:
        raise ValueError(f"Invalid IP range: {e}")

def ping_hosts(ip_range, show='all', output=None):
    hosts = parse_ip_range(ip_range)
    results = {}
    with concurrent.futures.ThreadPoolExecutor(max_workers=100) as executor:
        futures = {executor.submit(ping_host, host): host for host in hosts}
        for future in concurrent.futures.as_completed(futures):
            host = futures[future]
            try:
                host, reachable = future.result()
                results[str(host)] = reachable
                if show == 'all' or (show == 'alive' and reachable) or (show == 'dead' and not reachable):
                    print(f"{Fore.GREEN if reachable else Fore.RED}Host {host} {'alive' if reachable else 'dead'}{Fore.RESET}")
            except Exception as e:
                print(f"Error pinging host {host}: {e}")

    if output == 'json':
        filename = 'output.json'
        i = 1
        while os.path.exists(filename):
            filename = f'output{i}.json'
            i += 1
        with open(filename, 'w') as f:
            json.dump(results, f)

    alive_count = sum(1 for result in results.values() if result)
    dead_count = len(results) - alive_count
    print(f"Finished: alive [{alive_count}] | dead [{dead_count}]")

def main():
    parser = argparse.ArgumentParser(description='Ping multiple hosts concurrently.')
    parser.add_argument('ip_range', help='IP range to ping (e.g., 192.168.100.1-20)')
    parser.add_argument('--show', choices=['all', 'alive', 'dead'], default='all', help='Show only alive or dead hosts')
    parser.add_argument('--output', choices=['json'], help='Save output to file in JSON format')
    args = parser.parse_args()
    ping_hosts(args.ip_range, args.show, args.output)

if __name__ == "__main__":
    main()
