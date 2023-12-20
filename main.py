from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time
import pandas as pd
import tkinter as tk
from tkinter import messagebox

url_situator = ''
caminho_planilha = r''
dados = pd.read_excel(caminho_planilha, dtype=str)
array_dados = dados.to_numpy()
print(array_dados)
driver = webdriver.Chrome()

driver.get(url_situator)

time.sleep(5)

campo_nome = driver.find_element(by=By.ID, value="userName")
campo_nome.send_keys("")
campo_senha = driver.find_element(by=By.ID, value="password")
campo_senha.send_keys("")
campo_nome.send_keys(Keys.ENTER)
time.sleep(5)
driver.get('')
time.sleep(4)



for linha in array_dados:
    for elemento in linha:
        campo_elemento = driver.find_element(by=By.CLASS_NAME, value="add-new-data")
        campo_elemento.click()
        time.sleep(8)
        campo_nome = driver.find_element(by=By.ID, value="control-ref_name")
        campo_nome.send_keys(elemento)
        time.sleep(2)
        campo_nome.send_keys(Keys.ENTER)

time.sleep(5)
driver.quit()

fonte = ("Arial", 24)
def realizar_teste():
    print("Breve teste realizado com sucesso!")
    janela.destroy()


janela = tk.Tk()
fonte = ("Arial", 12)
rotulo = tk.Label(janela, text="Migração 100% Concluida Obrigado por usar meu sistema. Por: Willian Hora", font=fonte)
rotulo.pack(pady=10)
botao_ok = tk.Button(janela, text="fechar", command=realizar_teste)
botao_ok.pack(pady=20)
largura_tela = janela.winfo_screenwidth()
altura_tela = janela.winfo_screenheight()
pos_x = (largura_tela - janela.winfo_reqwidth()) / 2
pos_y = (altura_tela - janela.winfo_reqheight()) / 2
janela.geometry("+%d+%d" % (pos_x, pos_y))
janela.mainloop()


