class gerhor:
    def __init__(self):
        self.h = {}

    def input_d(self, periodos, turmas, nome_profs, turmas_disciplinas, horas_profs):
        self.periodos = periodos
        self.turmas = turmas
        self.nome_profs = nome_profs
        self.turmas_disciplinas = turmas_disciplinas
        self.horas_profs = horas_profs

    def allocate_h(self):
        # Exemplo de lógica para alocar horários
        self.h = {prof: f"Horário alocado para {prof}" for prof in self.nome_profs}
