from app.banco import sessoes

def listar_sessoes():  #retorna uma lista com as informações de cada sessão

    sessoes_info = []

    for sessao in sessoes:
        assentos_vagos = contar_assentos_vagos_da_sessao(sessao)

        sessoes_info.append({
            "id_sessao": sessao["id_sessao"],
            "titulo_filme": sessao["titulo_filme"],
            "sala": sessao["sala"],
            "horario": sessao["horario"],
            "assentos_vagos": assentos_vagos,
            "total_assentos": len(sessao["assentos"]),
        })

    return sessoes_info


def buscar_sessao_por_id(id_sessao: int):   # Busca e retorna a sessão do id selecionado e retorna None se não achar

    for sessao in sessoes:
        if sessao["id_sessao"] == id_sessao:
            return sessao

    return None


def contar_assentos_vagos_da_sessao(sessao):  # contador simples de assentos disponíveis da sessao 

    quantidade = 0

    for assento in sessao["assentos"]:
        if assento["disponivel"]:
            quantidade += 1

    return quantidade


def listar_assentos_vagos(id_sessao: int):  # Retorna quais assentos estão disponíveis para a sessão com id selecionado

    sessao = buscar_sessao_por_id(id_sessao)     # Chama a função para selecionar a sessao escolhida

    if sessao is None:
        return None

    assentos_vagos = []

    for assento in sessao["assentos"]:
        if assento["disponivel"]:
            assentos_vagos.append(assento["id"])

    return assentos_vagos

def reservar_assento(id_sessao: int, id_assento: str):    # Função para reservar o assento escolhido da sessao selecionada 
    
    sessao = buscar_sessao_por_id(id_sessao)

    if sessao is None:
        return "sessao_inexistente"

    for assento in sessao["assentos"]:
        if assento["id"].strip().upper() == id_assento.strip().upper():
            if assento["disponivel"]:
                assento["disponivel"] = False
                return "sucesso"
            else:
                return "assento_ocupado"

    return "assento_inexistente"
    