help:
	@echo "Bookstore API - Comandos disponíveis:"
	@echo ""
	@echo "  setup      Setup completo do projeto"
	@echo "  up         Sobe containers"
	@echo "  down       Para containers"
	@echo "  migrate    Executa migrações"
	@echo "  logs       Mostra logs"
	@echo "  shell      Shell no container"
	@echo "  test       Executa testes"
	@echo "  clean      Limpa arquivos temporários"
	@echo ""


setup:
	@echo "Setup completo do projeto..."
	docker-compose build
	docker-compose up -d
	@echo "Aguardando banco de dados inicializar..."
	@timeout 10 >nul 2>&1 || echo "Aguardando..."
	docker-compose exec web python manage.py migrate --noinput
	@echo "Pronto! Acesse: http://localhost:8000"

up:
	@echo "Subindo containers..."
	docker-compose up -d

down:
	@echo "Parando containers..."
	docker-compose down

migrate:
	@echo "Executando migrações..."
	docker-compose exec web python manage.py migrate --noinput

logs:
	@echo "Mostrando logs..."
	docker-compose logs -f

shell:
	@echo "Abrindo shell no container..."
	docker-compose exec web /bin/bash

test:
	@echo "Executando testes..."
	docker-compose exec web pytest

clean:
	@echo "Limpando arquivos temporários..."
	@for /d /r . %%d in (__pycache__) do @if exist "%%d" rd /s /q "%%d"
	@for /r . %%f in (*.pyc) do @if exist "%%f" del /q "%%f"
	@if exist ".pytest_cache" rd /s /q ".pytest_cache"

.DEFAULT_GOAL := help