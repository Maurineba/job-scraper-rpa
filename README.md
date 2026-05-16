# 🚀 Job Vacancy Monitor RPA

Sistema de automação para coleta, processamento e análise de vagas de emprego utilizando Python, Selenium, SQLite e Excel.

---

## 📌 Sobre o Projeto

O **Job Vacancy Monitor RPA** simula um pipeline corporativo de automação de processos (**RPA + ETL**), realizando desde a coleta automatizada de vagas até a geração de relatórios executivos em Excel.

O projeto foi desenvolvido com foco em:

- automação de tarefas repetitivas
- scraping de dados reais
- tratamento e persistência de informações
- geração automatizada de relatórios
- organização de aplicações Python em arquitetura modular

---

# ⚙️ Fluxo da Aplicação

```text
Scraper → Tratamento → Banco de Dados → Excel Dashboard
```

O sistema executa automaticamente:

1. Navegação em sites de vagas
2. Extração das informações
3. Tratamento e normalização dos dados
4. Persistência em banco SQLite
5. Geração de dashboard em Excel

---

# ✨ Funcionalidades

## 🔎 Coleta Automatizada

- Navegação automatizada com Selenium
- Paginação automática
- Extração de vagas em tempo real

## 📄 Extração de Dados

O sistema coleta:

- título da vaga
- salário
- modalidade
- link da vaga

## 🧹 Tratamento de Dados

- normalização de salários
- limpeza de strings
- padronização de informações

## 🗄️ Persistência

- armazenamento em SQLite
- prevenção de duplicidade de vagas

## 📊 Relatórios e Dashboard

Geração automática de planilha Excel contendo:

- tabela completa de vagas
- total de vagas encontradas
- média salarial
- distribuição por modalidade
- gráficos automáticos

---

# 🏗️ Estrutura do Projeto

```bash
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
```

---

# 🛠️ Tecnologias Utilizadas

- Python
- Selenium
- SQLite
- Pandas
- OpenPyXL
- Logging

---

# ▶️ Como Executar

## 1️⃣ Clonar o Repositório

```bash
git clone https://github.com/Maurineba/job-scraper-rpa.git
```

---

## 2️⃣ Entrar na Pasta do Projeto

```bash
cd job-scraper-rpa
```

---

## 3️⃣ Criar Ambiente Virtual

```bash
python -m venv venv
```

---

## 4️⃣ Ativar Ambiente Virtual

### Windows

```bash
venv\Scripts\activate
```

### Linux/macOS

```bash
source venv/bin/activate
```

---

## 5️⃣ Instalar Dependências

```bash
pip install -r requirements.txt
```

---

## 6️⃣ Criar Tabela do Banco

```bash
python -m database.create_table
```

---

## 7️⃣ Executar o Projeto

```bash
python main.py
```

---

# 📦 Saída do Sistema

Após a execução, o sistema gera automaticamente:

- banco SQLite com vagas persistidas
- logs de execução
- planilha Excel com dashboard analítico

---

# 📈 Dashboard Gerado

O dashboard em Excel contém:

- tabela completa das vagas
- total de vagas coletadas
- média salarial
- distribuição por modalidade
- gráficos automáticos

---

# 🎯 Objetivos do Projeto

Este projeto foi desenvolvido para praticar:

- automação web
- scraping de dados
- manipulação de dados reais
- persistência em banco de dados
- geração automatizada de relatórios
- organização de aplicações Python
- pipelines simples de ETL

---

# 🚧 Melhorias Futuras

- execução agendada automática
- API REST com FastAPI
- dashboard web
- envio automático de relatórios
- filtros avançados
- suporte a múltiplos sites
- containerização com Docker

---

# 👨‍💻 Autor

**Maurino Martins da Silva Junior**

- GitHub: https://github.com/Maurineba
- LinkedIn: https://linkedin.com/in/maurino-martins-444008335

---
