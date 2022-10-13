import time

delay = time.sleep_ms(300)
yy = time.localtime()[0]
mm = time.localtime()[1]
dd = time.localtime()[2]
h = time.localtime()[3]
m = time.localtime()[4]
date = "{}/{}/{} - {}:{}".format(dd,mm,yy,h,m)
print(date)
