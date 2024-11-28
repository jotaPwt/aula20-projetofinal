# Veja a interpretação do IMC
# Entre 18,5 e 24,9	Normal	0
# Entre 25,0 e 29,9	Sobrepeso	I
# Entre 30,0 e 39,9	Obesidade	II
# Maior que 40,0	Obesidade Grave	III

import tkinter as tk

def calculo():
    peso = float(input_peso.get())
    altura = float(input_altura.get())
    imc = peso // (altura ** 2)
    result.config(text=f'{imc}')


    if imc < 18.5 :
        classificacao = tk.Label(root, text='Você é classificado como Desnutrido')
        classificacao.pack()
    elif imc >= 18.5 and imc < 30:
        classificacao = tk.Label(root, text='Você é classificado como Normal 0')
        classificacao.pack()
    elif imc > 25 and imc < 30:
        classificacao = tk.Label(root, text='Você é classificado como Sobrepeso I')
        classificacao.pack()
    elif imc >= 30 and imc <= 40:
        classificacao = tk.Label(root, text='Você é classificado como Obesidade II')
        classificacao.pack()
    elif imc >= 40:
        classificacao = tk.Label(root, text='Você é classificado como Obesidade Grave III')
        classificacao.pack()


    

root = tk.Tk()


root.title('Calculador IMC')
root.geometry('500x300')

# label

boas_vindas = tk.Label(root, text='Calculadora de IMC')
boas_vindas.pack()

# input

# nome

# nome_txt = tk.Label(root, text='Digite seu nome: ')
# nome_txt.pack()


# input_nome = tk.Entry(root)
# input_nome.pack()

# peso

peso_txt = tk.Label(root, text='Digite seu peso abaixo: ')
peso_txt.pack()

input_peso = tk.Entry(root)
input_peso.pack()

# altura

altura_txt = tk.Label(root, text='Digite sua altura abaixo: ')
altura_txt.pack()

input_altura = tk.Entry(root)
input_altura.pack()



# botoes

botao_ver = tk.Button(root, text='Calcular', command=calculo)
botao_ver.pack()

# resultado

result = tk.Label(root, text='Resultado:')
result.pack()


classificacao_txt = tk.Label(root, text='Classificacão: ')
classificacao_txt.pack()


root.mainloop()