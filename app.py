import argparse
import os
import json

### --- ### --- ### --- ### --- ### --- ### --- ### --- ### --- ### --- ### --- ### --- ###

try:
    from ipwhois import IPWhois
    from ipwhois.exceptions import IPDefinedError
except ImportError:
    print("Please install ipwhois first: pip install ipwhois")
    exit(1)

### --- ### --- ### --- ### --- ### --- ### --- ### --- ### --- ### --- ### --- ### --- ###

def main():
    try:
        parser = argparse.ArgumentParser()
        parser.add_argument('--user_input', required=True, help='IP Address to Get Whois Information For')
        args = parser.parse_args()

        ip_address = args.user_input
        # ip_address = "8.8.8.8"  # Example IP address (Google's Public DNS)
        # # ip_address = "192.168.1.1" # Example of a private IP

        # Create an IPWhois object for the IP address
        obj = IPWhois(ip_address)

        # Perform the lookup. lookup_rdap() is preferred as it uses the newer
        # RDAP protocol (JSON based). Use depth=1 to get info for the immediate network.
        # Use lookup_whois() for the legacy WHOIS protocol (text-based).
        # print(f"--- Performing RDAP lookup for {ip_address} ---")
        results_rdap = obj.lookup_rdap(depth=1)

        # Print the results (often a nested dictionary)
        # Using json.dumps for pretty printing
        print(json.dumps(results_rdap, indent=4))

        # --- Optional: Legacy WHOIS lookup ---
        # print(f"\n--- Performing Legacy WHOIS lookup for {ip_address} ---")
        # results_whois = obj.lookup_whois()
        # print(json.dumps(results_whois, indent=4))
        # Note: Legacy WHOIS often returns less structured data or just raw text in 'raw' key

        return 0
    except IPDefinedError:
        print(f"[!] Error: {ip_address} is a private, loopback, or reserved IP address.")
    except Exception as e:
        print(f"[!] Error: {str(e)}")
        return 1

### --- ### --- ### --- ### --- ### --- ### --- ### --- ### --- ### --- ### --- ### --- ###

if __name__ == "__main__":
    exit(main())
