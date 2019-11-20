from easysnmp import Session
import time

session = Session(hostname='localhost',version=3,security_level="auth_with_privacy",security_username="MD5DESUser",auth_protocol="MD5", auth_password="snmpehvida",privacy_protocol="DES", privacy_password="snmpehvida")


ifNumber = session.get('ifNumber.0')
numberInterfaces = int(ifNumber.value)

valueIN1 = {}
valueIN2 = {}
valueOUT1 = {}
valueOUT2 = {}
IN_BitsPerSec = {}
OUT_BitsPerSec = {}
Sum_IN = 0
Sum_OUT = 0
MAX_IN = int(input('Insert max UPLOAD band: '))
MAX_OUT = int(input('Insert max DOWNLOAD band: '))

print('Numero de interfaces:' + ifNumber.value)

while ((Sum_IN < MAX_IN) or (Sum_OUT < MAX_OUT)):
    Bulk = session.get_bulk(['ifInOctets', 'ifOutOctets'], 0, numberInterfaces)
    time.sleep(5)
    Bulk2 = session.get_bulk(['ifInOctets', 'ifOutOctets'], 0, numberInterfaces)

    for i in range(numberInterfaces):
        ifInOctets1 = Bulk[i]
        ifOutOctets1 = Bulk[i+1]

        ifInOctets2 = Bulk2[i]
        ifOutOctets2 = Bulk2[i+1]

        valueIN1[i] = int(ifInOctets1.value)
        valueOUT1[i] = int(ifOutOctets1.value)
        valueIN2[i] = int(ifInOctets2.value)
        valueOUT2[i] = int(ifOutOctets2.value)

        IN_BitsPerSec[i] = (valueIN2[i] - valueIN1[i]) / 5
        OUT_BitsPerSec[i] = (valueOUT2[i] - valueOUT1[i]) / 5

        print "Interface:", i
        print "Taxa de entrada ", IN_BitsPerSec[i], "bits/s"
        print "Taxa de saida ", OUT_BitsPerSec[i], "bits/s"

        Sum_IN = Sum_IN + valueIN2[i] - valueIN1[i]
        Sum_OUT = Sum_OUT + valueOUT2[i] - valueOUT1[i]

if(Sum_IN >= MAX_IN):
	print "Maximum UPLOAD consumption"
else:
	print "Maximum DOWNLOAD consumption"
