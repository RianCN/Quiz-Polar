import tkinter as tk
from tkinter import messagebox
from PIL import Image, ImageTk
import pandas as pd
import random

#carregar os arquivos em Excel
df = pd.read_excel('questions.xlsx')

#pegar as perguntas aleatoriamente
questions = df.sample(n=10).values.tolist()


#variaveis globais
score = 0
curret_question = 0


#função para verificar resposta
def check_answer(answer):
    global score, curret_question

    if answer == correct_answer.get():
        score+=1

    curret_question +=1

    if curret_question < len(questions):
        display_question()
    else:
         show_reult()



#função para exibir a proxima pergunta
def display_question():
    question, option1, option2, option3, option4, answer = questions[curret_question]
    questions_label.config(text=question)
    option1_btn.config(text=option1, state=tk.NORMAL, command=lambda:check_answer(1))
    option2_btn.config(text=option2, state=tk.NORMAL, command=lambda:check_answer(2))
    option3_btn.config(text=option3, state=tk.NORMAL, command=lambda:check_answer(3))
    option4_btn.config(text=option4, state=tk.NORMAL, command=lambda:check_answer(4))

    correct_answer.set(answer)

#FUNÇÃO PARA EXIBIR O RESULTADO FINAL
def show_reult():
    messagebox.showinfo("Quiz Finalizado!", f"Parabéns! Você completou o Quiz!! \n\nPontuação Final dos pontos: {score}/{len(questions)}")
    option1_btn.config(state=tk.DISABLED)
    option2_btn.config(state=tk.DISABLED)
    option3_btn.config(state=tk.DISABLED)
    option4_btn.config(state=tk.DISABLED)
    play_again_btn.pack()

#JOGAR DE NOVO
def play_again():
    global score, curret_question
    score = 0
    curret_question = 0
    random.shuffle(questions) # embaralhar a lista de perguntas
    display_question() # exibir a próxima pergunta
    option1_btn.config(state=tk.NORMAL)
    option2_btn.config(state=tk.NORMAL)
    option3_btn.config(state=tk.NORMAL)
    option4_btn.config(state=tk.NORMAL)
    play_again_btn.pack_forget()


janela= tk.Tk()
janela.title("QUIZ POLAR")
janela.geometry("700x690")

#cores do Projeto
background_color = "#4196D3"
text_color = "#000000"
button_color = "#FFFFFF"
button_text_color ="#000000"

janela.config(bg=background_color)
janela.option_add('Font', 'Lilita One')

#icon na tela
imagem = Image.open("logopolar (1).png")
photo = ImageTk.PhotoImage(imagem)
label = tk.Label(janela, image=photo, bg=background_color)
label.pack(pady=10)


# Abre a segunda imagem
imagem2 = Image.open("urso polar.png")

# Converte a imagem para um objeto PhotoImage
photo2 = ImageTk.PhotoImage(imagem2)

# Cria um widget Label para exibir a imagem
label2 = tk.Label(janela, image=photo2, bg=background_color)
label2.pack(anchor='sw', side='bottom', pady=(10, 14))

#componetes de interface
questions_label = tk.Label(janela, text="", wraplength=498, bg=background_color, fg=text_color, font=("Lilita One", 20,))
questions_label.pack(pady=20)

correct_answer = tk.IntVar()


option1_btn = tk.Button(janela, text="", width=30, bg=button_color, fg= button_text_color,state=tk.DISABLED, font=("Lilita One", 12,))
option1_btn.pack(pady=10)

option2_btn = tk.Button(janela, text="", width=30, bg=button_color, fg= button_text_color,state=tk.DISABLED, font=("Lilita One", 12,))
option2_btn.pack(pady=10)

option3_btn = tk.Button(janela, text="", width=30, bg=button_color, fg= button_text_color,state=tk.DISABLED, font=("Lilita One", 12,))
option3_btn.pack(pady=10)

option4_btn = tk.Button(janela, text="", width=30, bg=button_color, fg= button_text_color,state=tk.DISABLED, font=("Lilita One", 12,))
option4_btn.pack(pady=10)

play_again_btn = tk.Button(janela,command=play_again, text="JOGAR NOVAMENTE", width=30, bg=button_color, fg= button_text_color, font=("Lilita One", 12,))


display_question()

janela.mainloop()



