#!/usr/bin/env python3

import requests
from concurrent.futures import ThreadPoolExecutor

banner = r'''
██████╗ ███████╗██████╗ ██████╗ ██╗   ██╗████████╗██╗  ██╗ ██████╗ ███╗   ██╗
██╔══██╗██╔════╝██╔══██╗██╔══██╗╚██╗ ██╔╝╚══██╔══╝██║  ██║██╔═══██╗████╗  ██║
██████╔╝█████╗  ██║  ██║██████╔╝ ╚████╔╝    ██║   ███████║██║   ██║██╔██╗ ██║
██╔══██╗██╔══╝  ██║  ██║██╔═══╝   ╚██╔╝     ██║   ██╔══██║██║   ██║██║╚██╗██║
██║  ██║███████╗██████╔╝██║        ██║      ██║   ██║  ██║╚██████╔╝██║ ╚████║
╚═╝  ╚═╝╚══════╝╚═════╝ ╚═╝        ╚═╝      ╚═╝   ╚═╝  ╚═╝ ╚═════╝ ╚═╝  ╚804╝                                                                          
'''

print(banner)
def is_proxy_working(proxy):
    proxies = {
        'http': f'http://{proxy}',
        'https': f'http://{proxy}',  # Assumes HTTP for both
    }
    try:
        r = requests.get('http://httpbin.org/ip', proxies=proxies, timeout=5)
        return r.status_code == 200
    except:
        return False

def check_proxies(proxy_list, output_file, threads=20):
    with ThreadPoolExecutor(max_workers=threads) as executor:
        futures = {executor.submit(is_proxy_working, p): p for p in proxy_list}
        with open(output_file, 'w') as f:
            for future in futures:
                proxy = futures[future]
                try:
                    if future.result():
                        print(f'[+] Working: {proxy}')
                        f.write(proxy + '\n')
                    else:
                        print(f'[-] Dead: {proxy}')
                except Exception as e:
                    print(f'[!] Error with {proxy}: {e}')

if __name__ == '__main__':
    import argparse
    parser = argparse.ArgumentParser(description='Check and whitelist working proxies.')
    parser.add_argument('--input', default='path/proxy.txt', help='Input file with proxies')
    parser.add_argument('--output', default='saveoutput.txt', help='Output file for working proxies')
    args = parser.parse_args()

    with open(args.input, 'r') as f:
        proxies = [line.strip() for line in f if line.strip()]

    check_proxies(proxies, args.output)
