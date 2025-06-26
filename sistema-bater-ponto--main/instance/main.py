from flask import Flask, jsonify, request
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = "sqlite:///dados.db"
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False  
db = SQLAlchemy()
db.init_app(app)


class Funcionario(db.Model):
    __tablename__ = 'funcionarios'

    id = db.Column(db.Integer, primary_key=True)
    nome = db.Column(db.String(100), nullable=False, unique=True)
    tipo = db.Column(db.String(50), nullable=False)  
    bateu_ponto = db.Column(db.Boolean, default=False)  
    justificativa = db.Column(db.String(255), nullable=True)  

    def __repr__(self):
        return f"<Funcionario {self.nome}>"


@app.route('/Login')
def login():
    return "Tela de login"


@app.route('/funcionarios', methods=['GET'])
def listar_funcionarios():
    funcionarios = Funcionario.query.all()
    return jsonify([{
        'id': f.id,
        'nome': f.nome,
        'tipo': f.tipo,
        'bateu_ponto': f.bateu_ponto,
        'justificativa': f.justificativa
    } for f in funcionarios])


@app.route('/funcionario', methods=['POST'])
def adicionar_funcionario():
    data = request.get_json()


    nome = data.get('nome')
    tipo = data.get('tipo')
    bateu_ponto = data.get('bateu_ponto', False)
    justificativa = data.get('justificativa', '')

    if not nome or not tipo:
        return jsonify({"error": "Nome e tipo são obrigatórios!"}), 400

    if tipo not in ["administrador", "funcionario"]:
        return jsonify({"error": "Tipo inválido. Deve ser 'administrador' ou 'funcionario'."}), 400

    funcionario = Funcionario(
        nome=nome,
        tipo=tipo,
        bateu_ponto=bateu_ponto,
        justificativa=justificativa
    )

    db.session.add(funcionario)
    db.session.commit()

    return jsonify({"message": f"Funcionário {nome} adicionado com sucesso!"}), 201

@app.route('/funcionario/<int:id>', methods=['GET'])
def verificar_funcionario(id):
    funcionario = Funcionario.query.get_or_404(id)
    return jsonify({
        'id': funcionario.id,
        'nome': funcionario.nome,
        'tipo': funcionario.tipo,
        'bateu_ponto': funcionario.bateu_ponto,
        'justificativa': funcionario.justificativa
    })

@app.before_first_request
def cria_banco():
    db.create_all()  

if __name__ == '__main__':
    app.run(debug=True)
