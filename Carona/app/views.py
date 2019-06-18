import psycopg2, psycopg2.extras
from flask import g, render_template, request, redirect, url_for, session


from app import app


@app.before_request
def before_request():
    g.db = psycopg2.connect('dbname=postgres user=postgres password=123 host=localhost')



@app.route('/login', methods=['POST'])
def formulario():
    c = g.db.cursor()
    c.execute(f"SELECT * FROM cadastro")
    for x in c.fetchall():
        if x[1] == request.form["cpf"] and x[2] == request.form["senha"] and len(x[6]) < 11 or len(x[6]) > 11:
            return redirect('/listar')
        elif x[1] == request.form["cpf"] and x[2] == request.form["senha"] and len(x[5])==11:
            return redirect('/listarEadd')
    c.close()
    print('eae')
    return redirect('/')

@app.route('/addviagem', methods=['GET'])
def viajar():
    return render_template('viagem.html')

@app.route('/', methods=['GET'])
def logar():
    return render_template('login.html')

@app.route('/formcadastro', methods=['GET'])
def cadastro():
    return render_template('cadastro.html')


@app.route('/cadastro', methods=['POST'])
def cadastrar():
    try:
        c=g.db.cursor()
        c.execute(f"INSERT INTO cadastro (nome, senhacadastro,  email, cpfcadastro, genero, datanascimento, carro, placa, cnh, vagas) VALUES (\'{request.form['nome']}\', \'{request.form['senha']}\',  \'{request.form['email']}\', \'{request.form['cpf']}\', \'{request.form['genero']}\', \'{request.form['data']}\', \'{request.form['modelo']}\', \'{request.form['placadocarro']}\', \'{request.form['cnh']}\', \'{request.form['vagas']}\')")
        g.db.commit()
        c.close()
        return redirect(url_for('logar'))
    except psycopg2.IntegrityError:
        return redirect(url_for('cadastro'))


@app.route('/viagem', methods=['GET', 'POST'])
def cadastrarviagem():
    try:
        c=g.db.cursor()
        c.execute(f"INSERT INTO viagens (nome, origem,  destino, dataviagem, horario, vagas) VALUES (\'{request.form['nome']}\', \'{request.form['origem']}\',  \'{request.form['destino']}\', \'{request.form['data']}\', \'{request.form['horario']}\', \'{request.form['vagas']}\')")
        g.db.commit()
        c.close()
        return redirect(url_for('listarEadicionar'))
    except psycopg2.IntegrityError:
        return redirect(url_for('cadastrarviagem'))
  


    


@app.route('/listar', methods=['GET'])
def listarviagens():
    c=g.db.cursor()
    c.execute(f"SELECT * FROM viagens")
    results=c.fetchall()
    return render_template('listar.html', listagem=results)
    c.close()

@app.route('/listarEadd', methods=['GET'])
def listarEadicionar():
    c=g.db.cursor()
    c.execute(f"SELECT * FROM viagens")
    results=c.fetchall()
    return render_template('listarEadd.html', listagem=results)
    c.close()