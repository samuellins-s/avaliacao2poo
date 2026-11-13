from modulos.erros import *
from dataclasses import dataclass
from abc import ABC, abstractmethod

@dataclass(frozen=True)
class Paciente:
    nome: str
    cartao_sus: str


class Atendimento(ABC):
    def __init__(self, paciente: Paciente) -> None:
        self._paciente = paciente
        self.tipo_atendimento = ''

    @property
    def paciente(self) -> Paciente:
        return self._paciente
    
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
        self._atendimentos: list[Atendimento] = []
        
    @property
    def minutos_ocupados(self) -> int:
        return sum(atendimento.duracao_minutos() for atendimento in self._atendimentos)

    @property
    def atendimentos(self) -> tuple[Atendimento]:
        return tuple(self._atendimentos)
    
    def agendar(self, atendimento: Atendimento):
        for intem in self._atendimentos:
            if intem.paciente == atendimento.paciente:
                raise PacienteJaAgendadoError(f"O paciente {atendimento.paciente.nome} já está agendado")
        
        duracao = atendimento.duracao_minutos()
        minutos_restantes = self._limite_minutos - self.minutos_ocupados
        
        if duracao > minutos_restantes:
            raise HorarioIndisponivelError("Horário indisponível: agenda cheia.")
        
        self._atendimentos.append(atendimento)