print ("Ola mundo")

from datetime import datetime

listaEventos = []

print("Bem-vindo ao sistema de gerenciamento de eventos BFD!")

def validacaoData(dataStr):
    try:
        datetime.strptime(dataStr, "%d/%m/%Y")
        return True
    except ValueError:
        return False

def adicionarEvento(listaEventos, nome, data, local, categoria):
    if listaEventos == "" or nome == "" or data == "" or local == "" or categoria == "":
        print("Erro: Todos os campos devem ser preenchidos.")
        return False
    if not validacaoData(data):
        print("Erro: Data inválida. Use o formato DD/MM/AAAA.")
        return False
    for criacaoEvento in listaEventos:
        if criacaoEvento["nome"] == nome:
            print("Erro: Já existe um evento com esse nome.")
            return False
    novoEvento = {
        "nome": nome,
        "data": data,
        "local": local,
        "categoria": categoria
    }
    listaEventos.append(novoEvento)
    print(f"Evento '{nome}' adicionado com sucesso!")
    return True
def ListarEventos(listaEventos):
    print("Lista de Eventos:")
    if not listaEventos:
        print("Nenhum evento cadastrado.")
    else:
        for evento in listaEventos:
            print(f"{evento['nome']}")
            print(f"Data: {evento['data']}")
            print(f"Local: {evento['local']}")
            print(f"Categoria: {evento['categoria']}")
            print("-" * 20)
def buscarEvento(listaEventos, nome):
    print(f"Buscando eventos com o nome '{nome}':")
    eventosEncontrados = False
    for evento in listaEventos:
        if nome.lower() in evento['nome'].lower():
            print(f"{evento['nome']} - {evento['data']} - {evento['local']} - {evento['categoria']}")
            eventosEncontrados = True
    if not eventosEncontrados:
        print(f"Nenhum evento encontrado com o nome '{nome}'.")
        print("-" * 20)
def removerEvento(listaEventos, nomeDeletar):
    indiceRemover = None
    for indice, evento in enumerate(listaEventos):
        if evento['nome'].lower() == nomeDeletar.lower():
            indiceRemover = indice
            break
    if indiceRemover is not None:
        del listaEventos[indiceRemover]
        print(f"Evento '{nomeDeletar}' removido com sucesso!")
    else:
        print(f"Nenhum evento encontrado com o nome '{nomeDeletar}'.")
