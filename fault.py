from easysnmp import Session
import time

session = Session(hostname="192.168.0.105",version=3,security_level="auth_with_privacy",security_username="MD5DESUser",auth_protocol="MD5",auth_password="snmpehvida",privacy_protocol="DES",privacy_password="snmpehvida")


while(1):
	inputErrors = session.get('ifInErrors.1')
	inputUnicastPackets = session.get('ifInUcastPkts.1')
	inputNoUnicastPackets = session.get('ifInNUcastPkts.1')


	inputErrorPercentage = int(inputErrors.value) / (int(inputUnicastPackets.value) + int(inputNoUnicastPackets.value))

	print "Input error percentage = " +  str(inputErrorPercentage)


	outputErrors = session.get('ifOutErrors.1')
	outputUnicastPackets = session.get('ifOutUcastPkts.1')
	outputNoUnicastPackets = session.get('ifOutNUcastPkts.1')	

	print "Output error percentage = " + str(outputErrors.value)	
	
	time.sleep(1)
