from Assets import GUI
from Assets import internetConnect as ic

if __name__ == "__main__":
    connector = ic.Connect()
    isConnected = connector.connected()
    if isConnected:
        print("Connected to the internet")
        g = GUI.GUI()
    else:
        print("Check your internet connection and relaunch.")