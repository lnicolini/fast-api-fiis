# fast-api-fiis
**API Controle de Investimentos Imobiliários - FIIS.**

Com o objetivo de estudar a linguagem Python e o Framework FastApi, resolvi desenvolver
uma API bem simples para inclusão de Compras e Vendas de Fundos Imobiliários.
A idéia é evoluir a API com o tempo adicionando novas funcionalidades, como recuperar dados de cotações, distribuição da carteira e dividendos recebidos.

### Dependências
* Docker
* Docker-compose
* Python >= 3.6
* Pipenv

### Como Executar?
Fazer o git clone do projeto para a sua máquina
```shell
git clone https://github.com/lnicolini/fast-api-fiis.git
```
Adicionar o arquivo `.env` na pasta do projeto podendo utilizar o exemplo abaixo:
```PG_USER=admin
PG_PASS=admin
PG_DB=fastapi
DATABASE_URL=postgresql+asyncpg://admin:admin@localhost:5432/fastapi
PYTHONPATH=/home/luan/Estudo/fast_api
```
Iniciar o serviço do **postgres** e do **pgadmin** (opcional)
```shell
docker-compose up -d
```
Para acessar o pgAdmin
```shell
http://127.0.0.1:5050/login
Login: "admin@gmail.com"
Password: "admin"
```
Iniciar o ambiente de desenvolvimento com o pipenv
```shell
pipenv shell
```
Instalar as dependências do Python
```shell
pipenv install
```
Criar a estrutura do Banco de Dados
```shell
python database/init_db.py
```
Iniciar a Aplicação
```shell
uvicorn main:app --port 8080
```

## Endpoints

- POST `/user/create` - Cria novos usuários
- GET `/user/list` - Lista todos os usuários cadastrados
- POST `/transaction/create` - Cria uma nova transação
- GET `/transaction/list` - Listas todos as transações realizadas
- GET `/transaction/list_by_transaction/{cod_transaction}` - Lista a transação pelo código único (UUID)
- GET `/transaction/list_by_user/{idt_user}` - Lista todas as transações de um usuário específico
- DELETE `/transaction/delete/{cod_transaction}` - Deleta a transação pelo código único (UUID)

## Docs
http://127.0.0.1:8080/docs  
http://127.0.0.1:8080/redoc