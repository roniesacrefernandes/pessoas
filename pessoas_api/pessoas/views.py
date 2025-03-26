from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .serializers import PessoaSerializer
from .services import PessoaService
from .tasks import PessoaTask

class PessoaAPI(APIView):
    def post(self, request):
        serializer = PessoaSerializer(data=request.data)
        if serializer.is_valid():
            PessoaService.create_pessoa(serializer.validated_data)
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def get(self, request, cpf=None):
        pessoa = PessoaService.get_pessoa_by_cpf(cpf)
        if pessoa:
            serializer = PessoaSerializer(pessoa)
            return Response(serializer.data)
        return Response({"error": "Pessoa não encontrada"}, status=status.HTTP_404_NOT_FOUND)

    def put(self, request, cpf):
        pessoa = PessoaService.get_pessoa_by_cpf(cpf)
        if pessoa:
            serializer = PessoaSerializer(pessoa, data=request.data, partial=True)
            if serializer.is_valid():
                PessoaService.update_pessoa(pessoa, serializer.validated_data)
                return Response(serializer.data)
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        return Response({"error": "Pessoa não encontrada"}, status=status.HTTP_404_NOT_FOUND)

    def delete(self, request, cpf):
        pessoa = PessoaService.get_pessoa_by_cpf(cpf)
        if pessoa:
            PessoaService.delete_pessoa(pessoa)
            return Response({"message": "Pessoa excluída com sucesso"}, status=status.HTTP_204_NO_CONTENT)
        return Response({"error": "Pessoa não encontrada"}, status=status.HTTP_404_NOT_FOUND)

class CalcularPesoIdealAPI(APIView):
    def get(self, request, cpf):
        return Response(PessoaTask.calcular_peso_ideal(cpf))
