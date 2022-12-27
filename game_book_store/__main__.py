from datetime import time
from flask import Flask, render_template, request, session, redirect, flash, url_for, send_from_directory
#from dao import JogoDao, UsuarioDao
#from models import Game
from core import get_games_from_database , add_game_to_database
import os
# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.

# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    app = Flask(__name__)
    app.secret_key = 'alura'  # Aqui!!!
    app.config['UPLOAD_PATH'] = os.path.dirname(os.path.abspath(__file__)) + '/uploads'
    #app.engine = engine
    #db = MySQL(app)
    #jogo_dao = JogoDao(db)
    #usuario_dao = UsuarioDao(db)
    @app.route('/')
    def index():
        list = get_games_from_database()
        return list
        #return render_template('lista.html', titulo='Jogos', jogos=lista)

    @app.route('/new')
    def new():
        #if 'usuario_logado' not in session or session['usuario_logado'] == None:
        #    flash('Favor efetuar o login para adiocionar jogo!')
        #    return redirect(url_for('login'))
        return render_template('new.html', titulo='New Game')
#
    #@app.route('/editar/<int:id>')
    #def editar(id):
    #    if 'usuario_logado' not in session or session['usuario_logado'] == None:
    #        flash('Favor efetuar o login para adiocionar jogo!')
    #        return redirect(url_for('login'))
    #    jogo = jogo_dao.busca_por_id(id)
    #    upload_path = app.config['UPLOAD_PATH']
    #    nome_imagem = recupera_imagem(id)
    #    return render_template('editar.html', titulo='Editando Jogo', jogo=jogo, capa_jogo=nome_imagem or 'capa_padrao.jpg')
    #    #Havia feito dessa maneira
    #    #if os.path.isfile(f'{upload_path}/capa{jogo.id}.jpg'):
    #    #    return render_template('editar.html', titulo='Editar Jogo', jogo=jogo, capa_jogo=f'capa{id}.jpg')
    #    #else:
    #    #    return render_template('editar.html', titulo='Editar Jogo', jogo=jogo, capa_jogo='capa_padrao.jpg')
#
    #@app.route('/deletar/<int:id>')
    #def deletar(id):
    #    if 'usuario_logado' not in session or session['usuario_logado'] == None:
    #        flash('Favor efetuar o login para adiocionar jogo!')
    #        return redirect(url_for('login'))
    #    jogo_dao.deletar(id)
    #    flash('O jogo foi removido com sucesso!')
    #    return redirect(url_for('index'))
#
    @app.route('/create', methods=['POST',])
    def create():
        name = request.form['name']
        category = request.form['category']
        console = request.form['console']
        file_name = request.files['file_name']
        add_game_to_database(name,category,console)
        #Vai retornar o id do jogo para poder salvar a imagem com o id
        #upload_path = app.config['UPLOAD_PATH']
        #timestamp = time.time()
        #arquivo.save(f'{upload_path}/capa{jogo.id}-{timestamp}.jpg')
        return redirect(url_for('index'))
#
#
    @app.route('/uploads/<file_name>')
    def image(file_name):
        return send_from_directory('uploads', file_name)
#
    #@app.route('/atualizar', methods=['POST',])
    #def atualizar():
    #    nome = request.form['nome']
    #    categoria = request.form['categoria']
    #    console = request.form['console']
    #    id = request.form['id']
    #    arquivo = request.files['arquivo']
    #    jogo = Jogo(nome, console, categoria, id)
    #    if arquivo:
    #        timestamp = time.time()
    #        upload_path = app.config['UPLOAD_PATH']
    #        deleta_arquivo(jogo.id)
    #        arquivo.save(f'{upload_path}/capa{jogo.id}-{timestamp}.jpg')
    #    jogo_dao.salvar(jogo)
    #    flash('O jogo foi atualizado com sucesso!')
    #    return redirect(url_for('index'))
#
#
    #@app.route('/login')
    #def login():
    #    if 'usuario_logado' not in session or session['usuario_logado'] == None:
    #        return render_template('login.html')
    #    else:
    #        flash(session['usuario_logado'] + ' ja esta logado!')
    #        return redirect(url_for('index'))
#
    #@app.route('/autenticar', methods=['POST', ])
    #def autenticar():
    #    usuario = usuario_dao.buscar_por_id(request.form['usuario'])
    #    if usuario:
    #        if usuario.senha == request.form['senha']:
    #            session['usuario_logado'] = usuario.id
    #            flash(usuario.nome + ' logou com sucesso!')
    #            return redirect(url_for('index'))
    #    else:
    #        flash('Erro login ou senha, tente de novo!')
    #        return redirect(url_for('login'))
#
#
    #@app.route('/logout')
    #def logout():
    #    if 'usuario_logado' not in session or session['usuario_logado'] == None:
    #        flash('Nenhum usuario logado!')
    #        return redirect(url_for('index'))
    #    else:
    #        flash(session['usuario_logado'] + ' deslogou com sucesso!')
    #        session['usuario_logado'] = None
    #        return redirect(url_for('index'))
#
    #def recupera_imagem(id):
    #    for nome_arquivo in os.listdir(app.config['UPLOAD_PATH']):
    #        if f'capa{id}' in nome_arquivo:
    #            return nome_arquivo
#
    #def deleta_arquivo(id):
    #    arquivo = recupera_imagem(id)
    #    if arquivo:
    #        os.remove(os.path.join(app.config['UPLOAD_PATH'], arquivo))
#

    app.run(debug=True)


# See PyCharm help at https://www.jetbrains.com/help/pycharm/
