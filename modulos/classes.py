from dataclasses import dataclass
from abc import ABC, abstractmethod

@dataclass(frozen=True)
class Paciente:
    nome: str
    cartao_sus: str


class Atendimento(ABC):
    def __init__(self, paciente: Paciente) -> None:
        self.paciente = paciente
        self.tipo_atendimento = ''

    @abstractmethod
    def duracao_minutos(self) -> int:
        pass

    def __str__(self) -> str:
        return f'\nTipo do atendimento: {self.tipo_atendimento},\nNome do paciente: {self.paciente.nome},\nDuração atendimento: {self.duracao_minutos()}'


class Consulta(Atendimento):
    def __init__(self, paciente, especialidade: str, retorno: bool = False) -> None:
        super().__init__(paciente)
        self.tipo_atendimento = 'Consulta'
        self.especialidade = especialidade
        self.retorno = retorno

    def duracao_minutos(self) -> int:
        if self.retorno:
            return 15
        else:
            return 30


class Exame(Atendimento):
    def __init__(self, paciente, tipo: str, jejum: bool = False) -> None:
        super().__init__(paciente)
        self.tipo = tipo
        self.jejum = jejum

    def duracao_minutos(self) -> int:
        if self.jejum:
            return 30
        else:
            return 20


class Vacinacao(Atendimento):
    def __init__(self, paciente, vacina: str, doses: int = 1) -> None:
        super().__init__(paciente)
        self.vacina = vacina
        self.doses = doses

    def duracao_minutos(self) -> int:
        return self.doses * 10


