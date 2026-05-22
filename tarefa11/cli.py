import users_wrapper as users

while True:

    print('\n========== USERS CRUD ==========')
    print('1 - Listar usuários')
    print('2 - Ler usuário')
    print('3 - Criar usuário')
    print('4 - Atualizar usuário')
    print('5 - Deletar usuário')
    print('6 - Listar tarefas do usuário')
    print('0 - Sair')

    opcao = input('Escolha: ')

    if opcao == '1':

        lista = users.list()

        print('\nUSUÁRIOS:')
        for user in lista:
            print(user['id'], '-', user['name'])

    elif opcao == '2':

        user_id = input('ID do usuário: ')

        user = users.read(user_id)

        print('\nNome:', user['name'])
        print('Username:', user['username'])
        print('Email:', user['email'])

    elif opcao == '3':

        nome = input('Nome: ')
        usuario = input('Usuário: ')
        email = input('Email: ')

        novo_user = {
            'nome': nome,
            'usuario': usuario,
            'email': email
        }

        resposta = users.create(novo_user)

        print('\nUsuário criado:')
        print(resposta)

    elif opcao == '4':

        user_id = input('ID do usuário: ')
        nome = input('Novo nome: ')
        usuario = input('Novo username: ')
        email = input('Novo email: ')

        user_atualizado = {
            'nome': nome,
            'usuario': usuario,
            'email': email
        }

        resposta = users.update(user_id, user_atualizado)

        print('\nUsuário atualizado:')
        print(resposta)

    elif opcao == '5':

        user_id = input('ID do usuário: ')

        status = users.delete(user_id)

        print('\nStatus HTTP:', status)

    elif opcao == '6':

        user_id = input('ID do usuário: ')

        todos = users.todos(user_id)

        print('\nTAREFAS:')

        for todo in todos:

            status = 'Completo' if todo['completed'] else 'Pendente'

            print(f"{status} {todo['title']}")

    elif opcao == '0':
        break

    else:
        print('Opção inválida')