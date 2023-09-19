import hmac
import hashlib

SECRET_CODE = "*****" # Secret key in string 
mac_address = "00:80:E1:26:AA:72" # Mac address in format: 00:80:E1:26:AA:72 (big letters :))


def generate_pin(mac_address, SECRET_CODE):
    mac_bytes = bytes.fromhex(mac_address.replace(":", ""))
    hmac_object = hmac.new(SECRET_CODE.encode(), mac_bytes, hashlib.sha256)
    hmac_digest = hmac_object.digest()
    pin = int.from_bytes(hmac_digest[:4], 'little')
    pin %= 1000000
    return pin
    

if __name__ == "__main__":
    pin = generate_pin(mac_address, SECRET_CODE)
    print(f"The generated PINs is: {pin}")

