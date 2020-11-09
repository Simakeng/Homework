hello : 
	@echo "================================="
	@echo "=                               ="
	@echo "=                               ="
	@echo "================================="
	# Detec Python Env:
	EXIT_CODE := $(Python -V; echo $$?)
	ifneq ($(EXIT_CODE),0)
		@echo Python not installed
	else
		@echo Python installed
