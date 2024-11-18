from flask import Flask, render_template, request, redirect, url_for
from gerador_horarios import gerhor
import logging

app = Flask(__name__)

# Configuração de logging
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

@app.route('/')
def index():
    return render_template('pages/pag-inicial.html')  # Página inicial

@app.route('/form', methods=['GET', 'POST'])
def formulario():
    if request.method == 'POST':
        # Coletando os dados do formulário
        dados = request.form  # Formulário enviado via POST
        num_periodos = dados['periodos']
        turmas = dados['turmas']
        professores = dados.getlist('professores')  # Lista de professores selecionados

        # Verificando se algum campo está vazio
        if not num_periodos or not turmas or not professores:
            return redirect(url_for('resultado', horarios=None))  # Redireciona para /resultado com dados vazios

        # Se os campos estiverem preenchidos corretamente, processa os dados
        num_periodos = int(num_periodos)
        turmas = turmas.split()  # Divide os nomes das turmas por espaço
        turmas_disciplinas = {}  # Mapeamento das disciplinas para os professores
        horas_profs = {}  # Mapeamento das horas de trabalho dos professores
        
        # Preenchendo os dados de turmas e disciplinas
        for professor in professores:
            turmas_disciplinas[professor] = []  # Aqui você pode adicionar logicamente as turmas e disciplinas
        for professor in professores:
            horas_profs[professor] = 0  # Atribua a carga horária necessária para cada professor

        # Criar uma instância da classe gerhor
        gerador = gerhor()
        
        # Passando os dados para a classe gerhor
        gerador.input_d(num_periodos, turmas, professores, turmas_disciplinas, horas_profs)
        
        # Gerar os horários
        gerador.allocate_h()

        # Obter os horários gerados
        horarios = gerador.get_h()

        # Redirecionar para a página de resultados com os horários gerados
        return redirect(url_for('resultado', horarios=horarios))

    return render_template('pages/formulario.html')  # Página do formulário

@app.route('/resultado')
def resultado():
    horarios = request.args.get('horarios')  # Recebe os horários via URL (se houver)
    
    # Se não houver horários, exibe mensagem
    if horarios is None:
        horarios = None  # Caso contrário, exibe uma lista vazia
    
    return render_template('pages/resultado.html', horarios=horarios)

@app.route('/sobre_nos')
def sobre_nos():
    return render_template('pages/sobre-nos.html')  # Página sobre nós

if __name__ == '__main__':
    app.run(debug=True)
