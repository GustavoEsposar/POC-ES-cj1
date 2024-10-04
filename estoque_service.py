from flask import Flask, request, jsonify
from services.estoque_logic import verificar_disponibilidade

app = Flask(__name__)

# Simula um estoque como um banco de dados sintético
estoque = {
    "item1": {"quantidade": 10},
    "item2": {"quantidade": 5},
    "item3": {"quantidade": 15}
}

@app.route('/verificar_estoque', methods=['POST'])
def verificar_estoque():
    resumo = request.json  

    produtos_disponiveis = verificar_disponibilidade(estoque, resumo["itens"])
    if produtos_disponiveis == True:
        return jsonify({"status": "disponível"}), 200
    elif produtos_disponiveis == False:
        return jsonify({"status": "indisponível"}), 200
    else:
        return jsonify({"erro": "Erro ao verificar estoque"}), 500

if __name__ == '__main__':
    app.run(port=5001, debug=True)
