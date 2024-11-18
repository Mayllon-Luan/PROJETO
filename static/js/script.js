function addProfessor() {
    const professorName = document.getElementById('professor-name').value;
    const container = document.getElementById('professores-container');

    if (professorName) {
        const professorDiv = document.createElement('div');
        professorDiv.className = 'professor';

        professorDiv.innerHTML = `
            <h3>Resposta sobre o(a) professor(a) ${professorName}:</h3>
            <div class="input">
                <label>Turmas & disciplinas (separadas por um _):</label>
                <input type="text" name="${professorName}-disciplinas" placeholder="Ex.: 3A_Matemática 4A_Física">
            </div>
            <div class="input">
                <label>Horas de trabalho por semana:</label>
                <input type="number" name="${professorName}-horas" placeholder="Ex.: 18">
            </div>
        `;

        container.appendChild(professorDiv);
        document.getElementById('professor-name').value = ''; // Limpa o campo de entrada
    }
}

function submitForm() {
    const periodos = document.getElementById('num-periodos').value;
    const turmas = document.getElementById('nome-turmas').value.split(' ');
    const professoresDiv = document.querySelectorAll('.professor');

    const professores = Array.from(professoresDiv).map(professorDiv => {
        const nome = professorDiv.querySelector('h3').textContent.replace('Resposta sobre o(a) professor(a) ', '').replace(':', '').trim();
        const disciplinas = professorDiv.querySelector('input[name*="disciplinas"]').value.split(' ');
        const horas = professorDiv.querySelector('input[name*="horas"]').value;
        return {
            nome,
            disciplinas: disciplinas.map(d => {
                const [turma, materia] = d.split('_');
                return { turma, materia };
            }),
            horas: parseInt(horas)
        };
    });

    const payload = {
        periodos: parseInt(periodos),
        turmas,
        professores
    };

    // Enviar via Fetch API
    fetch('/processar-horarios', {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json'
        },
        body: JSON.stringify(payload)
    })
    .then(response => response.json())
    .then(data => {
        console.log('Horários gerados:', data);
        alert('Horários gerados com sucesso!');
    })
    .catch(err => {
        console.error('Erro:', err);
        alert('Falha ao gerar os horários.');
    });
}
