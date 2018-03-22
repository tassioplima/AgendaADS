#Mensagem de Bem Vindo e Opcoes ao Usuario
import csv

def bemvindo():
	print("Bem Vindo a Agenda")
	print("Selecione uma Opcao")
	print("1  Adicionar um novo contato")
	print("2  Listar os contatos da agenda")
	print("3  Excluir contatos da agenda")
	print('4  Buscar contato pelo nome')
	print('9  Sair')


#Funcoes do processo
def adicionar():
	print("Adicionar um registro")
	agenda = open("agendatelefonica.csv",'a')
	nome = input("Nome do Contato:").lower()
	telefone = input("Digite o telefone:")
	print("Contato salvo com nome:",nome," e numero",telefone)
	agenda.write(nome)
	agenda.write(",")
	agenda.write(telefone)
	agenda.write(",")
	agenda.write("\n")
	agenda.close()
	
	
	
def listar():
	data = open('agendatelefonica.csv')
	numero = 0
	for linhas in data:
		numero = numero + 1
		print (numero, linhas)

	print ('Listado corretamente')
	data.close()	


def falha():
	print("Opcao Incorreta")


def excluir():
	import csv
	lista = []
	agenda = open('agendatelefonica.csv', 'r')
	ler = csv.reader(agenda)
	for lin in ler:
		lista.append(lin)

	nome = input('Escreva o nome para excluir da agenda\n').lower()
	x=0
	resp=0
	while x < len(lista):
		contato = lista[x]
		if nome in contato:
			print('Deseja excluir este contato?\n')
			print('Nome {} - Telefone {}\n'.format(contato[0],contato[1]))
			resp=int(input('[1]Sim   [2]Nao'))
			if resp==1:
				del(lista[x])
				print('contato excluido')
				break
		x += 1

	if resp != 1:
		print('Contato não encontrado')


	agenda.close()

	agenda = open('agendatelefonica.csv', 'w')
	agenda.truncate()
	agenda.close()

	agenda = open('agendatelefonica.csv', 'a')
	for linha in lista:
		for dado in linha:
			agenda.write(dado)
			if dado == '':
				agenda.write("\n")
			else:
				agenda.write(',')
				




def buscar_nome():
        import csv
        lista = []
        with open('agendatelefonica.csv') as csvfile:
                leitor = csv.reader(csvfile, delimiter=',')
                for linha in leitor:
                        lista.append(linha)
        x=0
        nome = input('Escreva o nome que procura na agenda:\n').lower()
        while x<len(lista):
                a = lista[x]
                if nome in a:
                        print('\nNome: {} - Telefone: {}'.format(a[0],a[1]))
                x+=1
        if x == len(lista):
                print('\n\nTodos contatos com este nome foram listados!! Caso não listado cadastre o contato.')
