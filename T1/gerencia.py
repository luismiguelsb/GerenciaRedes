# -*- coding: utf-8 -*-
from Tkinter import *
import ttk
import tkMessageBox
from easysnmp import Session
import datetime


# FUNCTIONS
def checkSites():
    blockedSite = 0
    openTcpConnections =int(session.get('tcpCurrEstab.0').value) + 2
    tcpConnections = session.get_bulk(['tcpConnState'],0,openTcpConnections)
    for i in range(openTcpConnections):
    	result = tcpConnections[i].oid_index.find('201.54.140.10')
	if result != -1:
	    blockedSite = 1
    if blockedSite == 1:
        tkMessageBox.showinfo("Aviso", "Acesso indevido ao site 201.54.140.10")
    root.after(1000, checkSites)


def updateTime():
    uptime = session.get('sysUpTimeInstance').value
    textUptime.config(state=NORMAL)
    textUptime.delete(0.0, END)
    textUptime.insert(END, uptime)
    textUptime.config(state=DISABLED)
    root.after(1000, updateTime)

def updateBytes():
    countBulk = session.get_bulk(['ifOutOctets'], 0, 2)
    global bytesOut
    bytesOut = countBulk[1].value
    textBytesOut.config(state=NORMAL)
    textBytesOut.delete(0.0, END)
    textBytesOut.insert(END, bytesOut)
    textBytesOut.config(state=DISABLED)

    countBulk = session.get_bulk(['ifInOctets'], 0, 2)
    global bytesIn
    bytesIn = countBulk[1].value
    textBytesIn.config(state=NORMAL)
    textBytesIn.delete(0.0, END)
    textBytesIn.insert(END, bytesIn)
    textBytesIn.config(state=DISABLED)
    root.after(1000, updateBytes)

def click_entrar():
    endereco = textentryEndereco.get()
    usuario = textentryUsuario.get()
    senha = textentrySenha.get()

    try:
	    global session
	    #session = Session(hostname=endereco, community='public', version=2, use_sprint_value = True)
	    session = Session(hostname=endereco, version=3, security_level="auth_with_privacy", security_username=usuario, auth_protocol=str(tipoAuth.get()), auth_password=senha,privacy_protocol=str(tipoCript.get()), privacy_password=senha, use_sprint_value = True)

            print(str(tipoAuth.get()))
            print(str(tipoCript.get()))

    	    textEndereco.insert(END, endereco)
            textEndereco.config(state=DISABLED)

	    name = session.get('sysName.0').value
	    textName.insert(END, name)
            textName.config(state=DISABLED)

            updateTime()

	    updateBytes()

            checkSites()

	    labelErro.config(text="")
	    textentryEndereco.delete(0, END)
	    textentryUsuario.delete(0, END)
	    textentrySenha.delete(0, END)
	    windowPrincipal.tkraise()

    except:
	labelErro.config(text="Não foi possível abrir a sessão!")

def click_ConfigTaxas():
    global topWindowConfigTaxas
    topWindowConfigTaxas = Toplevel()
    topWindowConfigTaxas.configure(background="black")
    
    # TEXTO (UPLOAD)
    Label(topWindowConfigTaxas, text = "Taxa Upload:", bg="black", fg="white", font="none 14 bold").pack(pady=10)
    global taxaentryUpload
    taxaentryUpload = Entry(topWindowConfigTaxas, width=30, bg="white", font="none 12")
    taxaentryUpload.pack(padx=10, pady=10)

    # TEXTO (DOWNLOAD)
    Label(topWindowConfigTaxas, text = "Taxa Download:", bg="black", fg="white", font="none 14 bold").pack(pady=10)
    global taxaentryDownload
    taxaentryDownload = Entry(topWindowConfigTaxas, width=30, bg="white", font="none 12")
    taxaentryDownload.pack(padx=10, pady=10)

    Button(topWindowConfigTaxas, text="Atualizar taxas", width="20", command=click_AttTaxas).pack(pady=10)

    Label(topWindowConfigTaxas, text = "%download:", bg="black", fg="white", font="none 14 bold").pack(pady=10)
    global varBarraIn
    varBarraIn = DoubleVar()
    varBarraIn.set(0)
    global minhaBarraIn
    minhaBarraIn = ttk.Progressbar(topWindowConfigTaxas, style="red.Horizontal.TProgressbar", variable=varBarraIn, maximum=0, length=300) 
    minhaBarraIn.pack(pady=10)

    Label(topWindowConfigTaxas, text = "%upload:", bg="black", fg="white", font="none 14 bold").pack(pady=10)
    global varBarraOut
    varBarraOut = DoubleVar()
    varBarraOut.set(0)
    global minhaBarraOut
    minhaBarraOut = ttk.Progressbar(topWindowConfigTaxas, style="red.Horizontal.TProgressbar",variable=varBarraOut, maximum=0, length=300) 
    minhaBarraOut.pack(pady=10)

def click_AttTaxas():
    MAX_IN = taxaentryDownload.get()
    MAX_OUT = taxaentryUpload.get() 
    
    minhaBarraIn['maximum'] = MAX_IN
    minhaBarraOut['maximum'] = MAX_OUT

    countBulk = session.get_bulk(['ifOutOctets'], 0, 2)
    global bytesOutInicial
    bytesOutInicial = countBulk[1].value

    countBulk = session.get_bulk(['ifInOctets'], 0, 2)
    global bytesInInicial
    bytesInInicial = countBulk[1].value
    
    updateTaxas()

def updateTaxas():
    progressoBarraIn = int(bytesIn) - int(bytesInInicial)
    progressoBarraOut = int(bytesOut) - int(bytesOutInicial)
    varBarraIn.set(progressoBarraIn)
    varBarraOut.set(progressoBarraOut)
    root.after(1000, updateTaxas)


def click_taxaErros():
    topWindowErros = Toplevel()
    topWindowErros.configure(background="black")
    
    # TEXTO (ERRO IN)
    Label(topWindowErros, text = "Erro IN:", bg="black", fg="white", font="none 14 bold").pack(pady=10)
    global textErroIn
    textErroIn = Text(topWindowErros, width=30, height=1, wrap=WORD, background="white", font="none 12")
    textErroIn.insert(END,"teste")
    textErroIn.pack(padx=10, pady=10)

    # TEXTO (ERRO OUT)
    Label(topWindowErros, text = "Erro OUT:", bg="black", fg="white", font="none 14 bold").pack(pady=10)
    global textErroOut
    textErroOut = Text(topWindowErros, width=30, height=1, wrap=WORD, background="white", font="none 12")
    textErroOut.pack(padx=10, pady=10)

    updateTaxaErros()

    topWindowErros.mainloop()

def updateTaxaErros():
    inputErrors = session.get('ifInErrors.1')
    inputUnicastPackets = session.get('ifInUcastPkts.1')
    inputNoUnicastPackets = session.get('ifInNUcastPkts.1')
    inputErrorPercentage = int(inputErrors.value) / (int(inputUnicastPackets.value) + int(inputNoUnicastPackets.value))

    #print "Input error percentage = " +  str(inputErrorPercentage)
    textErroIn.config(state=NORMAL)
    textErroIn.delete(0.0, END)
    textErroIn.insert(END, inputErrorPercentage)
    textErroIn.config(state=DISABLED)

    outputErrors = session.get('ifOutErrors.1')
    outputUnicastPackets = session.get('ifOutUcastPkts.1')
    outputNoUnicastPackets = session.get('ifOutNUcastPkts.1')	

    outputErrorPercentage = int(outputErrors.value) / (int(outputUnicastPackets.value) + int(outputNoUnicastPackets.value))

    #print "Output error percentage = " + str(outputErrors.value)
    textErroOut.config(state=NORMAL)
    textErroOut.delete(0.0, END)
    textErroOut.insert(END, outputErrorPercentage)
    textErroOut.config(state=DISABLED)

    root.after(1000, updateTaxaErros)
    

def click_sair():
    root.destroy()
    exit()

#def click_fechar():
    #session.close()
 #   session = None
  #  windowLogin.tkraise()
    

########## ROOT FRAME ----------------------------------------------------------------------------
root = Tk()
root.title("Gerência de Redes")
#root.geometry("600x400")
root.configure(background = "black")
root.resizable(0,0)

windowLogin = Frame(root)
windowLogin.configure(background = "black")
windowPrincipal = Frame(root)
windowPrincipal.configure(background = "black")

windowLogin.grid(row=0, column=0, sticky='nsew')
windowPrincipal.grid(row=0, column=0, sticky='nsew')

##########
########## WINDOW LOGIN ----------------------------------------------------------------------------
##########

# ENTRADA (ENDERECO)
Label(windowLogin, text = "Endereço do Agente SNMP:", bg="black", fg="white", font="none 14 bold").pack(pady=10)
textentryEndereco = Entry(windowLogin, width=30, bg="white", font="none 12")
textentryEndereco.pack(padx=20)

# ENTRADA (USUARIO)
Label(windowLogin, text = "Usuário:", bg="black", fg="white", font="none 14 bold").pack(pady=10)
textentryUsuario = Entry(windowLogin, width=30, bg="white", font="none 12")
textentryUsuario.pack(padx=20)

# ENTRADA (SENHA)
Label(windowLogin, text = "Senha:", bg="black", fg="white", font="none 14 bold").pack(pady=10)
textentrySenha = Entry(windowLogin, show="*", width=30, bg="white", font="none 12")
textentrySenha.pack(padx=20)

Label(windowLogin, text = "Autenticação:", bg="black", fg="white", font="none 14 bold").pack(pady=10)
tipoAuth = StringVar()
tipoAuth.set("MD5")
Radiobutton(windowLogin, text="MD5", variable=tipoAuth, value="MD5", background="black", fg="white", selectcolor="black").pack()
Radiobutton(windowLogin, text="SHA", variable=tipoAuth, value="SHA", background="black", fg="white", selectcolor="black").pack()

Label(windowLogin, text = "Criptografia:", bg="black", fg="white", font="none 14 bold").pack(pady=10)
tipoCript = StringVar()
tipoCript.set("DES")
Radiobutton(windowLogin, text="DES", variable=tipoCript, value="DES", background="black", fg="white", selectcolor="black").pack()
Radiobutton(windowLogin, text="AES", variable=tipoCript, value="AES", background="black", fg="white", selectcolor="black").pack()

# BOTAO (ENTRAR)
Button(windowLogin, text="ENTRAR", width=6, command=click_entrar).pack(padx=10, pady=10)

labelErro = Label(windowLogin, bg="black", fg="white", font="none 14 bold", width="50")
labelErro.pack(pady=10)

# BOTAO (SAIR)
Button(windowLogin, text="SAIR", width="6", command=click_sair).pack(padx=5, pady=5, side=RIGHT)

##########
########## WINDOW PRINCIPAL ----------------------------------------------------------------------------
##########

# TITULO
Label(windowPrincipal, text = "Gerenciamento de Desempenho", bg="black", fg="white", font="none 20 bold").pack(pady=5, padx=20)

# TEXTO (ENDERECO)
Label(windowPrincipal, text = "Endereço:", bg="black", fg="white", font="none 14 bold").pack(pady=5)
textEndereco = Text(windowPrincipal, width=30, height=1, wrap=WORD, background="white", font="none 12")
textEndereco.pack(padx=10)

# TEXTO (NOME)
Label(windowPrincipal, text = "Nome:", bg="black", fg="white", font="none 14 bold").pack(pady=5)
textName = Text(windowPrincipal, width=30, height=1, wrap=WORD, background="white", font="none 12")
textName.pack(padx=10)

# TEXTO (UPTIME)
Label(windowPrincipal, text = "Uptime:", bg="black", fg="white", font="none 14 bold").pack(pady=5)
textUptime = Text(windowPrincipal, width=30, height=1, wrap=WORD, background="white", font="none 12")
textUptime.pack(padx=10)

# TEXTO (BYTES OUT)
Label(windowPrincipal, text = "Bytes Enviados:", bg="black", fg="white", font="none 14 bold").pack(pady=5)
textBytesOut = Text(windowPrincipal, width=30, height=1, wrap=WORD, background="white", font="none 12")
textBytesOut.pack(padx=10)

# TEXTO (BYTES IN)
Label(windowPrincipal, text = "Bytes Recebidos:", bg="black", fg="white", font="none 14 bold").pack(pady=5)
textBytesIn = Text(windowPrincipal, width=30, height=1, wrap=WORD, background="white", font="none 12")
textBytesIn.pack(padx=10)

# BOTAO (TAXA DE ERROS)
Button(windowPrincipal, text="TAXA DE ERROS", width="12", command=click_taxaErros).pack(pady=10)

# BOTAO (SETAR BANDA DOWNLOAD/UPLOAD)
Button(windowPrincipal, text="CONFIGURAR TAXA UP/DOWN", width="25", command=click_ConfigTaxas).pack(pady=10)


# BOTAO (FECHAR SESSAO)
Button(windowPrincipal, text="FECHAR", width="12", command=click_sair).pack(pady=10)


###################### -------------------------------------------------------------------------------

windowLogin.tkraise()
### MAIN LOOP
root.mainloop()
