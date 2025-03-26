from .models import Pessoa

class PessoaService:
    @staticmethod
    def get_pessoa_by_cpf(cpf):
        return Pessoa.objects.filter(cpf=cpf).first()

    @staticmethod
    def create_pessoa(data):
        return Pessoa.objects.create(**data)

    @staticmethod
    def update_pessoa(pessoa, data):
        for key, value in data.items():
            setattr(pessoa, key, value)
        pessoa.save()
        return pessoa

    @staticmethod
    def delete_pessoa(pessoa):
        pessoa.delete()
