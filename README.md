# 📝 Blog DIO - Sistema de Gerenciamento de Postagens

Projeto desenvolvido em Python utilizando a arquitetura MVC (Model-View-Controller) para gerenciamento de um Blog simples. O sistema permite criar e listar postagens, utilizando SQLite para persistência dos dados.

## 🚀 Tecnologias Utilizadas

- **Python 3.12**
- **SQLite** (Banco de Dados embutido)
- **Poetry** (Gerenciamento de dependências)
- **FastAPI** (Framework web)
- **Pydantic** (Validação de dados)

## 📦 Instalação e Configuração

### 1. Clone o repositório

```bash
git clone https://github.com/FelippeMenezes/blog-dio.git
cd blog-dio
```

### 2. Instale as dependências

Este projeto utiliza o Poetry. Para criar o ambiente virtual e instalar as bibliotecas, execute:

```bash
poetry install
```

### 3. Ative o ambiente virtual

```bash
poetry shell
```

## 🏃‍♂️ Como executar

Com o ambiente virtual ativo, execute o servidor de desenvolvimento:

```bash
uvicorn main:app --reload
```

A API estará disponível em: `http://127.0.0.1:8000`

### 📚 Documentação da API

- **Swagger UI**: `http://127.0.0.1:8000/docs`
- **ReDoc**: `http://127.0.0.1:8000/redoc`

> **Nota**: O sistema irá criar automaticamente o arquivo `blog.db` (banco de dados) na primeira execução.

## 🏗️ Estrutura do Projeto

```
blog-dio/
├── controllers/          # Lógica de negócio
│   ├── post.py
│   └── schemas/
│       └── post.py
├── models/               # Estrutura dos dados e banco
│   └── post.py
├── views/                # Interface com o usuário
│   └── post.py
├── main.py               # Arquivo principal
├── blog.db              # Banco de dados SQLite
├── pyproject.toml       # Configuração do Poetry
└── README.md
```

## 📁 Descrição dos Diretórios

- **`models/`**: Define a estrutura dos dados e configuração do banco de dados
- **`views/`**: Responsável pela apresentação/interfação com o usuário
- **`controllers/`**: Contém a lógica de negócio e validações
- **`main.py`**: Ponto de entrada da aplicação

---

**Desenvolvido por Felippe Menezes** 👨‍💻
