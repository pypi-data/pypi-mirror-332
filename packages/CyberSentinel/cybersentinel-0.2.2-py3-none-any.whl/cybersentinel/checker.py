import requests
import socket
import ssl
import time
import sys
from cybersentinel.malware_check import check_malware

# Google Safe Browsing API Key
API_KEY = "AIzaSyDtgCMpZdOCDWCUIkAzB41w-7MwA9iI3Vs"

def check_website_status(url):
    """Check if the website is online and measure response time."""
    try:
        start_time = time.time()
        response = requests.get(url, timeout=5)
        response_time = round((time.time() - start_time) * 1000, 2)  # in ms
        return response.status_code == 200, response_time
    except requests.exceptions.RequestException:
        return False, None

def check_ssl_certificate(url):
    """Check if the website has a valid SSL certificate."""
    try:
        hostname = url.split("//")[-1].split("/")[0]  # Extract hostname
        context = ssl.create_default_context()
        with socket.create_connection((hostname, 443), timeout=5) as sock:
            with context.wrap_socket(sock, server_hostname=hostname) as ssock:
                return True  # SSL is valid if no exception occurs
    except Exception:
        return False

def run_security_checks(url):
    """Run all security checks on the given URL."""
    print("\nChecking website status...")
    is_online, response_time = check_website_status(url)
    if is_online:
        print(f"✅ Website {url} is ONLINE")
        print(f"⏳ Response Time: {response_time}ms")
    else:
        print(f"❌ Website {url} is OFFLINE")
        return
    
    print("\nChecking SSL certificate...")
    if check_ssl_certificate(url):
        print("🔒 SSL Certificate: VALID")
    else:
        print("🚨 SSL Certificate: INVALID or MISSING")
    
    print("\nChecking for malware and phishing threats...")
    try:
        is_malicious = check_malware(url, API_KEY)
        if is_malicious:
            print("⚠️ WARNING: The website is flagged as MALICIOUS!")
        else:
            print("✅ The website is SAFE.")
    except Exception as e:
        print(f"❌ Error checking malware: {e}")

def main():
    """Main function to handle command-line and interactive execution."""
    if len(sys.argv) > 1:
        url = sys.argv[1]  # Take URL from command-line argument
    else:
        url = input("Enter website URL (including https:// or http://): ").strip()

    if not url.startswith(("http://", "https://")):
        print("❌ Invalid URL format! Please include http:// or https://")
        return

    run_security_checks(url)

if __name__ == "__main__":
    main()
