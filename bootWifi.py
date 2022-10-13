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
    ssid = 'HUAWEI_B612_DAA8'
    password = '69AB3AQHJ6E'
    print(connect(ssid, password))
    