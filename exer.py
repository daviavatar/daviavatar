usuario_filmes = {}


print('Cadastro de filmes')

while True:
  
   print('1 - adicionar filme')
   print('2 - remover filme')
   print('3 - ver filmes de um usuário')
   print('4 - ver todos os usuários')
   print('0 - sair')

   opcao = input('Escolha uma opção: \n')

   match opcao:
      case '1':
         usuario = input('Digite o nome do usuário: ').strip().title()
         filme = input('Digite o nome do filme: ').strip().title()
         if usuario not in usuario_filmes:
            usuario_filmes[usuario] = []
         usuario_filmes[usuario].append(filme)
         print(f'Filme "{filme}" adicionado para o usuário "{usuario}".')

      case '2':
         usuario = input('Digite o nome do usuário: ').strip().title()
         filme = input('Digite o nome do filme: ').strip().title()
         filmes = usuario_filmes.get(usuario)
         if filmes and filme in filmes:
            filmes.remove(filme)
            print(f'Filme "{filme}" removido do usuário "{usuario}".')
         else:
            print(f'Filme "{filme}" não encontrado para o usuário "{usuario}".')
      
      case '3':
         usuario = input('Digite o nome do usuário: ').strip().title()
         filmes = usuario_filmes.get(usuario)
         if filmes:
            print(f'Filmes do usuário "{usuario}": {(filmes)}')
         else:
            print(f'Nenhum filme encontrado para o usuário "{usuario}".')

      case '4':
         if usuario_filmes:
            print('Usuários e seus filmes:')
            for usuario, filmes in usuario_filmes.items():
               print(f'{usuario}: {filmes}')
         else:
            print('Nenhum usuário cadastrado.')

      case '0':
         print('Saindo do programa')
         break
      
      case _:
         print('Opção inválida, refaça a escolha.')