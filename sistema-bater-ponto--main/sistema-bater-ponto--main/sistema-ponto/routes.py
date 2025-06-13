from flask import Flask, request, render_template

# Criando a aplicação flask
app = Flask(__name__)


# Definindo uma rota básica que responde a requisições GET
@app.route('/Login')
def root():
    return render_template ('login.html')


@app.route('/submit', methods=['GET', 'POST'])
def submit():
    if request.method == 'POST':
        usuario = request.form.get('usuario')
        senha = request.form.get('senha')
        data = request.form['name']
        return f'Você enviou :{data}'
        
        # Validação de login
        return render_template('inicial.html', usuario=usuario)
    return'''
        <form method="POST">
            Usuário: <input type="text" name="usuario"><br>
            Senha: <input type="password" name="senha"><br>
            <button type="submit">Entrar</button>
        </form>
    '''

#Executando o servidor
if __name__ == '__main__':
    app.run(debug=True, port=5152)