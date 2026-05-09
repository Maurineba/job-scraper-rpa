Job Vacancy Monitor RPA

Automação de coleta, processamento e análise de vagas de emprego utilizando Selenium, SQLite e Excel.

Sobre o projeto

Este projeto simula um pipeline simples de automação corporativa (RPA + ETL), realizando:

navegação automatizada em sites de vagas
extração de dados com Selenium
tratamento e normalização de informações
persistência em banco SQLite
geração automática de relatórios em Excel
criação de dashboard com métricas e gráficos

O objetivo do projeto é praticar automação de processos, manipulação de dados reais e organização de aplicações Python voltadas para RPA.

Fluxo da aplicação
Scraper → Tratamento → Banco de Dados → Excel Dashboard
Funcionalidades
Coleta automatizada de vagas
Extração de:
título
salário
modalidade
link da vaga
Paginação automática
Tratamento de salários
Persistência em SQLite
Evita duplicidade de vagas
Exportação automática para Excel
Dashboard com:
total de vagas
média salarial
gráfico de modalidades
Estrutura do projeto
job-vacancy-monitor-rpa/
│
├── bot/
│   ├── exporter.py
│   ├── logger.py
│   └── scrapper.py
│
├── database/
│   ├── conn.py
│   ├── create_table.py
│   └── jobs_repository.py
│
├── utils/
│   ├── parse_salary.py
│   └── resolve_salary.py
│
├── exports/
│
├── logs/
│
├── main.py
├── requirements.txt
└── README.md
Tecnologias utilizadas
Python
Selenium
SQLite
OpenPyXL
Pandas
Logging
Como executar
1. Clonar o repositório
git clone https://github.com/Maurineba/job-scraper-rpa.git
2. Entrar na pasta
cd job-scraper-rpa
3. Criar ambiente virtual
python -m venv venv
4. Ativar ambiente virtual
Windows
venv\Scripts\activate
Linux/macOS
source venv/bin/activate
5. Instalar dependências
pip install -r requirements.txt
6. Criar tabela do banco
python -m database.create_table
7. Executar o projeto
python main.py
Saída do sistema

O sistema gera automaticamente:

banco SQLite com vagas persistidas
logs de execução
planilha Excel com dashboard
Dashboard gerado

O arquivo Excel contém:

tabela completa de vagas
total de vagas encontradas
média salarial
distribuição por modalidade
gráfico automático
Objetivos do projeto
praticar automação web
desenvolver lógica de scraping
trabalhar com persistência de dados
gerar relatórios automatizados
simular pipelines simples de dados
Melhorias futuras
execução agendada automática
API com FastAPI
dashboard web
envio automático de relatórios
filtros avançados
suporte a múltiplos sites
