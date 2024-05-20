import hmac
import hashlib

SECRET_CODE = "" # Secret key in string 
mac_addresses = [
    "00:80:E1:26:03:8E",
    "00:80:E1:26:8E:A8",
    "00:80:E1:26:A1:41",
    "00:80:E1:26:AA:72",
    "...",
    "...",
    "...",
]

def generate_pin(mac_address, SECRET_CODE):
    mac_bytes = bytes.fromhex(mac_address.replace(":", ""))
    hmac_object = hmac.new(SECRET_CODE.encode(), mac_bytes, hashlib.sha256)
    hmac_digest = hmac_object.digest()
    pin = int.from_bytes(hmac_digest[:4], 'little')
    pin %= 1000000
    return pin

def generate_pins(mac_addresses, SECRET_CODE):
    pins = {}
    for mac in mac_addresses:
        pins[mac] = generate_pin(mac, SECRET_CODE)
    return pins

if __name__ == "__main__":
    pins = generate_pins(mac_addresses, SECRET_CODE)
    for mac, pin in pins.items():
        print(f"The generated PIN for {mac} is: {pin}")
