# Sistema de Ponto Eletrônico

Um sistema completo de controle de ponto eletrônico desenvolvido em Flask com interface web moderna e responsiva.

## 🚀 Funcionalidades

### Para Funcionários
- **Login seguro** com autenticação
- **Registro de ponto** (entrada, saída para almoço, volta do almoço, saída)
- **Envio de justificativas** para faltas, atrasos, etc.
- **Visualização do histórico** de pontos
- **Painel intuitivo** com informações do dia

### Para Administradores
- **Painel administrativo completo**
- **Cadastro de funcionários**
- **Controle de ponto** de todos os funcionários
- **Gerenciamento de justificativas** (aprovar/rejeitar)
- **Cadastro de horários** de trabalho
- **Relatórios e estatísticas**

## 🛠️ Tecnologias Utilizadas

- **Backend:** Flask (Python)
- **Banco de Dados:** SQLite com SQLAlchemy
- **Frontend:** Bootstrap 5, HTML5, CSS3, JavaScript
- **Autenticação:** Session-based com hash de senhas
- **Interface:** Responsiva e moderna

## 📋 Pré-requisitos

- Python 3.7 ou superior
- pip (gerenciador de pacotes Python)

## 🔧 Instalação e Configuração

1. **Clone ou baixe o projeto**
   ```bash
   # Se usando git
   git clone <url-do-repositorio>
   cd sistema-ponto-eletronico
   ```

2. **Instale as dependências**
   ```bash
   pip install -r requirements.txt
   ```

3. **Execute o sistema**
   ```bash
   python run.py
   ```

4. **Acesse o sistema**
   - Abra seu navegador
   - Acesse: `http://127.0.0.1:5000`

## 👤 Usuários Padrão

O sistema cria automaticamente usuários de teste:

### Administrador
- **Usuário:** `admin`
- **Senha:** `admin123`

### Funcionário
- **Usuário:** `funcionario`
- **Senha:** `123456`

## 📁 Estrutura do Projeto

```
sistema-ponto/
├── run.py                 # Arquivo principal para executar
├── app.py                 # Configurações da aplicação Flask
├── requirements.txt       # Dependências Python
├── instance/
│   ├── dados.db          # Banco de dados SQLite
│   ├── models.py         # Modelos do banco de dados
│   └── db.py             # Configuração do banco
├── sistema-ponto/
│   └── routes.py         # Rotas da aplicação
├── templates/            # Templates HTML
│   ├── base.html         # Template base
│   ├── login.html        # Tela de login
│   ├── inicial.html      # Painel funcionário
│   ├── inicial-admin.html # Painel administrador
│   ├── baterponto.html   # Bater ponto
│   ├── justificativaF.html # Enviar justificativa
│   ├── usuario.html      # Cadastrar funcionário
│   └── ...               # Outros templates
└── static/               # Arquivos estáticos (CSS, JS, imagens)
```

## 🗄️ Banco de Dados

O sistema utiliza SQLite com as seguintes tabelas:

- **usuarios** - Dados dos usuários (funcionários e admins)
- **pontos** - Registros de ponto dos funcionários
- **justificativas** - Justificativas enviadas pelos funcionários
- **horarios** - Horários de trabalho configurados

## 🔒 Segurança

- Senhas são criptografadas com hash
- Autenticação baseada em sessões
- Controle de acesso por tipo de usuário
- Validações no frontend e backend

## 📱 Interface Responsiva

O sistema é totalmente responsivo e funciona em:
- Desktop
- Tablets
- Smartphones

## 🚀 Como Usar

### Para Funcionários

1. **Fazer Login**
   - Acesse o sistema
   - Digite seu usuário e senha
   - Clique em "Entrar"

2. **Bater Ponto**
   - No painel inicial, clique em "Bater Ponto"
   - Clique no botão correspondente (Entrada, Saída Almoço, etc.)
   - Confirme o registro

3. **Enviar Justificativa**
   - No painel inicial, clique em "Justificativa"
   - Preencha os dados da justificativa
   - Clique em "Enviar"

### Para Administradores

1. **Fazer Login**
   - Use as credenciais de administrador
   - Será direcionado para o painel admin

2. **Cadastrar Funcionário**
   - No painel admin, clique em "Cadastrar Funcionário"
   - Preencha os dados do novo funcionário
   - Clique em "Cadastrar"

3. **Gerenciar Justificativas**
   - Clique em "Justificativas" para ver pendentes
   - Aprove ou rejeite as justificativas

4. **Controlar Pontos**
   - Clique em "Controle de Ponto"
   - Visualize e edite os pontos dos funcionários

## 🔧 Personalização

### Modificar Configurações

Edite o arquivo `run.py` para alterar:
- Porta do servidor (padrão: 5000)
- Host (padrão: 127.0.0.1)
- Configurações de debug

### Adicionar Funcionalidades

1. **Modelos:** Edite `instance/models.py`
2. **Rotas:** Edite `sistema-ponto/routes.py`
3. **Templates:** Adicione/edite arquivos em `templates/`

## 🐛 Resolução de Problemas

### Erro: "Módulo não encontrado"
```bash
pip install -r requirements.txt
```

### Erro: "Banco de dados não encontrado"
O banco será criado automaticamente na primeira execução.

### Erro: "Porta em uso"
Altere a porta no arquivo `run.py` ou finalize processos que usam a porta 5000.

## 📈 Futuras Melhorias

- [ ] Relatórios em PDF/Excel
- [ ] Notificações por email
- [ ] API REST para integração
- [ ] Dashboard com gráficos
- [ ] Backup automático do banco
- [ ] Múltiplas empresas/filiais

## 📞 Suporte

Para dúvidas ou problemas:
1. Verifique a documentação
2. Consulte os logs de erro
3. Certifique-se de que todas as dependências estão instaladas

## 📄 Licença

Este projeto é de uso livre para fins educacionais e comerciais.

---

**Desenvolvido com ❤️ usando Flask e Bootstrap**
