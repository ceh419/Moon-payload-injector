import requests

def get_location(ip):
    try:
        response = requests.get(f"http://ip-api.com/json/{ip}")
        data = response.json()
        if data['status'] == 'success':
            print(f"[+] Country: {data['country']}")
            print(f"[+] City: {data['city']}")
            print(f"[+] ISP: {data['isp']}")
            print(f"[+] Latitude: {data['lat']}")
            print(f"[+] Longitude: {data['lon']}")
            print(f"[+] Timezone: {data['timezone']}")
            print(f"[+] Google Maps: https://www.google.com/maps?q={data['lat']},{data['lon']}")
        else:
            print("[-] Invalid IP or no data found.")
    except Exception as e:
        print(f"Error: {e}")

if __name__ == "__main__":
    ip = input("Enter IP: ")
    get_location(ip)
