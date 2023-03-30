# kwl-python-automacao
# Documentação das Funções do Script Python<br>
</head>
<body>
	<h1>Documentação das Funções do Script Python</h1>

	<h2>Descrição</h2>
	<p>Este script Python define diversas funções que podem ser úteis para automatizar tarefas repetitivas em um sistema operacional Windows. As funções incluem clicar em imagens na tela, escrever texto, apertar teclas, notificar o usuário e muito mais.</p>

	<h2>Exemplos de Uso</h2>
	<p>Para utilizar as funções definidas no script Python, basta importá-las para o seu próprio código e chamar a função desejada com os argumentos adequados. Por exemplo:</p>

	<pre><code># Importando as funções do script
from nome_do_script import *

# Exemplo de uso das funções
notificar(conteudo='Bot Citrix executando com sucesso',titulo='Bot Citrix',duracao=10)
esperar(5)
clicar_na_imagem('nome_da_imagem.png')
escreva('Exemplo de texto')
apertar_tecla('enter')
segurar_tecla('ctrl')
apertar(['c'])
soltar_tecla('ctrl')</code></pre>

	<h2>Lista de Funções</h2>
	<ul>
		<li>clicar_na_imagem(nome_da_imagem)</li>
		<li>click(x, y, segundos=1)</li>
		<li>escreva(texto)</li>
		<li>apertar_tecla(tecla)</li>
		<li>esperar(segundos=1)</li>
		<li>fale(texto_a_se_falado)</li>
		<li>notificar(conteudo='Bot Citrix executando com sucesso',titulo='Bot Citrix',duracao=10)</li>
		<li>enter()</li>
		<li>tab()</li>
		<li>alt()</li>
		<li>seta_para_cima()</li>
		<li>seta_para_baixo()</li>
		<li>seta_para_direita()</li>
		<li>seta_para_esquerda()</li>
		<li>apertar(nome_da_tecla)</li>
		<li>segurar_tecla(nome_da_tecla)</li>
		<li>soltar_tecla(nome_da_tecla)</li>
		<li>simple_click(x, y, segundos=1)</li>
		<li>cmd(comando_cmd="echo sem comando")</li>
		<li>duplo_click(x, y, segundos=1)</li>
		<li>alt_tab()</li>
		<li>windows_d()</li>
	</ul>
</body>
</html>
