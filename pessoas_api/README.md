Cadastro de Pessoas - Peso Ideal

Este projeto consiste em um sistema de cadastro de pessoas com cálculo de peso ideal. Ele possui uma interface web em HTML5 e um backend desenvolvido em Django com Django Rest Framework (DRF), além de utilizar um banco de dados PostgreSQL para armazenar as informações.

Tecnologias Utilizadas

Frontend: HTML5, CSS e JavaScript

Backend: Django, Django Rest Framework (DRF)

Banco de Dados: PostgreSQL

ORM: Django ORM

API REST: JSON, Fetch API

Gerenciamento de Dependências: pip, virtualenv

Variáveis de Ambiente: django-environ

⚙️ Funcionalidades

CRUD completo para cadastro de pessoas (Criar, Ler, Atualizar e Excluir)

Consulta por CPF

Cálculo do peso ideal baseado na altura e sexo da pessoa

Validações de formulário

Persistência de dados com PostgreSQL

**Configuração segura com **.env

Como Rodar o Projeto

1️⃣ Clonar o repositório

git clone https://github.com/roniesacrefernandes/pessoas.git
cd projeto_peso_ideal

2️⃣ Criar um ambiente virtual e instalar dependências

python -m venv venv
source venv/bin/activate  # Linux/macOS
venv\Scripts\activate  # Windows
pip install -r requirements.txt

3️⃣ Configurar variáveis de ambiente (.env)

Crie um arquivo .env na raiz do projeto e adicione:

DB_NAME=peso_ideal_db
DB_USER=postgres
DB_PASSWORD=sua_senha
DB_HOST=localhost
DB_PORT=5432

4️⃣ Executar as migrações do banco de dados

python manage.py migrate

5️⃣ Iniciar o servidor Django

python manage.py runserver

O backend estará disponível em: http://127.0.0.1:8000

6️⃣ Abrir o Frontend

Basta abrir o arquivo frontend/index.html no navegador.

🌍 Endpoints da API

Método

Endpoint

Descrição

GET

/api/pessoas/{cpf}/

Buscar uma pessoa pelo CPF

POST

/api/pessoas/

Criar uma nova pessoa

PUT

/api/pessoas/{cpf}/

Atualizar os dados de uma pessoa

DELETE

/api/pessoas/{cpf}/

Excluir uma pessoa

GET

/api/pessoas/{cpf}/calcular_peso_ideal/

Retornar o peso ideal