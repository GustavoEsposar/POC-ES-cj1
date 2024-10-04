
def verificar_disponibilidade(estoque, itens):
    for item in itens:
        nome_item = item["nome"]
        quantidade_requerida = item["quantidade"]
        if nome_item not in estoque or estoque[nome_item]["quantidade"] < quantidade_requerida:
            return False
    return True
