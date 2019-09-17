# -*- coding: utf-8 -*-
from tkinter import *
from easysnmp import Session
import datetime


# FUNCTIONS
def click_entrar():
    endereco = textentryEndereco.get

    global session 
    session = Session(hostname=endereco, community='public', version=2, use_sprint_value = True)

    textEndereco.insert(END, endereco)

    textentryEndereco.delete(0, END)
    textentryUsuario.delete(0, END)
    textentrySenha.delete(0, END)
    windowPrincipal.tkraise()

def click_sair():
    root.destroy()
    exit()

def click_fechar():
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
textEndereco.delete(0.0, END)
textEndereco.insert(END, "entered_text")

Label(windowPrincipal, text = "Nome:", bg="black", fg="white", font="none 14 bold").pack(pady=10)
textName = Text(windowPrincipal, width=30, height=1, wrap=WORD, background="white", font="none 12")
textName.pack(padx=10)
textName.delete(0.0, END)
textName.insert(END, "entered_text")

Label(windowPrincipal, text = "Uptime:", bg="black", fg="white", font="none 14 bold").pack(pady=10)
textUptime = Text(windowPrincipal, width=30, height=1, wrap=WORD, background="white", font="none 12")
textUptime.pack(padx=10)
textUptime.delete(0.0, END)
textUptime.insert(END, "entered_text")

Label(windowPrincipal, text = "Bytes Enviados:", bg="black", fg="white", font="none 14 bold").pack(pady=10)
textBytesOut = Text(windowPrincipal, width=30, height=1, wrap=WORD, background="white", font="none 12")
textBytesOut.pack(padx=10)
textBytesOut.delete(0.0, END)
textBytesOut.insert(END, "entered_text")

Label(windowPrincipal, text = "Bytes Recebidos:", bg="black", fg="white", font="none 14 bold").pack(pady=10)
textBytesIn = Text(windowPrincipal, width=30, height=1, wrap=WORD, background="white", font="none 12")
textBytesIn.pack(padx=10)
textBytesIn.delete(0.0, END)
textBytesIn.insert(END, "entered_text")

# BOTAO (FECHAR SESSAO)
Button(windowPrincipal, text="FECHAR SESSÃO", width="12", command=click_fechar).pack(pady=10)


###################### -------------------------------------------------------------------------------

windowLogin.tkraise()
### MAIN LOOP
root.mainloop()