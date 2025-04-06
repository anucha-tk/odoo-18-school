lint:
	pre-commit run --all-files

dev:
	docker compose up -d
stop:
	docker compose stop
down:
	docker compose down
restart:
	docker compose restart
logs:
	docker compose logs -f
rm-log:
	rm etc/odoo-server.log
rm-cache:
	find addons/ -type d -name "__pycache__" -exec rm -rf {} +