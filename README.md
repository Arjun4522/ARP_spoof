# ARP Spoofing Tool

This is an ARP spoofing tool implemented in Python using the Scapy library. This script is capable of poisoning the arp cache of the target machine, which can lead to Man-in-the-Middle(MiTM) attacks.

## Prerequisites

Before using this tool, make sure you have the following requirements:

- Python 3.x
- Scapy library

You can install the Scapy library by running the following command:

`pip3 install scapy`

## Usage

In the code section, Modify the `target_ip` and `gateway_ip` variables in the file to specify the IP addresses of the target machine and the gateway/router.

`target_ip = "10.0.0.8"  # IP of the target machine
gateway_ip = "10.0.0.1"  # IP of the gateway/router`


Run the script with `python3 arp_spoofing.py`

## Output

Notice physical/MAC address of the gateway before running the script,

![before](https://github.com/Arjun4522/ARP_spoof/assets/94633408/cf125634-33ef-43f0-864a-ee503eaf0c56)

and after running the script

![after](https://github.com/Arjun4522/ARP_spoof/assets/94633408/205c572f-32a2-4b47-b3d1-7da0deac24e0)

One can see, the gateway's MAC address(10-da-43-35-1e-79) has been modified to attacker's MAC address(08-00-27-53-0c-ba).

## Disclaimer

The author of this tool is not responsible for any unauthorized use or potential damage caused by the misuse of this tool. Use at your own risk.
