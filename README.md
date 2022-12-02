# Super Load Tests

Projeto com scripts no jmeter para testes de carga e stress no Super.

Inicialmente focamos para atender demanda específica no SEI4, portanto os testes disponibilizados até então suportam apenas essa plataforma.

O review e adpatação para o Super somente será feito após a priorização das issues  #8, #9 e #10

Em caso de necessidade e com conhecimento mediano em jmeter você consegue rapidamente isolar os assets e rodar os testes no Super.

## Divisão do Projeto

O projeto atualmente está dividido em 3 partes independentes. Ao entrar em cada pasta existe um README específico:

- **testes de carga e stress:** 
	aqui ficam os testes em jmeter para fazer carga e stress nos ambientes
	
- **testes de monitoramento:**
	aqui ficam testes em jmeter que ao implantar o sistema e nos depararmos com alguma lentidão foram necessários para o profissional da sustentação identificar possíveis gargalos relacionados a nó de aplicação ou ingress

	- **monitoramento-cookies-nagios:**
		esse teste faz inicialmente um apanhado dos cookies ofertados pela url com intuito de levantar os possíveis nós(ou pods) de entrada possíveis. Depois disso faz uma chamado ao sistema, logando com o usuário robô disponibilizado, e faz algumas operações simples para informar se o sistema está no ar.
		Segue junto um script para ser disponibilizado no Nagios para monitorar a disponiblidade
	
	
	- **monitoramento-nodes-ingress:**
		nesse teste você informa os possíveis nós físicos onde reside seus ingress kubernetes (ou seus balanceadores cattle, ou até mesmo as vms internas q ofertam o tráfego http ou https para o sistema) e dispara uma chamada independente para cada um deles testando o login e pesquisa simples de processo e documentos. A execução do teste em loop vai mostrar possíveis erros aleatórios que possam acontecer e listá-los para análise