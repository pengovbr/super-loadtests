# Super Load Tests

Nesta primeira versão dos testes de carga iremos disponibilizar em jmeter com 1 carga preparatória e 2 cenários iniciais.

O teste foi feito baseando-se no [sei-docker](https://github.com/spbgovbr/sei-docker). SEI4.0.7. Mas evoluirá para atender ao SEI e Super.


## Cenários Implementados


### Carga Inicial Preparatória

- Cria unidades (unidade00001, unidade00002, etc). A quantidade é informada no início do teste
- Cria usuários (usuario00001, etc). A quantidae é 20x a de unidades
- Cadastra Hierarquia das Unidades
- Cadastra as Permissoes de Usuários - Cada unidade vai ter 20 usuários
- Configura Endereço das Unidades
- Configura Num SEI p Unidades
- Configura Cargos de Assinatura para as Novas Unidades


### Teste de Carga

Cada cenário deve rodar simultaneamente.
Defina por cenário a qtde de usuarios simultaneos e as repetições dos cenários
O teste vai randomizar uma unidade e usuário para fazer o flood a cada repetição das threads.
Sendo assim vai criar processos em varias unidades.

- **Cenario 1**
	
	- Login
	- Novo Processo (tipo aleatorio)
	- Assunto aleatorio
	- Contato Fixo
	- Loop Cadastra Docs Internos
		- cria novo doc com tipo randomizado pre informado 
		- salva doc
		- edita 1a vez doc com centenas de linhas aleatorias
		- edita 2a vez doc com frase aleatoria para servir de pesquisa posterior com solr
		- assina o documento
	- Loop Cadastra Docs Externos
		- cria doc externo do tipo abaixo assinado
		- randomiza o upload com algum pdf q esteja disponivel no dir upload_files
		- salva

- **Cenario 2**
	
	- Seleciona aleatoriamente um processo cadastrado anteriormente
	- Seleciona aleatoriamente um usuário da unidade daquele processo
	- pesquisa pelo número do protocolo
	- para cada documento do protocolo, pesquisa individualmente usando o seu número
	



## Instruções Básicas

### Pré-teste

1. Suba o SEI, pode ser conforme em:  
	https://github.com/spbgovbr/sei-docker

2. Abra o teste PreCarga

3. Informe em User Defined Variables de acordo com o seu ambiente

4. Rode o pré-teste. Esse teste irá fazer a pré carga no ambiente com as unidades, usuários e configs necessárias para o teste rodar

5. O pré-teste é feito para rodar apenas 1x, mas pode rodar novamente se quiser, ele já está preparado para tratar caso já exista cadastro prévio

6. Caso o teste falhe, por alguma falha na infra, basta rodar novamente que ao rodar ele irá completar o cadastro. O teste de pré-carga deve chegar até o final, caso contrário houve algo errado

7. Vc sabe q ele chegou ao final olhando o "View Results Tree" da última thread. Ela deve finalizar sem requisicoes vemelhas

8. Agora q vc rodou o pré-teste pode rodar o teste de carga de várias formas analisando a carga
 

### Teste de carga

1. Informe em User Defined Variables de acordo com o seu ambiente e tb o que foi feito no pré-teste

2. Para cada cenário informe a quantidade de threads desejadas e tb as repetições. Observe que o cenário 2 deve entrar em ação apenas um tempo depois do cenário 1. Para isso vc pode usar o startup delay do ThreadGroup

3. Aqui vc pode rodar usando a interface jmeter ou caso a carga seja alta deve rodar usando linha de comando

4. Os resultados devem ser coletados e analisados a luz da filosofia jmeter e tb levando em consideração o que vc deseja medir


## Futuras implementações

Está previsto implementarmos mais cenários e tb outras funcionalidades. Porém as mesmas ainda não foram priorizadas internamente.

Entre elas:
- Flood de Pesquisa usando Solr
- Blocos de Assinatura e Assinatura em unidades externas ao processo
- Tramitação de processo para outra unidade e conclusão
- Humanização dos testes para definir melhor quantos usuários o ambiente aguenta


## Dúvidas ou Sugestões

Pode usar a parte de issue aqui do projeto no github.
Contribuição pode enviar pull-requests
