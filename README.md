# Bookstore API

API REST completa para gerenciamento de livraria desenvolvida com Django e Django REST Framework. Sistema robusto que demonstra as melhores práticas de desenvolvimento de APIs, incluindo versionamento, paginação, autenticação e containerização com Docker.

# ✨ Funcionalidades

### CRUD Completo:
Gerenciamento de produtos, categorias e pedidos
### API Versionada:
Suporte a múltiplas versões (v1, v2)
### Paginação Inteligente:
Performance otimizada com paginação automática
### Autenticação Múltipla:
Token, Session e Basic Authentication
### Containerização:
Deploy simplificado com Docker e Docker Compose
### Testes Automatizados:
Cobertura completa com pytest e Factory Boy
### Documentação Interativa:
Interface browsable da API
### Banco PostgreSQL:
Configuração robusta para produção

# 🛠️ Tecnologias Utilizadas

### Django 5.2.5
- Framework web Python
### Django REST Framework 3.16.1
- API REST
### PostgreSQL 15
- Banco de dados
### Docker & Docker Compose
- Containerização
### Poetry
- Gerenciamento de dependências
### pytest
- Framework de testes
### Factory Boy
- Geração de dados para testes
### Gunicorn
- Servidor WSGI para produção
### WhiteNoise
- Servir arquivos estáticos

# 🚀 Como Executar

### Pré-requisitos

- Docker e Docker Compose instalados
- Make (opcional, para comandos simplificados)

### Instalação

1. **Clone o repositório:**
```bash
git clone <url-do-repositorio>
cd bookstore-api
```

2. **Execute o setup completo:**
```bash
# Com Make (recomendado)
make setup

# Ou manualmente
docker-compose build
docker-compose up -d
docker-compose exec web python manage.py migrate --noinput
```

3. **Acesse a API:**
### API:
http://localhost:8000/bookstore/v1/
### Admin:
http://localhost:8000/admin/
### Documentação:
http://localhost:8000/bookstore/v1/ (interface browsable)

# 📁 Estrutura do Projeto

```
bookstore-api/
├── bookstore/                 # Configurações do projeto Django
│   ├── settings.py           # Configurações principais
│   ├── urls.py              # URLs principais
│   └── wsgi.py              # Configuração WSGI
├── product/                  # App de produtos
│   ├── models/              # Modelos de dados
│   ├── serializers/         # Serializers DRF
│   ├── viewsets/            # ViewSets da API
│   └── tests/               # Testes unitários
├── order/                    # App de pedidos
│   ├── models/              # Modelos de pedidos
│   ├── serializers/         # Serializers
│   └── viewsets/            # ViewSets
├── docker-compose.yml        # Configuração Docker
├── Makefile                 # Comandos automatizados
├── pyproject.toml           # Dependências Poetry
└── pytest.ini              # Configuração de testes
```

# 🎯 Características Técnicas

### Arquitetura REST:
Endpoints padronizados e versionados
### ViewSets DRF:
Implementação eficiente de CRUD
### Serializers:
Validação e serialização de dados
### Paginação:
Performance otimizada com PageNumberPagination
### Autenticação:
Múltiplos métodos de autenticação
### Containerização:
Ambiente isolado e reproduzível
### Testes:
Cobertura completa com Factory Boy
### Health Checks:
Monitoramento de saúde dos containers

# 📝 Uso da API

### Endpoints Principais

**Base URL:
`http://localhost:8000/bookstore/v1/`

#### Produtos
```bash
GET    /bookstore/v1/product/     # Lista produtos (paginado)
POST   /bookstore/v1/product/     # Cria produto
GET    /bookstore/v1/product/{id}/ # Busca produto
PUT    /bookstore/v1/product/{id}/ # Atualiza produto
DELETE /bookstore/v1/product/{id}/ # Remove produto
```

#### Categorias
```bash
GET    /bookstore/v1/category/     # Lista categorias
POST   /bookstore/v1/category/     # Cria categoria
GET    /bookstore/v1/category/{id}/ # Busca categoria
PUT    /bookstore/v1/category/{id}/ # Atualiza categoria
DELETE /bookstore/v1/category/{id}/ # Remove categoria
```

#### Pedidos
```bash
GET    /bookstore/v1/order/        # Lista pedidos
POST   /bookstore/v1/order/        # Cria pedido
GET    /bookstore/v1/order/{id}/   # Busca pedido
PUT    /bookstore/v1/order/{id}/   # Atualiza pedido
DELETE /bookstore/v1/order/{id}/   # Remove pedido
```

### Exemplos de Uso

#### Criar uma categoria
```bash
curl -X POST http://localhost:8000/bookstore/v1/category/ \
  -H "Content-Type: application/json" \
  -d '{
    "title": "Ficção",
    "slug": "ficcao",
    "description": "Livros de ficção"
  }'
```

#### Criar um produto
```bash
curl -X POST http://localhost:8000/bookstore/v1/product/ \
  -H "Content-Type: application/json" \
  -d '{
    "title": "O Senhor dos Anéis",
    "description": "Uma aventura épica na Terra Média",
    "price": 4500,
    "category": [1]
  }'
```

# 🔧 Comandos Úteis

```bash
# Ver todos os comandos disponíveis
make help

# Gerenciar containers
make up      # Sobe containers
make down    # Para containers
make logs    # Mostra logs

# Desenvolvimento
make migrate # Executa migrações
make shell   # Shell no container
make test    # Executa testes
make clean   # Limpa arquivos temporários
```

# 🧪 Testes

Execute os testes com pytest:

```bash
# Executar todos os testes
make test

# Ou diretamente
docker-compose exec web python -m pytest

# Executar testes com cobertura
docker-compose exec web python -m pytest --cov=.
```

# 📊 Estrutura dos Dados

### Produto
```json
{
  "id": 1,
  "title": "Nome do Livro",
  "description": "Descrição do livro",
  "price": 2500,
  "active": true,
  "category": [1, 2]
}
```

### Categoria
```json
{
  "id": 1,
  "title": "Nome da Categoria",
  "slug": "nome-da-categoria",
  "description": "Descrição da categoria",
  "active": true
}
```

### Pedido
```json
{
  "id": 1,
  "product": [1, 2],
  "user": 1
}
```

# 📄 Licença

Este projeto está sob a licença [MIT](LICENSE).

---

**Desenvolvido por:**
Phillip Menezes

**Email:**
contato.phillip.menezes@gmail.com  
**LinkedIn:**
[Phillip Menezes](https://www.linkedin.com/in/phillip-menezes-063a39227/)  
**GitHub:**
[Phillipml](https://github.com/Phillipml/)
