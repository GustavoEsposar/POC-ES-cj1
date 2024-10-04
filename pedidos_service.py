from flask import Flask, request, jsonify
import requests
from services.pedidos_logic import calcular_resumo_do_carrinho, buscar_endereco_usuario

app = Flask(__name__)

# Simula endereços de usuários'
enderecos_usuarios = {
    1: [{"rua": "Rua A", "cidade": "Cidade X", "cep": "12345-000"}],
    2: [{"rua": "Rua C", "cidade": "Cidade Z", "cep": "67890-000"}]
}

@app.route('/checkout/carrinho', methods=['POST'])
def checkout_carrinho():
    try:
        # Obtém o corpo da requisição JSON (carrinho)
        carrinho = request.json

        # Envia apenas a lista de itens para o serviço de estoque
        itens_para_verificar = {"itens": carrinho["itens"]}
        response = requests.post(f'http://localhost:5001/verificar_estoque', json=itens_para_verificar)
        response.raise_for_status()

        # Busca o endereço do usuário com base no user_id fornecido
        user_id = carrinho.get("user_id")
        enderecos = buscar_endereco_usuario(user_id, enderecos_usuarios)

        if response.json()["status"] == "indisponível":
            return jsonify({"erro": "Item(s) indisponível(is)"}), 400
        else:
            resumo = calcular_resumo_do_carrinho(carrinho)
            return jsonify({"resumo_pedido": resumo, "endereco": enderecos}), 200

    except requests.exceptions.RequestException as e:
        return jsonify({"erro": "Erro ao consultar o serviço de estoque"}), 500

    except ValueError as e:
        return jsonify({"erro": str(e)}), 400

if __name__ == '__main__':
    app.run(port=5000, debug=True)

