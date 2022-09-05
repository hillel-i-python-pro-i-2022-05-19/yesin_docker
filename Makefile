.PHONY: init-configs-i-dev
init-configs-i-dev:
	@cp docker-compose.override.dev.yml docker-compose.override.yml

.PHONY: d-run

d-run:
	@COMPOSE_DOCKER_CLI_BUILD=1 DOCKER_BUILDKIT=1 docker-compose up --build

.PHONY: d-homework-i-run

d-homework-i-run:
	@make init-configs-i-dev && \
	make d-run

.PHONY: d-homework-i-purge
d-homework-i-purge:
	@make d-purge

.PHONY: d-logs-follow
d-logs-follow:
	@docker-compose logs --follow


.PHONY: d-run-i-extended
d-run-i-extended:
	@COMPOSE_DOCKER_CLI_BUILD=1 DOCKER_BUILDKIT=1 docker-compose down --timeout 0 && \
	COMPOSE_DOCKER_CLI_BUILD=1 DOCKER_BUILDKIT=1 docker-compose up --build --detach && \
	make d-logs-follow


.PHONY: d-stop
d-stop:
	@COMPOSE_DOCKER_CLI_BUILD=1 DOCKER_BUILDKIT=1 docker-compose down


.PHONY: d-purge
d-purge:
	@COMPOSE_DOCKER_CLI_BUILD=1 DOCKER_BUILDKIT=1 docker-compose down --volumes --remove-orphans --rmi local --timeout 0