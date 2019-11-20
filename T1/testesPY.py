from easysnmp import Session
import datetime

session = Session(hostname='192.168.15.10', community='public', version=2, use_sprint_value = True)

# UPTIME
uptime = session.get('sysUpTimeInstance')
print("Uptime = " + uptime.value + "\n")

# NOME
name = session.get('sysName.0')
print("Name = " + name.value + "\n")

# NUM INTERFACES
interfaces = session.get('ifNumber.0')
print("Interfaces = " + interfaces.value + "\n")
numInterfaces = int(interfaces.value)

# MACs
print("\nMACs:")
endMAC = []
countBulk = session.get_bulk(['ifPhysAddress'], 0, numInterfaces)
for i in range(numInterfaces):
    endMAC.append(countBulk[i])
    print (endMAC[i].value)

# IPs
print("\nIPs:")
endIP = []
countBulk = session.get_bulk(['ipAdEntAddr'], 0, numInterfaces)
for i in range(numInterfaces):
    endIP.append(countBulk[i])
    print (endIP[i].value)

# BYTES ENVIADOS
print("\nBytes Enviados:")
bytesOut = []
countBulk = session.get_bulk(['ifOutOctets'], 0, numInterfaces)
for i in range(numInterfaces):
    bytesOut.append(countBulk[i])
    print (bytesOut[i].value)

# BYTES RECEBIDOS
print("\nBytes Recebidos:")
bytesIn = []
countBulk = session.get_bulk(['ifInOctets'], 0, numInterfaces)
for i in range(numInterfaces):
    bytesIn.append(countBulk[i])
    print (bytesIn[i].value)

# PACOTES ENVIADOS
print("\nPacotes Enviados:")
pacotesOut = []
countBulk = session.get_bulk(['ifOutUcastPkts'], 0, numInterfaces)
countBulkAux = session.get_bulk(['ifOutNUcastPkts'], 0, numInterfaces)
for i in range(numInterfaces):
    pacotesUniOut = countBulk[i]
    pacotesNaoUniOut = countBulkAux[i]
    pacotesOut.append(pacotesUniOut.value + pacotesNaoUniOut.value)
    print (pacotesOut[i])

# PACOTES RECEBIDOS
print("\nPacotes Recebidos:")
pacotesIn = []
countBulk = session.get_bulk(['ifInUcastPkts'], 0, numInterfaces)
countBulkAux = session.get_bulk(['ifInNUcastPkts'], 0, numInterfaces)
for i in range(numInterfaces):
    pacotesUniIn = countBulk[i]
    pacotesNaoUniIn = countBulkAux[i]
    pacotesIn.append(pacotesUniIn.value + pacotesNaoUniIn.value)
    print (pacotesIn[i])

# PACOTES RECEBIDOS COM ERROS
print("\nPacotes Recebidos com Erros:")
pacotesErroIn = []
countBulk = session.get_bulk(['ifInErrors'], 0, numInterfaces)
for i in range(numInterfaces):
    pacotesErroIn.append(countBulk[i])
    print (pacotesErroIn[i].value)

# PACOTES ENVIADOS COM ERROS
print("\nPacotes Enviados com Erros:")
pacotesErroOut = []
countBulk = session.get_bulk(['ifOutErrors'], 0, numInterfaces)
for i in range(numInterfaces):
    pacotesErroOut.append(countBulk[i])
    print (pacotesErroOut[i].value)

# PORCENTAGEM DE ERRO NA ENTRADA
print("\nPorcentagem de Erro na Entrada:")
porcentagemErroIn = []
for i in range(numInterfaces):
    porcentagemErroIn.append(int(pacotesErroIn[i].value)/int(pacotesIn[i]))
    print(porcentagemErroIn[i])

# PORCENTAGEM DE ERRO NA SAIDA
print("\nPorcentagem de Erro na Saida:")
porcentagemErroOut = []
for i in range(numInterfaces):
    porcentagemErroOut.append(int(pacotesErroOut[i].value)/int(pacotesOut[i]))
    print(porcentagemErroOut[i])

# PACOTES RECEBIDOS DESCARTADOS
print("\nPacotes Recebidos Descartados:")
pacotesDescIn = []
countBulk = session.get_bulk(['ifInDiscards'], 0, numInterfaces)
for i in range(numInterfaces):
    pacotesDescIn.append(countBulk[i])
    print (pacotesDescIn[i].value)

# PACOTES ENVIADOS DESCARTADOS
print("\nPacotes Enviados Descartados:")
pacotesDescOut = []
countBulk = session.get_bulk(['ifOutDiscards'], 0, numInterfaces)
for i in range(numInterfaces):
    pacotesDescOut.append(countBulk[i])
    print (pacotesDescOut[i].value)

# PORCENTAGEM DE DESCARTE NA ENTRADA
print("\nPorcentagem de Descarte na Entrada:")
porcentagemDescIn = []
for i in range(numInterfaces):
    porcentagemDescIn.append(int(pacotesDescIn[i].value)/int(pacotesIn[i]))
    print(porcentagemDescIn[i])

# PORCENTAGEM DE DESCARTE NA SAIDA
print("\nPorcentagem de Descarte na Saida:")
porcentagemDescOut = []
for i in range(numInterfaces):
    porcentagemDescOut.append(int(pacotesDescOut[i].value)/int(pacotesOut[i]))
    print(porcentagemDescOut[i])

# BANDA TOTAL
print("\nBanda Total:")
bandaTotal = []
countBulk = session.get_bulk(['ifSpeed'], 0, numInterfaces)
for i in range(numInterfaces):
    bandaTotal.append(countBulk[i])
    print (bandaTotal[i].value)

# BANDA UTILIZADA
#print("\nBanda Utilizada:")
#bandaUtil = []
#for i in range(numInterfaces):
#    bandaUtil.append(       )
#    print (bandaUtil[i].value)

