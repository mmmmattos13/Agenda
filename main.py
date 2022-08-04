from time import sleep

AGENDA = {}

def limpar():
  import os
  from time import sleep
  def screen_clear():
    if os.name == 'posix':
      _ = os.system('clear')
    else:
      _ = os.system('cls')
  sleep(1)
  screen_clear()


def menu():
  print('----------------------------------------')
  print('============>>> MENU <<<================')
  print('----------------------------------------')
  print("[1] - Entrar no sistema")
  print("[0] - Sair")
  escolha = int(input("Selecione uma das opções: "))
  return escolha

def sub_menu():
  limpar()
  print('----------------------------------------')
  print('============>>> SUB-MENU <<<================')
  print('----------------------------------------')

  print('[1] - Mostrar todos os contatos da agenda')
  print('[2] - Buscar contato')
  print('[3] - Incluir contato')
  print('[4] - Editar contato')
  print('[5] - Excluir contato')
  print('[6] - Exportar contatos para CSV')
  print('[7] - Importar contatos CSV')
  print('[0] - Retornar ao menu')
  print('------------------------------------------')
  escolha = int(input("Selecione uma das opções: "))
  return escolha

def buscar_contato(contato):
  try:
    print("Nome: ", contato)
    print("Telefone: ", AGENDA[contato]['telefone'])
    print("E-mail: ", AGENDA[contato]['email'])
    print("Endereço: ", AGENDA[contato]['endereco'])
    print(40*"-")
  except KeyError:
    print(">>>Contato inexistente")
  except Exception as error:
    print(error)  
def exibir_contatos():
  if AGENDA:
    for j in AGENDA:
      buscar_contato(j)
  else:
    print("AGENDA VAZIA")
    input("PRESSIONE <ENTER> PARA CONTINUAR")
    



def detalhes_contato():  
  telefone = input("Digite o telefone: ")
  email = input('Digite o email: ')
  endereco = input('Digite o endereço: ')
  return telefone, email, endereco
def incluir_contato(contato, telefone, email, endereco):
  AGENDA[contato] = {'telefone':telefone, 'email':email, 'endereco':endereco}
  salvar()
  print("\n")
  print(f">>> Contato {contato} adicionado com sucesso")
  input("Pressione <ENTER> para continuar...")
def excluir_contato(contato):
  try:
    AGENDA.pop(contato)
    salvar()
    print()
    print(f">>> Contato {contato} adicionado com sucesso")
  except Exception as e:
    print(e)
  else:
    input("Pressione <ENTER> para continuar...")

def importar_contatos(agenda):
  try:
    with open(agenda, 'r') as arquivo:
      linhas = arquivo.readlines()
      for linha in linhas:
        detalhes = linha.strip().split(',')
  
        nome = detalhes[0]
        telefone = detalhes[1]
        email = detalhes[2]
        endereco = detalhes[3]

        incluir_contato(nome, telefone, email, endereco)
  except FileNotFoundError:
    print('>>>> Arquivo não encontrado')
  except Exception as error:
    print('>>>> Algum erro inesperado ocorreu!')
    print(error)
def exportar_contatos(agenda):
  try:
    with open(agenda, 'w') as arquivo:
      for contato in AGENDA:
        telefone = AGENDA[contato]['telefone']
        email = AGENDA[contato]['email']
        endereco = AGENDA[contato]['endereco']
        arquivo.write("{},{},{},{}\n".format(contato, telefone, email, endereco))
    print(">>>Agenda exportada com sucesso!")
  except Exception as e:
    print(e)
  else:
    input("PRESSIONE <ENTER> PARA CONTINUAR...")

def salvar():
  exportar_contatos("agenda.csv")
def carregar():
  try:
    with open('agenda.csv', 'r') as arquivo:
      linhas = arquivo.readlines()
      for j in linhas:
        detalhes = j.strip().split(',')
        nome = detalhes[0]
        telefone = detalhes[1]
        email = detalhes[2]
        endereco = detalhes[3]

        AGENDA[nome] = {'telefone':telefone,'email':email,'endereco':endereco}
    print(">>> Database carregado com sucesso!")
    print(f"{len(AGENDA)} contatos carregados.")
  except FileNotFoundError:
    print("Arquivo não encontrado!")
  except Exception as e:
    print(e)
  else:
    input("PRESSIONE <ENTER> PARA CONTINUAR...")
    limpar()

while True:
  carregar()
  opcao = menu()
  if opcao == 1:   
    limpar()
    escolha = sub_menu()    
    if escolha == 1:
      limpar()
      exibir_contatos()
    elif escolha == 2:
      contato = input("Digite o nome do contato: ")
      buscar_contato(contato)
    elif escolha == 3:
      contato = input("Digite o nome do contato: ")      
      try:
        AGENDA[contato]
        print(">>>Contato existente!")
      except KeyError:
        telefone, email, endereco = detalhes_contato()
      incluir_contato(contato, telefone, email, endereco)
    elif escolha == 4:
      exibir_contatos()
      contato = input("Digite o nome do contato: ")
      try:
        AGENDA[contato]
        print(f"Editando contato {contato}")
        telefone, email, endereco = detalhes_contato()
        incluir_contato(contato, telefone, email, endereco)
      except KeyError:
        print('>>>> Contato inexistente')
      else:
        input("PRESSIONE <ENTER> PARA CONTINUAR...")
    elif escolha == 5:
      exibir_contatos()
      contato = input("Digite o nome do contato a excluir: ")
      excluir_contato(contato)
    elif escolha == 6:
      arquivo = input("Nome do arquivo: ")
      exportar_contatos(arquivo)
    elif escolha == 7:
      arquivo = input("Nome do arquivo: ")
      importar_contatos(arquivo)
    elif escolha == 0:
      menu()
    else:
      print("Opção inválida!")
      input("PRESSIONE <ENTER> PARA CONTINUAR...")
  elif opcao == 0:
    print("Encerrando programa...")
    sleep(1)
    break
  else:
    print("Opção inválida!")    