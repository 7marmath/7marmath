print("Registro")

tabela = []
Id=0
# definindo função
def buscarNome (tabela,nameSearch) :
    for paciente in tabela :
        if paciente[1] == nameSearch :
            return paciente
    return None
def buscarId (tabela,idSearch) :
    for paciente in tabela :
        if paciente[0] == int(idSearch) :
            return paciente
    return None
while True:
    option = str(input("\n 1-Cadastr paciente-= \n 2-Buscar paciente \n 3-Listar pacientes \n 4-Atualizar Cadastro  \n 5-Deletar Paciente \n 6-sair \n\n Escolha a opção:  "))
    if option == '1' :
        Id += 1
        print("ID : " , Id)
        cpf=str(input("CPF do paciente: "))
        name=str(input("Nome completo: "))
        momName=str(input("Nome da mãe:  "))
        born=str(input("Data de Nascimento:  "))
    elif option == '2' :
        tabela.append([Id,name,momName,born,cpf])
        print("buscando paciente")
        nameSearch = str(input("insira o nome completo do paciente: \n | "))
        found=buscarNome(tabela,nameSearch)
        if found == None :
            print('Paciente não encontrado')
    elif option == '3' :
        print ("exibindo lista")
        print(" \n Lista de contatos: " )
        for paciente in tabela :
            print (f"ID: {paciente[0]} - Nome : {paciente[1]} - Nome da mãe: {paciente[2]} - Data de nascimento: {paciente[3]} - CPF: {paciente[4]} " )
    elif option == '4' :
        print("editar um paciente")
        idSearch = str(input("insira o ID do paciente: \n | "))
        found=buscarId(tabela,idSearch)
        if found == None :
            print('Paciente não encontrado')
        else :
            print('Paciente encontrado , insira os novos dados: ')
            cpf=str(input("novo CPF do paciente: "))
            name=str(input("novo Nome completo: "))
            momName=str(input("novo Nome da mãe:  "))
            born=str(input("nova Data de Nascimento:  "))
            found[1] = name
            found[2] = momName
            found[3] = born
            found[4] = cpf
            print( 'dados atualizados com sucesso!')
    elif option == '5' :
        print(" \n Deletar paciente: " )
        for paciente in tabela :
            print (f"ID: {paciente[0]} - Nome : {paciente[1]} - Nome da mãe: {paciente[2]} - Data de nascimento: {paciente[3]} - CPF: {paciente[4]} " )
        removeId = int(input(" Informe ID a ser removido: ")) - 1
        removeId = tabela.pop(removeId)
        print("paciente removido com sucesso")
    elif option == '6' :
        break