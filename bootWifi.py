import network

def connect(ssid, password):
    wlan = network.WLAN(network.STA_IF)
    wlan.active(True)
    if not wlan.isconnected():
        print('connecting ...')
        wlan.connect(ssid, password)
        while not wlan.isconnected():
            pass
    return wlan.ifconfig()

#('192.168.8.111', '255.255.255.0', '192.168.8.1', '192.168.8.1')

if __name__ == "__main__":
    ssid = 'DESKKTOP-5TKR1V4'
    password = "it'spassword"
    print(connect(ssid, password))
    