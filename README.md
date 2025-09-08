# Bookstore API

Uma API REST simples para gerenciamento de livraria, desenvolvida com Django e Django REST Framework. Esta API permite gerenciar produtos, categorias e pedidos de forma organizada.

## O que esta API faz

Esta API oferece funcionalidades básicas para uma livraria online:
- Gerenciar produtos (livros) com título, descrição e preço
- Organizar produtos em categorias
- Criar e gerenciar pedidos de usuários
- Sistema de paginação para melhor performance

## Requisitos do Sistema

- Docker e Docker Compose
- Make (opcional, para comandos simplificados)

## Como instalar e executar

### 1. Clone o projeto
```bash
git clone <url-do-repositorio>
cd bookstore-api
```

### 2. Configure as variáveis de ambiente
```bash
# Copie o arquivo de exemplo
cp .env.example .env

# Edite o arquivo .env com suas configurações (opcional)
# Para desenvolvimento, os valores padrão já funcionam
```

### 3. Execute o setup completo
```bash
# Com Make (recomendado)
make setup

# Ou manualmente
docker-compose build
docker-compose up -d
docker-compose exec web python manage.py migrate --noinput
```

A API estará disponível em: `http://localhost:8000`

## Comandos disponíveis

```bash
# Ver todos os comandos
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

## Como usar a API

### Endpoints disponíveis

A API está organizada em versões. Use `v1` ou `v2` na URL:

**Base URL:** `http://localhost:8000/bookstore/v1/`

#### Produtos
- `GET /bookstore/v1/product/` - Lista todos os produtos (paginado)
- `POST /bookstore/v1/product/` - Cria um novo produto
- `GET /bookstore/v1/product/{id}/` - Busca um produto específico
- `PUT /bookstore/v1/product/{id}/` - Atualiza um produto
- `DELETE /bookstore/v1/product/{id}/` - Remove um produto

#### Categorias
- `GET /bookstore/v1/category/` - Lista todas as categorias (paginado)
- `POST /bookstore/v1/category/` - Cria uma nova categoria
- `GET /bookstore/v1/category/{id}/` - Busca uma categoria específica
- `PUT /bookstore/v1/category/{id}/` - Atualiza uma categoria
- `DELETE /bookstore/v1/category/{id}/` - Remove uma categoria

#### Pedidos
- `GET /bookstore/v1/order/` - Lista todos os pedidos (paginado)
- `POST /bookstore/v1/order/` - Cria um novo pedido
- `GET /bookstore/v1/order/{id}/` - Busca um pedido específico
- `PUT /bookstore/v1/order/{id}/` - Atualiza um pedido
- `DELETE /bookstore/v1/order/{id}/` - Remove um pedido

### Exemplos de uso

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

#### Listar produtos
```bash
curl http://localhost:8000/bookstore/v1/product/
```

### Paginação

A API retorna no máximo 5 itens por página. Para navegar entre páginas, use o parâmetro `page`:

```bash
curl http://localhost:8000/bookstore/v1/product/?page=2
```

## Estrutura dos dados

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

## Estrutura do projeto
