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
    def __init__(self, paciente) -> None:
        super().__init__(paciente)
        self.tipo_atendimento = 'Consulta'

    def duracao_minutos(self):
        return super().duracao_minutos()