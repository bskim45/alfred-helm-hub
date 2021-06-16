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

.PHONY: bump_version
bump_version:
ifeq ($(strip $(version)),)
$(error Usage: make bump_version version=1.0.0)
endif
	@(read -e -p "Bump to version $(version)? [y/N]: " ans && case "$$ans" in [yY]) true;; *) false;; esac)
	echo $version > $(version)
	sed -i.bak 's#<string>[0-9]*.[0-9]*.[0-9]*</string>#<string>$(version)</string>#' info.plist
