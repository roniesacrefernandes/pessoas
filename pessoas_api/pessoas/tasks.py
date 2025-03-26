from .services import PessoaService

class PessoaTask:
    @staticmethod
    def calcular_peso_ideal(cpf):
        pessoa = PessoaService.get_pessoa_by_cpf(cpf)
        if pessoa:
            return {"peso_ideal": pessoa.calcular_peso_ideal()}
        return {"error": "Pessoa não encontrada"}
