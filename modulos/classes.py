from modulos.erros import *
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
    def __init__(self, paciente: Paciente, especialidade: str, retorno: bool = False) -> None:
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
    def __init__(self, paciente: Paciente, tipo: str, jejum: bool = False) -> None:
        super().__init__(paciente)
        self.tipo = tipo
        self.jejum = jejum

    def duracao_minutos(self) -> int:
        if self.jejum:
            return 30
        else:
            return 20


class Vacinacao(Atendimento):
    def __init__(self, paciente: Paciente, vacina: str, doses: int = 1) -> None:
        super().__init__(paciente)
        self.vacina = vacina
        self.doses = doses

    def duracao_minutos(self) -> int:
        return self.doses * 10


class Agenda:
    def __init__(self, limite_minutos: int = 240) -> None:
        self._limite_minutos: int = limite_minutos
        self.atendimentos: list[Atendimento] = []
        self.agendamentos: list[Atendimento] = []

    @property
    def listaAtendimento(self) -> None:
        for atendimento in self.atendimentos:
            print(atendimento)

    @property
    def minutos_ocupados(self) -> int:
        return sum(atendimento.duracao_minutos() for atendimento in self.atendimentos)

    def agendar(self, atendimento: Atendimento):
        for index in range(len(self.atendimentos)):
            for index2 in range( index + 1, len(self.atendimentos)):
                if index.paciente.nome and index.paciente.cartao_sus ==  index2.paciente.nome and index2.paciente.cartao_sus:
                    raise PacienteJaAgendadoError('O paciente já está agendado')
                else:
                    self.agendamentos.append(atendimento)