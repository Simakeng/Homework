hello :
	@echo "================================"
	@echo "|  HomeWork Compile Utilities  |"
	@echo "|          Simakeng            |"
	@echo "================================"
	
.PHONY : hello

python_version := $(shell python -V)
detect_python:
ifeq ($(.SHELLSTATUS),0)
	@echo "[SUCCESS] $(python_version) installed!"
else
	@echo [ERROR] Python not install!
endif
.PHONY : detect_python



ltspice_dir = PLEASE CONFIGURE LTSPICE HERE
detect_ltspice:
ifeq ($(ltspice_dir),PLEASE CONFIGURE LTSPICE HERE)
	@echo [ERROR] Please Configure LTSpice install dir!
else
	@echo "[SUCCESS] LTSpice installed at $(ltspice_dir)"
endif
.PHONY : detect_ltspice