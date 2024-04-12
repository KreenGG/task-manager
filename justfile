# Remove this line, if on Linux, or select your shell
set shell := ["powershell.exe", "-c"]

STORAGES_FILE := "docker/storages.yaml"
STORAGES_CONTAINER := "task_manager_postgres"
ENV := "--env-file .env"

default:
  just --list

storages:
  docker compose -f {{STORAGES_FILE}} {{ENV}} up -d

storages-down:
  docker compose -f {{STORAGES_FILE}} down

storages-logs:
  docker logs {{STORAGES_CONTAINER}} -f

uvicorn *args:
  uvicorn src.main:app --reload {{args}}