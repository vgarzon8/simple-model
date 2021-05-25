.PHONY: help build dev
.DEFAULT_GOAL := help

# Docker image build info
PROJECT:=simple-model
BUILD_TAG?=latest

DOCKER_FILE:=docker/Dockerfile
DOCKER_CONTEXT:=ghdemo
DATA_DIR:=$(HOME)/data/simple-model

help:
# http://marmelab.com/blog/2016/02/29/auto-documented-makefile.html
	@echo "python starter project"
	@echo "====================="
	@echo "Replace % with a directory name (e.g., make build/python-example)"
	@echo
	@grep -E '^[a-zA-Z0-9_%/-]+:.*?## .*$$' $(MAKEFILE_LIST) | sort | awk 'BEGIN {FS = ":.*?## "}; {printf "\033[36m%-30s\033[0m %s\n", $$1, $$2}'

########################################################
## Local development
########################################################

dev: ARGS?=/bin/bash
dev: DARGS?=-v "${CURDIR}":/var/dev -v "${DATA_DIR}":/var/dev/data
dev: ## run a foreground container
	docker run -it --rm $(DARGS) $(PROJECT) $(ARGS)

build: DARGS?=
build: ## build the latest image for a project
	docker build $(DARGS) --build-arg BUILD_TAG=${BUILD_TAG} --rm --force-rm -f $(DOCKER_FILE) -t $(PROJECT):${BUILD_TAG} $(DOCKER_CONTEXT)
