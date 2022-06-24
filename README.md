# fast-api-fiis
API Controle de Investimentos Imobiliários - FIIS.

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
```git clone https://github.com/lnicolini/fast-api-fiis.git
```
Adicionar o arquivo `.env` na pasta do projeto como no exemplo abaixo:
```PG_USER=admin
PG_PASS=admin
PG_DB=fastapi
DATABASE_URL=postgresql+asyncpg://admin:admin@localhost:5432/fastapi
PYTHONPATH=/home/luan/Estudo/fast_api
```