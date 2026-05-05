eventos = []
inscricoes = {}

def cadastrar_evento():
    print("\n--- Cadastrar Novo Evento ---")
    nome = input("Nome do evento: ")
    data = input("Data do evento (DD/MM/AAAA): ")
    descricao = input("Descrição do evento: ")
    max_participantes = int(input("Número máximo de participantes: "))
    
    evento = {
        'id': len(eventos) + 1,
        'nome': nome,
        'data': data,
        'descricao': descricao,
        'max_participantes': max_participantes,
        'participantes': 0
    }
    
    eventos.append(evento)
    inscricoes[evento['id']] = []
    print(f"Evento '{nome}' cadastrado com sucesso!")

def atualizar_evento():
    print("\n--- Atualizar Evento ---")
    if not eventos:
        print("Não há eventos cadastrados.")
        return
    
    listar_eventos()
    try:
        id_evento = int(input("ID do evento a ser atualizado: ")) - 1
        
        if 0 <= id_evento < len(eventos):
            evento = eventos[id_evento]
            print(f"\nEditando evento: {evento['nome']}")
            print("Deixe em branco para manter o valor atual.")
            
            novo_nome = input(f"Nome [{evento['nome']}]: ") or evento['nome']
            nova_data = input(f"Data [{evento['data']}]: ") or evento['data']
            nova_desc = input(f"Descrição [{evento['descricao']}]: ") or evento['descricao']
            
            # Verifica se o novo máximo é maior ou igual ao número atual de participantes
            while True:
                try:
                    novo_max = input(f"Máximo de participantes [{evento['max_participantes']}]: ")
                    novo_max = int(novo_max) if novo_max else evento['max_participantes']
                    
                    if novo_max >= evento['participantes']:
                        break
                    else:
                        print(f"Erro: O novo máximo ({novo_max}) deve ser maior ou igual ao número atual de participantes ({evento['participantes']})")
                except ValueError:
                    print("Por favor, digite um número válido.")
            
            # Atualiza os dados do evento
            evento['nome'] = novo_nome
            evento['data'] = nova_data
            evento['descricao'] = nova_desc
            evento['max_participantes'] = novo_max
            
            print("Evento atualizado com sucesso!")
        else:
            print("ID inválido.")
    except ValueError:
        print("Por favor, digite um ID válido.")

def listar_eventos():
    print("\n--- Eventos Disponíveis ---")
    if not eventos:
        print("Nenhum evento cadastrado.")
        return
    
    for evento in eventos:
        vagas_restantes = evento['max_participantes'] - evento['participantes']
        print(f"\nID: {evento['id']}")
        print(f"Nome: {evento['nome']}")
        print(f"Data: {evento['data']}")
        print(f"Descrição: {evento['descricao']}")
        print(f"Vagas disponíveis: {vagas_restantes}/{evento['max_participantes']}")

def inscrever_aluno():
    print("\n--- Inscrever Aluno em Evento ---")
    if not eventos:
        print("Nenhum evento disponível para inscrição.")
        return
    
    listar_eventos()
    try:
        id_evento = int(input("ID do evento para inscrição: ")) - 1
        
        if 0 <= id_evento < len(eventos):
            evento = eventos[id_evento]
            
            if evento['participantes'] < evento['max_participantes']:
                nome_aluno = input("Nome do aluno: ")
                email_aluno = input("Email do aluno: ")
                
                # Adiciona aluno à lista de inscrições
                inscricoes[evento['id']].append({'nome': nome_aluno, 'email': email_aluno})
                # Atualiza contador de participantes
                evento['participantes'] += 1
                
                print(f"{nome_aluno} inscrito(a) no evento {evento['nome']} com sucesso!")
            else:
                print("Desculpe, não há vagas disponíveis para este evento.")
        else:
            print("ID inválido.")
    except ValueError:
        print("Por favor, digite um ID válido.")

def listar_inscritos():
    print("\n--- Listar Inscritos em Evento ---")
    if not eventos:
        print("Nenhum evento cadastrado.")
        return
    
    listar_eventos()
    try:
        id_evento = int(input("ID do evento para listar inscritos: ")) - 1
        
        if 0 <= id_evento < len(eventos):
            evento = eventos[id_evento]
            lista_inscritos = inscricoes[evento['id']]
            
            print(f"\nInscritos no evento '{evento['nome']}':")
            if not lista_inscritos:
                print("Nenhum inscrito ainda.")
            else:
                for i, aluno in enumerate(lista_inscritos, 1):
                    print(f"{i}. {aluno['nome']} - {aluno['email']}")
        else:
            print("ID inválido.")
    except ValueError:
        print("Por favor, digite um ID válido.")

def excluir_evento():
    print("\n--- Excluir Evento ---")
    if not eventos:
        print("Não há eventos cadastrados.")
        return
    
    listar_eventos()
    try:
        id_evento = int(input("ID do evento a ser excluído: ")) - 1
        
        if 0 <= id_evento < len(eventos):
            evento = eventos[id_evento]
            confirmacao = input(f"Tem certeza que deseja excluir o evento '{evento['nome']}'? (S/N): ").upper()
            
            if confirmacao == 'S':
                # Remove o evento e suas inscrições
                eventos.pop(id_evento)
                inscricoes.pop(evento['id'])
                
                # Atualiza IDs dos eventos restantes
                for i, ev in enumerate(eventos, 1):
                    ev['id'] = i
                
                print("Evento excluído com sucesso!")
            else:
                print("Operação cancelada.")
        else:
            print("ID inválido.")
    except ValueError:
        print("Por favor, digite um ID válido.")

def menu_principal():
    while True:
        print("\n=== Sistema de Gerenciamento de Eventos - UniFECAF ===")
        print("1. Cadastrar novo evento")
        print("2. Atualizar evento existente")
        print("3. Listar eventos disponíveis")
        print("4. Inscrever aluno em evento")
        print("5. Listar inscritos em evento")
        print("6. Excluir evento")
        print("0. Sair do sistema")
        
        opcao = input("\nEscolha uma opção: ")
        
        if opcao == '1':
            cadastrar_evento()
        elif opcao == '2':
            atualizar_evento()
        elif opcao == '3':
            listar_eventos()
        elif opcao == '4':
            inscrever_aluno()
        elif opcao == '5':
            listar_inscritos()
        elif opcao == '6':
            excluir_evento()
        elif opcao == '0':
            print("Saindo do sistema...")
            break
        else:
            print("Opção inválida. Por favor, tente novamente.")

menu_principal()