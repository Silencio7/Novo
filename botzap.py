from selenium import webdriver
import pyautogui
import time
from tkinter import *


class WhatsappBot:
    def __init__(self, contatos, mensagem):
        self.mensagem = mensagem
        self.contatos = contatos
        options = webdriver.FirefoxOptions()
        options.add_argument('lang=pt-br')
        self.navegador = webdriver.Firefox(executable_path="./geckodriver.exe")

    def enviar_mensagens(self):
        self.navegador.get('https://web.whatsapp.com')
        time.sleep(15)
        for contatos in self.contatos:
            self.navegador.find_element_by_class_name('_13NKt').send_keys(f'{contatos}')
            time.sleep(2)
            pyautogui.press("Enter")
            time.sleep(1)
            chat_box = self.navegador.find_element_by_xpath("/html/body/div[1]/div[1]/div[1]/div[4]/div[1]\
                                                                /footer/div[1]/div/div/div[2]/div[1]/div/div[2]")
            time.sleep(1)
            chat_box.click()
            chat_box.send_keys(self.mensagem)
            botao_enviar = self.navegador.find_element_by_xpath("/html/body/div[1]/div[1]/div[1]/div[4]/div[1]\
                                                                        /footer/div[1]/div/div/div[2]/div[2]/button")
            time.sleep(1.5)
            botao_enviar.click()
            time.sleep(2)


def janela_bot():
    janela = Tk()
    janela.geometry('170x160+580+280')
    janela.configure(background='black')
    janela.title('V.1 - WhatsApp.Bot')
    texto_vazio2 = Label(janela, text='', bg='black')
    texto_vazio2.grid(column=0, row=0)
    texto_vazio3 = Label(janela, text='', bg='black')
    texto_vazio3.grid(column=1, row=0)
    texto_cont = Label(janela, text='Insira os contatos:', bg='black', fg='white')
    texto_cont.grid(column=2, row=1)
    caixa1 = Entry(janela, font='Courier 8', bd=2, justify='left', fg='black')
    caixa1.grid(column=2, row=2)
    texto_cont = Label(janela, text='Insira a mensagem:', bg='black', fg='white')
    texto_cont.grid(column=2, row=3)
    caixa2 = Entry(janela, font='Courier 8', bd=2, justify='left', fg='black')
    caixa2.grid(column=2, row=4)
    # texto_inicial = Label(janela, text='Clique no "Iniciar" para começar o funcionamento do Bot.', bg='black',
    #                       fg='white')
    # texto_inicial.grid(column=0, row=5)
    texto_vazio2 = Label(janela, text='', bg='black')
    texto_vazio2.grid(column=2, row=5)
    botao = Button(janela, text="Iniciar", command=janela.destroy, font='bold 9')
    botao.grid(column=2, row=6)

    janela.mainloop()


def janela_bot2():
    janela = Tk()
    janela.geometry('165x70+580+290')
    janela.configure(bg='black')
    janela.title('V.1 - WhatsApp.Bot')
    texto_inicial = Label(janela, text="O Bot terminou o seu serviço.", bg='black', fg='white')
    texto_inicial.grid(column=0, row=1)
    botao = Button(janela, text="Encerrar", command=janela.quit, font='bold 8')
    botao.grid(column=0, row=2)
    texto_inicial = Label(janela, text="Obrigado por utilizar!", bg='black', fg='white')
    texto_inicial.grid(column=0, row=3)
    janela.mainloop()


janela_bot()
# try:
bot = WhatsappBot()
bot.enviar_mensagens()
# except Exception as erro:
#     print(erro)
janela_bot2()
