# API_reservas_cinema

API desenvolvida para gerenciar sessões de cinema e permitir a reserva de assentos.
O projeto foi construído com foco em organização arquitetural, separação de responsabilidades e clareza na implementação das regras de negócio.

A aplicação está publicada em ambiente de produção utilizando Render.

# Tecnologias Utilizadas:

- Python 3.11+
- FastAPI
- Uvicorn
- Ambiente virtual (venv)

Deploy

A aplicação está disponível publicamente em:

https://api-reservas-cinema.onrender.com


Documentação interativa (Swagger):

https://api-reservas-cinema.onrender.com/docs


Execução Local
1. Clonar o repositório:

git clone https://github.com/EmanuelGMachado/API_reservas_cinema.git
cd API_reservas_cinema

2. Instalar dependências

Recomendado utilizar o arquivo requirements.txt:
pip install -r requirements.txt

Caso necessário, instalar manualmente:
pip install fastapi uvicorn

4. Executar o servidor

Como o projeto está estruturado em pacote (app), execute:
uvicorn app.main:app --reload

A aplicação será iniciada em:
http://127.0.0.1:8000


# Documentação da API
O FastAPI gera automaticamente a documentação interativa.

Acesse:
http://127.0.0.1:8000/docs

Ou, em produção:
https://api-reservas-cinema.onrender.com/docs

Nela é possível testar todos os endpoints diretamente pelo navegador.
Nota: Por estar em um ambiente de demonstração gratuito, o primeiro carregamento pode levar cerca de 1 minuto para inicializar o servidor. Após isso, a navegação será instantânea.

Endpoints disponíveis:

| Método | Rota                            | Descrição                             |
| ------ | ------------------------------- | ------------------------------------- |
| GET    | `/`                             | Endpoint raiz de verificação          |
| GET    | `/sessoes`                      | Lista todas as sessões disponíveis    |
| GET    | `/sessoes/{id_sessao}/assentos` | Lista os assentos vagos de uma sessão |
| POST   | `/reservar`                     | Realiza a reserva de um assento       |


Códigos HTTP de Resposta
200 OK — Operação realizada com sucesso
404 Not Found — Sessão ou assento não encontrado
409 Conflict — Assento já reservado
400 Bad Request — Erro inesperado na requisição

# Arquitetura

O projeto foi organizado em camadas:
Rotas: Responsáveis por receber requisições HTTP e retornar respostas.
Regras: Contêm a lógica de negócio do sistema.
Banco: Simulação de persistência em memória, estruturada para permitir futura migração para banco relacional ou JSON.
Main: Configuração da aplicação e registro das rotas.

Essa organização permite desacoplamento entre regras de negócio e camada de API.

# Modelagem de Dados

Cada sessão contém:
-id_sessao
-titulo_filme
-sala
-horario
-lista de assentos

Cada assento contém:
-id
-disponivel (boolean)

- A estrutura foi definida para facilitar futura evolução para banco relacional (SQLite ou PostgreSQL).


# Considerações Técnicas

- Não há controle real de concorrência, mas a lógica de validação impede dupla reserva no fluxo normal.
- A estrutura foi pensada para permitir escalabilidade futura.
- Projeto desenvolvido para avaliação técnica de backend.