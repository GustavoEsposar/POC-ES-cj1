
def calcular_resumo_do_carrinho(carrinho):
    if not isinstance(carrinho, dict) or 'itens' not in carrinho:
        raise ValueError("Formato do carrinho inválido")
    
    total = sum(item["preco"] * item["quantidade"] for item in carrinho["itens"])
    return {"itens": carrinho["itens"], "total": total}


def buscar_endereco_usuario(user_id, enderecos_usuarios):
    if user_id not in enderecos_usuarios:
        raise ValueError(f"Usuário com ID {user_id} não encontrado")
    
    return enderecos_usuarios[user_id]
