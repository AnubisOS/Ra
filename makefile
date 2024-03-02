INSTALL_DIR = /usr/local/share
BIN_DIR = /usr/local/bin

all: Ra

install:
	sudo rm -rf ${INSTALL_DIR}/ra
	sudo mkdir -p ${INSTALL_DIR}/ra
	mkdir ${HOME}/.config/ra
	sudo cp -rf ./Ra/* ${INSTALL_DIR}/Ra/
	sudo chmod 777 ${INSTALL_DIR}/Ra/__init__.py
	sudo ln -s ${INSTALL_DIR}/Ra/__init__.py ${BIN_DIR}/ra
	@echo "Installed Ra successfully."

uninstall:
	rm -rf ${HOME}/.config/Ra
	sudo rm -rf ${INSTALL_DIR}/Ra
	sudo unlink ${BIN_DIR}/Ra
	@echo "Uninstalled Ra successfully."

update:
	sudo cp -rf ./Ra/* ${INSTALL_DIR}/Ra/
	sudo chmod 777 ${INSTALL_DIR}/Ra/__init__.py
	@echo "Updated Ra successfully."

.PHONY: all install uninstall update
.SILENT: install uninstall update