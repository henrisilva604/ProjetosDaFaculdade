class Evento:
    def __init__(self, nome, data, descricao, vagas_max):
        self.nome = nome
        self.data = data
        self.descricao = descricao
        self.vagas_max = vagas_max
        self.inscritos = []

    def vagas_restantes(self):
        return self.vagas_max - len(self.inscritos)

    def atualizar(self, nome=None, data=None, descricao=None, vagas_max=None):
        if nome:
            self.nome = nome
        if data:
            self.data = data
        if descricao:
            self.descricao = descricao
        if vagas_max is not None:
            # Atualizar vagas_max, mas só se for maior que inscritos atuais
            if vagas_max >= len(self.inscritos):
                self.vagas_max = vagas_max
            else:
                print("Não pode reduzir vagas abaixo do número de inscritos.")

    def inscrever(self, aluno):
        if self.vagas_restantes() > 0:
            self.inscritos.append(aluno)
            print(f"{aluno} inscrito no evento {self.nome}.")
        else:
            print(f"Não há vagas disponíveis para o evento {self.nome}.")

    def listar_inscritos(self):
        return self.inscritos

class SistemaEventos:
    def __init__(self):
        self.eventos = {}

    def cadastrar_evento(self, nome, data, descricao, vagas_max):
        if nome in self.eventos:
            print("Evento já cadastrado.")
            return
        evento = Evento(nome, data, descricao, vagas_max)
        self.eventos[nome] = evento
        print(f"Evento '{nome}' cadastrado com sucesso.")

    def atualizar_evento(self, nome, **kwargs):
        if nome not in self.eventos:
            print("Evento não encontrado.")
            return
        self.eventos[nome].atualizar(**kwargs)
        print(f"Evento '{nome}' atualizado.")

    def listar_eventos(self):
        if not self.eventos:
            print("Nenhum evento disponível.")
            return
        for evento in self.eventos.values():
            print(f"Nome: {evento.nome}")
            print(f"Data: {evento.data}")
            print(f"Descrição: {evento.descricao}")
            print(f"Vagas restantes: {evento.vagas_restantes()}")
            print("-" * 30)

    def inscrever_aluno(self, nome_evento, aluno):
        if nome_evento not in self.eventos:
            print("Evento não encontrado.")
            return
        self.eventos[nome_evento].inscrever(aluno)

    def listar_inscritos(self, nome_evento):
        if nome_evento not in self.eventos:
            print("Evento não encontrado.")
            return
        inscritos = self.eventos[nome_evento].listar_inscritos()
        if inscritos:
            print(f"Inscritos no evento '{nome_evento}':")
            for aluno in inscritos:
                print(f"- {aluno}")
        else:
            print("Nenhum inscrito ainda.")

    def excluir_evento(self, nome):
        if nome in self.eventos:
            del self.eventos[nome]
            print(f"Evento '{nome}' excluído.")
        else:
            print("Evento não encontrado.")


