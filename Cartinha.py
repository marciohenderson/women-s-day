import tkinter as tk
import pygame
from PIL import Image, ImageTk

pygame.mixer.init()

# função para colocar fundo
def colocar_fundo(janela, arquivo):
    imagem = Image.open(arquivo)
    imagem = imagem.resize((479,639))
    fundo = ImageTk.PhotoImage(imagem)

    label_fundo = tk.Label(janela, image=fundo)
    label_fundo.place(x=0, y=0, relwidth=1, relheight=1)

    label_fundo.image = fundo


def abrir_final():
    janela3 = tk.Toplevel()
    janela3.title("This is for you my baby! I love you so much ❤️")
    janela3.geometry("479x639")

    colocar_fundo(janela3, "fundo2.jpg")

    # tocar música
    pygame.mixer.music.load("musica.mp3")
    pygame.mixer.music.play(-1)

    texto_final = tk.Label(
        janela3,
        text="Isso é para você meu amor 🌸🌺🌼🌻🌷🌹",
        font=("Comic Sans MS",16),
        fg="Black",
        bg= "#a3ab98"
    )
    texto_final.place(relx=0.5, rely=0.5, anchor="center")


def abrir_surpresa():
    janela2 = tk.Toplevel()
    janela2.title("Surpresa")
    janela2.geometry("479x639")

    colocar_fundo(janela2, "fundo.jpg")

    texto = tk.Label(
        janela2,
        text="Feliz dia das mulheres minha mulher incrível! sou eternamente grato por você meu amor! aproveite esse dia tão especial para você, continue sendo sempre essa garotinha LINDA e MARAVILHOSA que eu amoooooo!!! ❤️❤️❤️❤️❤️❤️❤️❤️❤️❤️❤️❤️❤️❤️❤️❤️❤️❤️❤️❤️❤️❤️❤️❤️❤️❤️❤️❤️❤️❤️❤️❤️❤️❤️❤️",
        font=("Comic Sans MS",16),
        wraplength=420,
        justify="center",
        fg="black"
    )
    texto.place(relx=0.5, rely=0.35, anchor="center")

    botao_proximo = tk.Button(
        janela2,
        text="mais uma surpresinha rs",
        font=("Comic Sans MS",10),
        command=abrir_final
    )
    botao_proximo.place(relx=0.5, rely=0.9, anchor="center")


def criar_janela():
    janela = tk.Tk()
    janela.title("Dia das Mulheres ❤️")
    janela.geometry("479x639")

    colocar_fundo(janela, "fundo.jpg")

    titulo = tk.Label(
        janela,
        text="Feliz dia das mulheres MEU AMOR!",
        font=("Comic Sans MS",18,),
        fg="black"
    )
    titulo.pack(pady=150)

    botao = tk.Button(
        janela,
        text="Clique aqui para uma surpresa! rsrs",
        font=("Comic Sans MS",12),
        command=abrir_surpresa
    )
    botao.pack()

    janela.mainloop()


criar_janela()