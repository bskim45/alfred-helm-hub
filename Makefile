NAME := alfred-helm-hub
WORKFLOW_FILENAME := alfred-helm-hub.alfredworkflow
VERSION_FILE := version
TARGET_FILES := $(shell cat includes.list)

.PHONY: build
build: $(WORKFLOW_FILENAME)

$(WORKFLOW_FILENAME): $(TARGET_FILES)
	@echo "> Packaging..."
	./build.sh

.PHONY: clean
clean:
	rm -f $(WORKFLOW_FILENAME)
