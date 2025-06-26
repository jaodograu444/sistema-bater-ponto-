from flask import Blueprint, request, render_template, redirect, url_for, flash, session, jsonify
from datetime import datetime, date, time
from models import db, Usuario, Ponto, Justificativa, Horario

routes = Blueprint('routes', __name__)

# Decorators

def login_required(f):
    def decorated_function(*args, **kwargs):
        if 'user_id' not in session:
            return redirect(url_for('routes.login'))
        return f(*args, **kwargs)
    decorated_function.__name__ = f.__name__
    return decorated_function

def admin_required(f):
    def decorated_function(*args, **kwargs):
        if 'user_id' not in session:
            return redirect(url_for('routes.login'))
        user = Usuario.query.get(session['user_id'])
        if not user or user.tipo != 'admin':
            flash('Acesso negado! Apenas administradores podem acessar esta página.')
            return redirect(url_for('routes.login'))
        return f(*args, **kwargs)
    decorated_function.__name__ = f.__name__
    return decorated_function

# ============= ROTAS DE AUTENTICAÇÃO =============

@routes.route('/')
def login():
    return render_template('login.html')

@routes.route('/login', methods=['POST'])
def fazer_login():
    username = request.form.get('usuario')
    password = request.form.get('senha')
    user = Usuario.query.filter_by(username=username).first()
    if user and user.check_password(password) and user.ativo:
        session['user_id'] = user.id
        session['user_type'] = user.tipo
        session['user_name'] = user.nome
        if user.tipo == 'admin':
            return redirect(url_for('routes.escolha_admin'))
        else:
            return redirect(url_for('routes.inicial_funcionario'))
    else:
        flash('Usuário ou senha inválidos!')
        return redirect(url_for('routes.login'))

@routes.route('/logout')
def logout():
    session.clear()
    flash('Logout realizado com sucesso!')
    return redirect(url_for('routes.login'))

# ============= ROTAS ADMINISTRADOR =============

@routes.route('/escolha-admin')
@admin_required
def escolha_admin():
    return render_template('sistemaAdministrador/escolha-admin/escolha.html')

@routes.route('/inicial-admin')
@admin_required
def inicial_admin():
    return render_template('sistemaAdministrador/tela-inicial-admin/inicial-admin.html')

@routes.route('/cadastrar-funcionario')
@admin_required
def cadastrar_funcionario():
    return render_template('sistemaAdministrador/cadastrar-funcionario/usuario.html')

@routes.route('/cadastrar-funcionario', methods=['POST'])
@admin_required
def salvar_funcionario():
    nome = request.form.get('nome')
    username = request.form.get('username')
    email = request.form.get('email')
    password = request.form.get('password')
    tipo = request.form.get('tipo', 'funcionario')
    if Usuario.query.filter_by(username=username).first():
        flash('Nome de usuário já existe!')
        return redirect(url_for('routes.cadastrar_funcionario'))
    if Usuario.query.filter_by(email=email).first():
        flash('E-mail já cadastrado!')
        return redirect(url_for('routes.cadastrar_funcionario'))
    novo_usuario = Usuario(
        nome=nome,
        username=username,
        email=email,
        tipo=tipo
    )
    novo_usuario.set_password(password)
    db.session.add(novo_usuario)
    db.session.commit()
    flash('Funcionário cadastrado com sucesso!')
    return redirect(url_for('routes.inicial_admin'))

@routes.route('/bater-ponto-admin')
@admin_required
def bater_ponto_admin():
    funcionarios = Usuario.query.filter_by(tipo='funcionario', ativo=True).all()
    return render_template('sistemaAdministrador/tela-bater-ponto/baterpontoADM.html', funcionarios=funcionarios)

@routes.route('/justificativas-admin')
@admin_required
def justificativas_admin():
    justificativas = Justificativa.query.filter_by(status='pendente').all()
    return render_template('sistemaAdministrador/justificativas-admin/justificativasAD.html', justificativas=justificativas)

@routes.route('/listar-justificativas')
@admin_required
def listar_justificativas():
    justificativas = Justificativa.query.all()
    return render_template('sistemaAdministrador/tela-listar-justificaivas/listar-justificativas.html', justificativas=justificativas)

@routes.route('/cadastrar-horario')
@admin_required
def cadastrar_horario():
    funcionarios = Usuario.query.filter_by(tipo='funcionario', ativo=True).all()
    return render_template('sistemaAdministrador/tela-cadastrarHorario/cadastrarHorario.html', funcionarios=funcionarios)

@routes.route('/cadastrar-horario', methods=['POST'])
@admin_required
def salvar_horario():
    usuario_id = request.form.get('usuario_id')
    dia_semana = request.form.get('dia_semana')
    hora_entrada = request.form.get('hora_entrada')
    hora_saida = request.form.get('hora_saida')
    hora_almoco_inicio = request.form.get('hora_almoco_inicio')
    hora_almoco_fim = request.form.get('hora_almoco_fim')
    hora_entrada_obj = datetime.strptime(hora_entrada, '%H:%M').time()
    hora_saida_obj = datetime.strptime(hora_saida, '%H:%M').time()
    hora_almoco_inicio_obj = datetime.strptime(hora_almoco_inicio, '%H:%M').time() if hora_almoco_inicio else None
    hora_almoco_fim_obj = datetime.strptime(hora_almoco_fim, '%H:%M').time() if hora_almoco_fim else None
    horario_existente = Horario.query.filter_by(usuario_id=usuario_id, dia_semana=dia_semana, ativo=True).first()
    if horario_existente:
        horario_existente.hora_entrada = hora_entrada_obj
        horario_existente.hora_saida = hora_saida_obj
        horario_existente.hora_almoco_inicio = hora_almoco_inicio_obj
        horario_existente.hora_almoco_fim = hora_almoco_fim_obj
    else:
        novo_horario = Horario(
            usuario_id=usuario_id,
            dia_semana=dia_semana,
            hora_entrada=hora_entrada_obj,
            hora_saida=hora_saida_obj,
            hora_almoco_inicio=hora_almoco_inicio_obj,
            hora_almoco_fim=hora_almoco_fim_obj
        )
        db.session.add(novo_horario)
    db.session.commit()
    flash('Horário cadastrado com sucesso!')
    return redirect(url_for('routes.cadastrar_horario'))

# ============= ROTAS FUNCIONÁRIO =============

@routes.route('/inicial-funcionario')
@login_required
def inicial_funcionario():
    return render_template('sistemaFuncionario/tela-inicial-funcionario/inicial.html')

@routes.route('/bater-ponto')
@login_required
def bater_ponto_funcionario():
    usuario_id = session['user_id']
    hoje = date.today()
    ponto_hoje = Ponto.query.filter_by(usuario_id=usuario_id, data=hoje).first()
    return render_template('sistemaFuncionario/tela-bater-ponto/baterponto.html', ponto=ponto_hoje)

@routes.route('/registrar-ponto', methods=['POST'])
@login_required
def registrar_ponto():
    usuario_id = session['user_id']
    tipo_ponto = request.form.get('tipo_ponto')
    hoje = date.today()
    agora = datetime.now().time()
    ponto = Ponto.query.filter_by(usuario_id=usuario_id, data=hoje).first()
    if not ponto:
        ponto = Ponto(usuario_id=usuario_id, data=hoje)
        db.session.add(ponto)
    if tipo_ponto == 'entrada':
        ponto.hora_entrada = agora
    elif tipo_ponto == 'almoco_saida':
        ponto.hora_almoco_saida = agora
    elif tipo_ponto == 'almoco_volta':
        ponto.hora_almoco_volta = agora
    elif tipo_ponto == 'saida':
        ponto.hora_saida = agora
    db.session.commit()
    flash(f'Ponto de {tipo_ponto} registrado com sucesso!')
    return redirect(url_for('routes.bater_ponto_funcionario'))

@routes.route('/justificativa')
@login_required
def justificativa_funcionario():
    return render_template('sistemaFuncionario/tela-justificativa/justificativaF.html')

@routes.route('/justificativa', methods=['POST'])
@login_required
def salvar_justificativa():
    usuario_id = session['user_id']
    data_str = request.form.get('data')
    motivo = request.form.get('motivo')
    descricao = request.form.get('descricao')
    data_obj = datetime.strptime(data_str, '%Y-%m-%d').date()
    nova_justificativa = Justificativa(
        usuario_id=usuario_id,
        data=data_obj,
        motivo=motivo,
        descricao=descricao
    )
    db.session.add(nova_justificativa)
    db.session.commit()
    flash('Justificativa enviada com sucesso!')
    return redirect(url_for('routes.inicial_funcionario'))

# ============= API ROUTES =============

@routes.route('/api/aprovar-justificativa/<int:justificativa_id>', methods=['POST'])
@admin_required
def aprovar_justificativa(justificativa_id):
    justificativa = Justificativa.query.get_or_404(justificativa_id)
    justificativa.status = 'aprovada'
    justificativa.aprovado_por = session['user_id']
    justificativa.data_aprovacao = datetime.utcnow()
    db.session.commit()
    return jsonify({'success': True, 'message': 'Justificativa aprovada!'})

@routes.route('/api/rejeitar-justificativa/<int:justificativa_id>', methods=['POST'])
@admin_required
def rejeitar_justificativa(justificativa_id):
    justificativa = Justificativa.query.get_or_404(justificativa_id)
    justificativa.status = 'rejeitada'
    justificativa.aprovado_por = session['user_id']
    justificativa.data_aprovacao = datetime.utcnow()
    db.session.commit()
    return jsonify({'success': True, 'message': 'Justificativa rejeitada!'})

@routes.route('/api/funcionarios')
@admin_required
def api_funcionarios():
    funcionarios = Usuario.query.filter_by(tipo='funcionario', ativo=True).all()
    return jsonify([{
        'id': f.id,
        'nome': f.nome,
        'username': f.username,
        'email': f.email
    } for f in funcionarios])

@routes.route('/api/pontos/<int:usuario_id>')
@admin_required
def api_pontos_usuario(usuario_id):
    pontos = Ponto.query.filter_by(usuario_id=usuario_id).order_by(Ponto.data.desc()).limit(30).all()
    return jsonify([{
        'data': p.data.strftime('%Y-%m-%d'),
        'hora_entrada': p.hora_entrada.strftime('%H:%M') if p.hora_entrada else None,
        'hora_saida': p.hora_saida.strftime('%H:%M') if p.hora_saida else None,
        'hora_almoco_saida': p.hora_almoco_saida.strftime('%H:%M') if p.hora_almoco_saida else None,
        'hora_almoco_volta': p.hora_almoco_volta.strftime('%H:%M') if p.hora_almoco_volta else None,
        'observacoes': p.observacoes
    } for p in pontos])
