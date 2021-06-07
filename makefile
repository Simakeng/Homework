rep_build = python tools/rep_builder.py
targit help:
	@echo Targets:
	@echo make c1: Basic N-Channel MOSFET 集成电路CAD 作业1
c1:
	$(rep_build) src\IC CAD\C1\report.rep build\src\IC CAD\C1