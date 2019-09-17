from easysnmp import Session
import time




session = Session(hostname='localhost',version=3,security_level="auth_with_privacy",security_username="MD5DESUser",auth_protocol="MD5", auth_password="snmpehvida",privacy_protocol="DES", privacy_password="snmpehvida")


while True:
    IfInOctets1 = int(session.get('ifInOctets.1').value)
    IfOutOctets1 = int(session.get('ifOutOctets.1').value)

    time.sleep(5)

    IfInOctets2 = int(session.get('ifInOctets.1').value)
    IfOutOctets2 = int(session.get('ifOutOctets.1').value)

    print 'Bits IN/sec:', (IfInOctets2 - IfInOctets1)/5
    print 'Bits OUT/sec:', (IfOutOctets2 - IfOutOctets1)/5
