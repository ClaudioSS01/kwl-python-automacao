import pyautogui
from time import sleep
import pyttsx3
import os

def clicar_na_imagem(nome_da_imagem):
        location = None
        imageFile = nome_da_imagem
        while (location == None):
                print("procurando...")
                try:
                        location = pyautogui.locateOnScreen(imageFile)
                except Exception as e:
                        print(e)

        print(location)
        centro_da_imagem = pyautogui.center(location)
        print("o centro da imagem é ")
        print(centro_da_imagem)
        pyautogui.doubleClick(centro_da_imagem)
        esperar(10)
        pass


def click(x,y,segundos=1):
        try:
                pyautogui.doubleClick(x,y,duration=segundos)
        except:
                print("nao conseguimos clicar nas cordenadas: x ="+str(x)+" y="+str(y))
                pass



def escreva(texto):
        try:
                pyautogui.write(texto)
        except:
                print("nao conseguimos escrever o texto: "+str(texto))

def apertar_tecla(tecla):
        try:
                pyautogui.press(tecla)
        except:
                print("nao conseguimos escrever o texto: "+str(tecla))




def esperar(segundos=1):
        sleep(segundos)



#pip install win10toast
from win10toast import ToastNotifier
toast = ToastNotifier()

def fale(texto_a_se_falado):
        robo = pyttsx3.init()
        robo.say(texto_a_se_falado)
        
        #os.system('cmd /k  echo >script.vbs "CreateObject(""SAPI.SpVoice"").Speak(""'+str(texto_a_se_falado)+'"") & script.vbs')
 


def notificar(conteudo='Bot Citrix executando com sucesso',titulo='Bot Citrix',duracao=10):
        print('notificando')
        print("titulo: "+str(titulo))
        print('conteudo: '+str(conteudo))
        print("duração: "+str(duracao))
        toast.show_toast(titulo,conteudo,duration=duracao,icon_path="icon.ico",threaded=True)
        fale(conteudo)

def enter():
        pyautogui.press('enter')

def tab():
        pyautogui.press(['tab'])

def alt():
        cmd('echo >script.vbs set shell = CreateObject("WScript.Shell"):shell.SendKeys "{%}" & script.vbs')

def seta_para_cima():
        pyautogui.press('up')

def seta_para_baixo():
        pyautogui.press('down')

def seta_para_direita():
        pyautogui.press('right')

def seta_para_esquerda():
        pyautogui.press('left')


def apertar(nome_da_tecla):
        try:
                pyautogui.press(nome_da_tecla)
        except:
                print("tecla invalida")


def segurar_tecla(nome_da_tecla):
        try:
                pyautogui.keyDown(nome_da_tecla)
        except:
                print("tecla invalida")

def soltar_tecla(nome_da_tecla):
        try:
                pyautogui.keyUp(nome_da_tecla)
        except:
                print("tecla invalida")

def simple_click(x,y,segundos=1):
        pyautogui.click(x,y,duration=segundos)


def cmd(comando_cmd="echo sem comando"):
        try:
                com = comando_cmd
                return_value = os.system("cmd /k "+str(com))
                print('o retorno do comando foi: ', return_value)
        except:
                pass


def duplo_click(x,y,segundos=1):
        pyautogui.click(x,y,duration=segundos)



def alt_tab():
        segurar_tecla('alt')
        #aperta o tab
        apertar(['tab'])
        #solta o alt
        soltar_tecla('alt')


def windows_d():
        segurar_tecla('win')
        #aperta o tab
        apertar('d')
        #solta o tecla windows
        soltar_tecla('win')
