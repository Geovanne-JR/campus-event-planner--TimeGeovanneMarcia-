from typing import List, Dict, Any
from datetime import datetime

Event = Dict[str, Any]

print("\nBem-vindo ao sistema de gerenciamento de eventos BFD!")

def validarData(data_str: str) -> bool:
    try:
        datetime.strptime(data_str, "%d/%m/%Y")
        return True
    except ValueError:
        return False

def addEvent(lista_eventos: List[Event], nome: str, data: str, local: str, categoria: str):
    if not nome.strip() or not data.strip() or not local.strip() or not categoria.strip():
        print("❌ Erro: Todos os campos (nome, data, local, categoria) são obrigatórios.")
        return

    if not validarData(data):
        print("❌ Erro: Data inválida. Use o formato DD/MM/AAAA (exemplo: 11/10/2025).")
        return
    else:
        data_formatada = datetime.strptime(data, "%d/%m/%Y").strftime("%d/%m/%Y")

    novo_id = max([ev.get("id", 0) for ev in lista_eventos], default=0) + 1

    evento = {
        "id": novo_id,
        "nome": nome.strip(),
        "data": data_formatada,
        "local": local.strip(),
        "categoria": categoria.strip(),
        "participado": False
    }

    lista_eventos.append(evento)
    print(f"✅ Evento '{nome}' (ID: {novo_id}) adicionado com sucesso!")

def displayEvents(lista_eventos: List[Event]):
    print("\n--- LISTA DE EVENTOS ---")
    if not lista_eventos:
        print("Nenhum evento cadastrado.")
    else:
        for ev in lista_eventos:
            status = "✔️ Participado" if ev.get('participado', False) else "❌ Pendente"
            print(f"  ID: {ev.get('id', 'N/A')} | Nome: {ev.get('nome', 'N/A')}")
            print(f"  Data: {ev.get('data', 'N/A')} | Local: {ev.get('local', 'N/A')}")
            print(f"  Categoria: {ev.get('categoria', 'N/A')} | Status: {status}")
            print("-" * 25)

def procurarEvento(listEventos: List[Event], termo_busca: str) -> List[Event]:
    termo = termo_busca.strip().lower()
    resultados = [
        ev for ev in listEventos
        if termo in ev.get("nome", "").lower()
    ]
    return resultados

def deleteEvento(lista_eventos: List[Event], id_evento: int) -> bool:
    for i, ev in enumerate(lista_eventos):
        if ev.get("id") == id_evento:
            del lista_eventos[i]
            return True
    return False

def filtrarPorCategoria(eventos: List[Event], categoria: str):
    categoria_lower = categoria.strip().lower()
    filtrados = [e for e in eventos if e.get("categoria", "").lower() == categoria_lower]
    
    print(f"\n--- EVENTOS NA CATEGORIA: {categoria} ---")
    if not filtrados:
        print("Nenhum evento nessa categoria.")
    else:
        for e in filtrados:
            status = "✔️" if e.get("participado", False) else "❌"
            print(f"ID: {e['id']}. {e['nome']} ({e['data']}) {status}")
    print("-" * 30)

def marcarEvento(eventos: List[Event], id_evento: int):
    encontrado = False
    for e in eventos:
        if e.get("id") == id_evento:
            e["participado"] = True
            print(f"Evento ID {id_evento} ('{e['nome']}') marcado como **participado**!")
            encontrado = True
            break
            
    if not encontrado:
        print(f"Erro: Evento com ID {id_evento} não encontrado.")

def gerarRelatorio(eventos: List[Event]):
    if not eventos:
        print("\nNenhum evento para relatar.")
        return
        
    total = len(eventos)
    participados = sum(1 for e in eventos if e.get("participado", False))
    categorias = {}
    
    for e in eventos:
        cat = e.get("categoria", "Sem Categoria")
        categorias[cat] = categorias.get(cat, 0) + 1
        
    print("\n===== RELATÓRIO DE EVENTOS =====")
    print(f"Total de Eventos: {total}")
    
    if total > 0:
        print(f"Eventos Participados: {participados} ({participados/total*100:.1f}%)")
    else:
        print("Eventos Participados: 0 (0.0%)")
    
    print("\n--- Contagem por Categoria ---")
    for c, q in categorias.items():
        print(f"  {c}: {q}")
    print("-" * 30)

def displayMenu():
    print("\n===== GESTOR DE EVENTOS =====")
    print("1. Adicionar novo evento")
    print("2. Visualizar todos os eventos")
    print("3. Procurar evento por nome")
    print("4. Marcar evento como participado")
    print("5. Filtrar por categoria")
    print("6. Gerar relatório")
    print("7. Deletar evento por ID")
    print("0. Sair")

def getEscolhaDoUsuario():
    try:
        return int(input("Escolha uma opção: "))
    except ValueError:
        return -1

def main():
    eventos: List[Event] = []
    
    while True:
        displayMenu()
        op = getEscolhaDoUsuario()

        if op == 1:
            nome = input("Nome do evento: ")
            data = input("Data (DD/MM/AAAA): ")
            local = input("Local: ")
            categoria = input("Categoria: ")
            addEvent(eventos, nome, data, local, categoria)
            
        elif op == 2:
            displayEvents(eventos)
            
        elif op == 3:
            termo = input("Digite o nome ou parte do nome para buscar: ")
            resultados = procurarEvento(eventos, termo)
            if resultados:
                print(f"\n--- Resultados da Busca por '{termo}' ---")
                for e in resultados:
                    status = "✔️" if e.get("participado", False) else "❌"
                    print(f"ID: {e['id']}. {e['nome']} ({e['data']}) - {e['categoria']} {status}")
                print("-" * 40)
            else:
                print("Nenhum evento encontrado.")

        elif op == 4:
            try:
                id_marcar = int(input("Digite o ID do evento para marcar como participado: "))
                marcarEvento(eventos, id_marcar)
            except ValueError:
                print("ID inválido. Por favor, insira um número inteiro.")
                
        elif op == 5:
            categoria_filtro = input("Digite a categoria para filtrar: ")
            filtrarPorCategoria(eventos, categoria_filtro)
            
        elif op == 6:
            gerarRelatorio(eventos)
            
        elif op == 7:
            try:
                id_deletar = int(input("Digite o ID do evento para deletar: "))
                if deleteEvento(eventos, id_deletar):
                    print(f"Evento ID {id_deletar} deletado com sucesso.")
                else:
                    print(f"Erro: Evento com ID {id_deletar} não encontrado.")
            except ValueError:
                print("ID inválido. Por favor, insira um número inteiro.")

        elif op == 0:
            print("Saindo do Gestor de Eventos. Até logo!")
            break
            
        else:
            print("Opção inválida. Tente novamente.")

if __name__ == "__main__":
    main()
