import sys
import os

# Adiciona o diretório raiz do projeto ao sys.path
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from flask import Flask, request, jsonify
from lib.numbers import Numbers

app = Flask(__name__)


@app.route('/somar', methods=['POST'])
def somar():
    try:
        data = request.get_json()
        numeros = data.get('numeros', [])

        if not isinstance(numeros, list):
            return jsonify({"erro": "O campo 'numeros' deve ser uma lista."}), 400

        if not all(isinstance(num, int) for num in numeros):
            return jsonify({"erro": "Todos os elementos da lista devem ser inteiros."}), 400

        numbers = Numbers(numeros)
        resultado = numbers.sum()
        return jsonify({"resultado": resultado}), 200
    except Exception as e:
        return jsonify({"erro": str(e)}), 500


@app.route('/media', methods=['POST'])
def media():
    try:
        data = request.get_json()
        numeros = data.get('numeros', [])

        if not isinstance(numeros, list):
            return jsonify({"erro": "O campo 'numeros' deve ser uma lista."}), 400

        if not all(isinstance(num, int) for num in numeros):
            return jsonify({"erro": "Todos os elementos da lista devem ser inteiros."}), 400

        numbers = Numbers(numeros)
        resultado = numbers.average()
        return jsonify({"resultado": resultado}), 200
    except ValueError as e:
        return jsonify({"erro": str(e)}), 400
    except Exception as e:
        return jsonify({"erro": str(e)}), 500


if __name__ == '__main__':
    app.run(debug=True)