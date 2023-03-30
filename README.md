Documentação das Funções do Script Python

Descrição
Este script Python define diversas funções que podem ser úteis para automatizar tarefas repetitivas em um sistema operacional Windows. As funções incluem clicar em imagens na tela, escrever texto, apertar teclas, notificar o usuário e muito mais.

Exemplos de Uso
Para utilizar as funções definidas no script Python, basta importá-las para o seu próprio código e chamar a função desejada com os argumentos adequados. Por exemplo:

Importando as funções do script
from nome_do_script import *

Exemplo de uso das funções
notificar(conteudo='Bot Citrix executando com sucesso',titulo='Bot Citrix',duracao=10)
esperar(5)
clicar_na_imagem('nome_da_imagem.png')
escreva('Exemplo de texto')
apertar_tecla('enter')
segurar_tecla('ctrl')
apertar(['c'])
soltar_tecla('ctrl')

Lista de Funções

clicar_na_imagem(nome_da_imagem)
click(x, y, segundos=1)
escreva(texto)
apertar_tecla(tecla)
esperar(segundos=1)
fale(texto_a_se_falado)
notificar(conteudo='Bot Citrix executando com sucesso',titulo='Bot Citrix',duracao=10)
enter()
tab()
alt()
seta_para_cima()
seta_para_baixo()
seta_para_direita()
seta_para_esquerda()
apertar(nome_da_tecla)
segurar_tecla(nome_da_tecla)
soltar_tecla(nome_da_tecla)
simple_click(x, y, segundos=1)
cmd(comando_cmd="echo sem comando")
duplo_click(x, y, segundos=1)
alt_tab()
windows_d()
