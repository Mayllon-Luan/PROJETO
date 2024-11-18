from flask import Blueprint, request, jsonify
from gerador import gerhor  # Importe a classe gerhor
import logging

gerador_bp = Blueprint('gerador', __name__)  # Cria o blueprint

# Configuração de logging
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

@gerador_bp.route('/processar-horarios', methods=['POST'])
def processar_horarios():
    try:
        dados = request.json
        logging.info(f"Dados recebidos: {dados}")  # Log dos dados recebidos

        num_periodos = dados['periodos']
        turmas = dados['turmas']
        professores = dados['professores']

        # Preparar dados para o algoritmo
        nome_profs = [p['nome'] for p in professores]
        turmas_disciplinas = {
            p['nome']: [(d['turma'], d['materia']) for d in p['disciplinas']]
            for p in professores
        }
        horas_profs = {p['nome']: p['horas'] for p in professores}

        # Executar o algoritmo
        gerador = gerhor()
        gerador.input_d(num_periodos, turmas, nome_profs, turmas_disciplinas, horas_profs)
        gerador.allocate_h()

        # Retornar os horários
        return jsonify(gerador.h)

    except Exception as e:
        logging.error(f"Erro ao processar horários: {e}")
        return jsonify({"error": str(e)}), 500
