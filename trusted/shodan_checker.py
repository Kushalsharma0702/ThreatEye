import shodan
import sys

# Your Shodan API Key (Replace with your actual key)
SHODAN_API_KEY = "YOUR_SHODAN_API_KEY"
api = shodan.Shodan(SHODAN_API_KEY)

def check_vulnerabilities(ip):
    try:
        print(f"[+] Searching Shodan for {ip}...")
        result = api.host(ip)

        print("\n--- Device Information ---")
        print(f"IP: {result['ip_str']}")
        print(f"Organization: {result.get('org', 'N/A')}")
        print(f"Operating System: {result.get('os', 'N/A')}")
        
        print("\n--- Open Ports ---")
        for port in result['ports']:
            print(f"Port: {port}")
            
        print("\n--- Vulnerabilities (CVEs) ---")
        for item in result.get('vulns', {}):
            cve = item.replace('!', '')  # Remove '!' from CVEs
            print(f"CVE: {cve}")
            print(f"Summary: {result['vulns'][item].get('summary', 'No details')}\n")
            
    except shodan.APIError as e:
        print(f"[!] Error: {e}")

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python shodan_checker.py <IP>")
        sys.exit(1)
    
    target_ip = sys.argv[1]
    check_vulnerabilities(target_ip)
