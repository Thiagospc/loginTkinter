import tkinter as tk
from cores import co1, co2, co3, co4
import dados
from dados import logins

def app():
    janela = tk.Tk()
    janela.title("Login")
    janela.geometry('710x400')
    janela.configure(background=co1)
    janela.resizable(width=True, height=True)

    def separador():
        global frame_cima, frame_baixo
        frame_cima = tk.Frame(janela, width=710, height=90, bg=co4, relief='flat')
        frame_cima.grid(row=0, column=0, pady=1, padx=0, sticky=tk.NSEW)

        frame_baixo = tk.Frame(janela, width=710, height=350, bg=co4, relief='flat')
        frame_baixo.grid(row=1, column=0, pady=1, padx=0, sticky=tk.NSEW)  

    def imagem():
        imagem = tk.PhotoImage(file="/home/thiago/Documentos/loginToken/doc/imagem.png")
        rImagem = imagem.subsample(1, 2)
        

    def texto():
        lnome = tk.Label(frame_cima, text="LOGIN", anchor=tk.NW, font=("Ivy 50"), bg=co4, fg=co1)  
        lnome.place(x=235, y=10)

        textUser = tk.Label(frame_baixo, text="EMAIL", font=("Ivy 15"), bg=co4, fg=co1)
        textPass = tk.Label(frame_baixo, text="PASSWORD", font=("Ivy 15"), bg=co4, fg=co1)
        textUser.place(x=105, y=30)
        textPass.place(x=105, y=70)

    def emailSenha():
        global userName, passWord
        userName = tk.Entry(frame_baixo, font=("Ivy 12"), bg=co4, fg=co1)
        userName.place(x=235, y=30)
        passWord = tk.Entry(frame_baixo, show="*",  font=("Ivy 12"), bg=co4, fg=co1)
        passWord.place(x=235, y=70)

        
    def logar():
        bt = tk.Button(frame_baixo, text="ENTRAR", command=hello_world)
        bt.place(x=295, y=120)
    
    def hello_world():
        userGet = userName.get()
        passGet  = passWord.get()
        
        quantidade = len(logins) 
        global cont
        cont = 0

        for i in range(quantidade):
            listaTemp = []
            for n in logins[i]:
                listaTemp.append(n)

            
            if userGet == listaTemp[0] and passGet == listaTemp[1]:
                cont = cont + 1

                
            

        if cont != 0:
            print("login ok")

            # janela.destroy()
        else:
            print("login not")
        
        cont = 0

        listaTemp = []

        

    def ordemDeExecucao():
        separador()
        texto()
        emailSenha()
        logar()

    
    ordemDeExecucao()

    janela.mainloop()

app()