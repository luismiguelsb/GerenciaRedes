# -*- coding: utf-8 -*-
from Tkinter import *
from easysnmp import Session
import datetime


# FUNCTIONS
def click_entrar():
    endereco = textentryEndereco.get()
    usuario = textentryUsuario.get()
    senha = textentrySenha.get()

    global session 
    session = Session(hostname=endereco, community='public', version=2, use_sprint_value = True)
    session = Session(hostname=endereco, version=3, security_level="auth_with_privacy",
         security_username=usuario, auth_protocol="MD5", auth_password=senha,privacy_protocol="DES", privacy_password=senha)


    textEndereco.insert(END, endereco)

    name = session.get('sysName.0').value
    textName.insert(END, name)

    uptime = session.get('sysUpTimeInstance').value
    textUptime.insert(END, uptime)

    countBulk = session.get_bulk(['ifOutOctets'], 0, 2)
    bytesOut = countBulk[1].value
    textBytesOut.insert(END, bytesOut)

    countBulk = session.get_bulk(['ifInOctets'], 0, 2)
    bytesIn = countBulk[1].value
    textBytesIn.insert(END, bytesIn)

    textentryEndereco.delete(0, END)
    textentryUsuario.delete(0, END)
    textentrySenha.delete(0, END)
    windowPrincipal.tkraise()

def click_sair():
    root.destroy()
    exit()

def click_fechar():
    textEndereco.delete(0.0,END)
    textName.delete(0.0,END)
    textUptime.delete(0.0,END)
    textBytesIn.delete(0.0,END)
    textBytesOut.delete(0.0,END)
    windowLogin.tkraise()
    

########## ROOT FRAME ----------------------------------------------------------------------------
root = Tk()
root.title("Gerência de Redes")
#root.geometry("600x400")
root.configure(background = "black")
#root.resizable(0,0)

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

#Label(windowLogin, bg="black").pack()   # label dummy para ocupar uma linha (tipo \n)

# BOTAO (ENTRAR)
Button(windowLogin, text="ENTRAR", width=6, command=click_entrar).pack(padx=10, pady=10)

Label(windowLogin, bg="black", width="50").pack()   # label dummy para ocupar uma linha (tipo \n)

# BOTAO (SAIR)
Button(windowLogin, text="SAIR", width="6", command=click_sair).pack(padx=5, pady=5, side=RIGHT)

##########
########## WINDOW PRINCIPAL ----------------------------------------------------------------------------
##########

Label(windowPrincipal, text = "Gerenciamento de Desempenho", bg="black", fg="white", font="none 20 bold").pack(pady=10, padx=20)

Label(windowPrincipal, text = "Endereço:", bg="black", fg="white", font="none 14 bold").pack(pady=10)
textEndereco = Text(windowPrincipal, width=30, height=1, wrap=WORD, background="white", font="none 12")
textEndereco.pack(padx=10)

Label(windowPrincipal, text = "Nome:", bg="black", fg="white", font="none 14 bold").pack(pady=10)
textName = Text(windowPrincipal, width=30, height=1, wrap=WORD, background="white", font="none 12")
textName.pack(padx=10)

Label(windowPrincipal, text = "Uptime:", bg="black", fg="white", font="none 14 bold").pack(pady=10)
textUptime = Text(windowPrincipal, width=30, height=1, wrap=WORD, background="white", font="none 12")
textUptime.pack(padx=10)

Label(windowPrincipal, text = "Bytes Enviados:", bg="black", fg="white", font="none 14 bold").pack(pady=10)
textBytesOut = Text(windowPrincipal, width=30, height=1, wrap=WORD, background="white", font="none 12")
textBytesOut.pack(padx=10)

Label(windowPrincipal, text = "Bytes Recebidos:", bg="black", fg="white", font="none 14 bold").pack(pady=10)
textBytesIn = Text(windowPrincipal, width=30, height=1, wrap=WORD, background="white", font="none 12")
textBytesIn.pack(padx=10)

# BOTAO (FECHAR SESSAO)
Button(windowPrincipal, text="FECHAR SESSÃO", width="12", command=click_fechar).pack(pady=10)


###################### -------------------------------------------------------------------------------

windowLogin.tkraise()
### MAIN LOOP
root.mainloop()