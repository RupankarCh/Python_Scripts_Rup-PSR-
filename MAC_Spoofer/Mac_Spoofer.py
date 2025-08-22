#!/usr/bin/env python3

import subprocess
import argparse

def get_arguments():
    parser = argparse.ArgumentParser(description="Change MAC Address of a network interface.")
    parser.add_argument("-i", "--interface", dest="interface", required=True, help="Interface to change it's MAC Address")
    parser.add_argument("-m", "--mac", dest="new_mac", required=True, help="New MAC Address")
    options = parser.parse_args()

    if not options.interface:
        parser.error("[-] Pleae specify an interface, use --help for more info.")
    elif not options.new_mac:
        parser.error("[-] Pleae specify a new  MAC address, use --help for more info.")

    return options

def MAC_Spoofer(interface, new_mac):
    print(f"[+] Changing value for {interface} to {new_mac}")

    subprocess.call(["ifconfig", interface, "down"])
    subprocess.call(["ifconfig", interface, "hw", "ether", new_mac])
    subprocess.call(["ifconfig", interface, "up"])


args = get_arguments()
MAC_Spoofer(args.interface, args.new_mac)