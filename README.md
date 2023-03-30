# Documentação das Funções do Script Python

# Descrição
<br>
Este script Python define diversas funções que podem ser úteis para automatizar tarefas repetitivas em um sistema operacional Windows. As funções incluem clicar em imagens na tela, escrever texto, apertar teclas, notificar o usuário e muito mais.
<br>
<b>Exemplos de Uso</b><br>
Para utilizar as funções definidas no script Python, basta importá-las para o seu próprio código e chamar a função desejada com os argumentos adequados. Por exemplo:
<br>
Importando as funções do script
<br>
```
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
```
<br>

<b>Lista de Funções</b><br>
<ul>
  <li>
clicar_na_imagem(nome_da_imagem)</li><br><li>
click(x, y, segundos=1)</li><br><li>
escreva(texto)</li><br><li>
apertar_tecla(tecla)</li><br><li>
esperar(segundos=1)</li><br><li>
fale(texto_a_se_falado)</li><br><li>
notificar(conteudo='Bot Citrix executando com sucesso',titulo='Bot Citrix',duracao=10)</li><br><li>
enter()</li><br><li>
tab()</li><br><li>
alt()</li><br><li>
seta_para_cima()</li><br><li>
seta_para_baixo()</li><br><li>
seta_para_direita()</li><br><li>
seta_para_esquerda()</li><br><li>
apertar(nome_da_tecla)</li><br><li>
segurar_tecla(nome_da_tecla)</li><br><li>
soltar_tecla(nome_da_tecla)</li><br><li>
simple_click(x, y, segundos=1)</li><br><li>
cmd(comando_cmd="echo sem comando")</li><br><li>
duplo_click(x, y, segundos=1)</li><br><li>
alt_tab()</li><br><li>
windows_d()</li></ul>
