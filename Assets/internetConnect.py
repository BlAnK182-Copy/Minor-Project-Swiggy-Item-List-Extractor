import os

try:
    import requests
except ModuleNotFoundError:
    os.system("pip install requests")
    import requests


class Connect:
    def __init__(self) -> None:
        self.timeout = 5
    def connected(self):
        try:
            r = requests.get("https://www.google.com", timeout = self.timeout)
            return True 
        except (requests.ConnectionError, requests.Timeout):
            return False 