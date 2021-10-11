from collections import OrderedDict 

def inserirUsuarios(lista_nomes, lista_emails):


    nome = str(input("Digite o seu nome: "))
    email = str(input("Digite o seu email: "))

    lista_nomes.append(nome)
    lista_emails.append(email)

    return lista_nomes, lista_emails

def listarUsuarios(lista_nomes, lista_emails):
    cont = 0

    for cada in lista_nomes:
        print(lista_nomes[cont], ":", lista_emails[cont])
        cont+=1 

def listarUsuariosAlfabetica(lista_nomes, lista_emails):
    dicionario = dict(zip(lista_nomes, lista_emails))
    dicionarioAlfab = OrderedDict(sorted(dicionario.items()))

    for item in dicionarioAlfab:
        print(item, ":", dicionarioAlfab[item])

def find_name(lista_nomes, lista_emails):
    i = False
    while(i == False):
        name = input("Insira o nome de quem procuras: \n")
        if(name in lista_nomes):
            index = lista_nomes.index(name)
            print("As informações associadas ao nome {} é:\nE-mail: {}".format(name,lista_emails[index]))

            i = True
        else: 
            print('Valor não encontrado')

            i = False

def remover_usuario(lista_nomes, lista_emails):
    email = input('Digite o email do usuário: ')
    if email in lista_emails:
        index = lista_emails.index(email)
        nome = lista_nomes[index]

        print('O usuário {} foi removido.'.format(lista_nomes[index]))

        lista_nomes.remove(nome)
        lista_emails.remove(email)
    else:
        print('Não foi localizado nenhum email.')
    return(lista_nomes, lista_emails)

def alterar_nome(lista_nomes, lista_emails):
    email = input('Digite o email do usuário: ')
    if email in lista_emails:
        index = lista_emails.index(email)
        print('O nome do usuário é {}'.format(lista_nomes[index]))
        lista_nomes[index] = input('Digite o novo nome do usuário: ')
        print('O nome do usuário agora é {}'.format(lista_nomes[index]))
    else:
        print('Não foi localizado nenhum email.')

    return(lista_nomes, lista_emails)

def main(menu,lista_nomes,lista_emails):
    i = False
    exit = False

    print('--------------------------')
    print('Você está no menu principal.\nSelecione uma opção para prosseguir:\n')
    print('1: Cadastrar novo Usuário.\n2: Listar Usuários por ordem de cadastro.\n3: Listar Usuários por ordem alfabética.')
    print('4: Buscar Usuário.\n5: Remover Usuário.\n6: Alterar o nome de um Usuário.\n7: Fechar o Programa.')
    print('--------------------------\n')
    menu = int(input())

    while(i == False):
        if(menu == 1):
            lista_nomes, lista_emails = inserirUsuarios(lista_nomes, lista_emails)
            i = True
        elif(menu == 2):
            listarUsuarios(lista_nomes, lista_emails)
            i = True
        elif(menu == 3):
            listarUsuariosAlfabetica(lista_nomes, lista_emails)
            i = True
        elif(menu == 4):
            find_name(lista_nomes, lista_emails)
            i = True
        elif(menu == 5):
            lista_nomes, lista_emails = remover_usuario(lista_nomes, lista_emails)
            i = True
        elif(menu == 6):
            lista_nomes, lista_emails = alterar_nome(lista_nomes, lista_emails)
            i = True
        elif(menu == 7):
            i = True
            exit = True
        else:
            menu = int(input('Menu inválido. Por favor, digite o menu desejado:\n'))
    return(exit, lista_nomes, lista_emails)

lista_nomes = []
lista_emails = []
exit = False
menu = 0

while(exit == False):
    exit,lista_nomes,lista_emails = main(menu,lista_nomes,lista_emails)