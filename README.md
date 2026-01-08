<<<<<<< HEAD
# Git and Analytics Project

## 🇧🇷 Português

Este repositório foi criado com o objetivo de **ensinar e demonstrar o uso básico do Git** utilizando um projeto real de dados como exemplo, dentro do contexto da **Comunidade DS**.

O projeto serve como um **esqueleto/base** para mostrar, na prática, como o Git pode ser utilizado ao longo do desenvolvimento de um projeto de dados — desde a criação do repositório até ajustes finais e deploy.

---

## 📊 Dashboard

O dashboard desenvolvido neste projeto pode ser acessado no link abaixo:

👉 **[Git Analytics Dashboard](https://git-analytic.streamlit.app/)**

---

## 🎯 Objetivo do Projeto

Os principais objetivos deste repositório são:

- Ensinar os **conceitos fundamentais de Git**
- Demonstrar **boas práticas de commits**
- Mostrar como estruturar um **projeto simples de dados**
- Servir como **material de apoio didático**
- Facilitar o aprendizado de Git de forma prática

O foco do projeto **não é complexidade técnica**, mas sim o **processo de versionamento e organização do código**.

---

## 🧱 Estrutura do Projeto

```text
git_analytics/
│
├── app.py                  # Arquivo principal da aplicação Streamlit
├── answers.py              # Respostas das perguntas de negócio e visualizações
├── extraction.py           # Carregamento e preparação dos dados
├── requirements.txt        # Dependências do projeto
├── runtime.txt             # Versão do Python para deploy
├── README.md               # Documentação do projeto
│
├── data/
│   └── processed/
│       └── bikes_completed.csv
│
└── .devcontainer/          # Configuração de ambiente de desenvolvimento

🛠️ Tecnologias Utilizadas

Python 3.10

Streamlit

Pandas

Plotly

Git e GitHub

▶️ Como Executar o Projeto Localmente

Clone o repositório:

git clone https://github.com/ramosvinicius/git_analytics.git
cd git_analytics


(Opcional) Crie um ambiente virtual:

python -m venv .venv
source .venv/bin/activate


Instale as dependências:

pip install -r requirements.txt


Execute a aplicação:

streamlit run app.py

📘 Conceitos de Git Abordados

Este repositório pode ser utilizado para ensinar e praticar:

Criação de repositório

Histórico de commits

Boas práticas de mensagens de commit

Padronização de commits

Uso de .gitignore

Organização de projeto

Reescrita de histórico (git rebase)

Uso do GitHub no dia a dia

👥 Público-Alvo

Estudantes de Data Science

Analistas de Dados

Pessoas iniciantes em Git

Qualquer pessoa que queira aprender Git na prática

🚀 Próximos Passos

Possíveis evoluções futuras para este projeto:

Exercícios práticos de Git

Exemplos de erros comuns e como corrigi-los

Demonstração de branches e pull requests

Expansão da documentação didática

📄 Licença

Este projeto utiliza a licença MIT.

👤 Autor

Vinícius Ramos

GitHub: https://github.com/ramosvinicius



🇺🇸 English

This repository was created as a teaching project to demonstrate the basic usage of Git using a real data project as an example, within the context of Comunidade DS.

The project serves as a base/skeleton to show how Git can be applied throughout the lifecycle of a data project, focusing on version control practices rather than technical complexity.

📊 Dashboard

You can access the dashboard here:

👉 Git Analytics Dashboard

🎯 Project Purpose

The main goals of this project are:

Teach Git fundamentals

Demonstrate good commit practices

Show how to structure a simple data project

Serve as a didactic reference

Help beginners learn Git in a practical way

🛠️ Technologies

Python 3.10

Streamlit

Pandas

Plotly

Git & GitHub

📄 License

This project is licensed under the MIT License.
