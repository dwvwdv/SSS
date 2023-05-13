import requests
import clipboard

ip = requests.get('https://api.ipify.org').content.decode('utf8')
print(f'My public IP address is: {ip}')
clipboard.copy(ip)
