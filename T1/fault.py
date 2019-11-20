from easysnmp import Session
import time

session = Session(hostname="192.168.0.105",version=3,security_level="auth_with_privacy",security_username="MD5DESUser",auth_protocol="MD5",auth_password="snmpehvida",privacy_protocol="DES",privacy_password="snmpehvida")


while 1:
	blockedSite = 0
	openTcpConnections =int(session.get('tcpCurrEstab.0').value) + 2
	tcpConnections = session.get_bulk(['tcpConnState'],0,openTcpConnections)


#print tcpConnections[0]
	for i in range(openTcpConnections):
		result = tcpConnections[i].oid_index.find('143.54.2.20')
		if result != -1:
			blockedSite = 1;
#print tcpConnections

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
	
	if(blockedSite):
		print "ATENCAO!!!!!!!!!!!!!!!!!!!!!!!!!"
		print "Site indevido acessado!"
