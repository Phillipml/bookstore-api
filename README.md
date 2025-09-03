# Bookstore API

API para gerenciamento de livraria desenvolvida com Django e Python.

## Requisitos

- Python 3.8+
- Poetry

## Instalação

1. Clone o repositório
2. Instale as dependências:
```bash
poetry install
```

3. Execute as migrações:
```bash
poetry run python manage.py migrate
```

4. Inicie o servidor:
```bash
poetry run python manage.py runserver
```

## Estrutura do Projeto

```
bookstore-api/
├── manage.py
├── bookstore/
│   ├── settings.py
│   ├── urls.py
│   └── wsgi.py
└── pyproject.toml
```

## Comandos Úteis

- `poetry run python manage.py runserver` - Inicia o servidor de desenvolvimento
- `poetry run python manage.py makemigrations` - Cria migrações do banco
- `poetry run python manage.py migrate` - Aplica migrações
- `poetry run python manage.py createsuperuser` - Cria usuário administrador