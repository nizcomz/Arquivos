from flask import Flask, render_template, request, jsonify
from datetime import datetime

app = Flask(__name__)

# Página Principal
@app.route("/")
def home():
    return render_template("index.html")

# Rota para processar formulário (AJAX)
@app.route("/api/processar-formulario", methods=["POST"])
def processar_formulario():
    data = request.get_json()
    nome = data.get("nome", "Visitante")
    email = data.get("email", "não informado")
    mensagem = data.get("mensagem", "sem mensagem")
    
    # Retorna resposta 
    resposta = {
        "sucesso": True,
        "mensagem": f"Obrigado {nome}! Sua mensagem foi recebida.",
        "timestamp": datetime.now().strftime("%H:%M:%S"),
        "dados_recebidos": {
            "nome": nome,
            "email": email,
            "mensagem": mensagem
        }
    }
    return jsonify(resposta)

# Rota para calcular (exemplo de API)
@app.route("/api/calcular", methods=["POST"])
def calcular():
    data = request.get_json()
    numero1 = float(data.get("numero1", 0))
    numero2 = float(data.get("numero2", 0))
    operacao = data.get("operacao", "soma")
    
    if operacao == "soma":
        resultado = numero1 + numero2
    elif operacao == "subtracao":
        resultado = numero1 - numero2
    elif operacao == "multiplicacao":
        resultado = numero1 * numero2
    elif operacao == "divisao":
        resultado = numero1 / numero2 if numero2 != 0 else "Erro: divisão por zero"
    else:
        resultado = "Operação inválida"
    
    return jsonify({
        "resultado": resultado,
        "operacao": operacao,
        "numero1": numero1,
        "numero2": numero2
    })

if __name__ == "__main__":
    app.run(debug=True)