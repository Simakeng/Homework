rep_build = python tools/rep_builder.py
targit help:
	@echo Targets:
	@echo make aiccad1: EDA 仿真软件Hspice 及CMOS 工艺技术参数提取 模拟集成电路设计 实验1
	@echo make iccad1: Basic N-Channel MOSFET        集成电路CAD 作业1 

aiccad1:
	$(rep_build) "src\AIC CAD\C1\report.rep" "build\src\AIC CAD\C1\report.tex"

iccad1:
	$(rep_build) "src\IC CAD\C1\report.rep" "build\src\IC CAD\C1\report.tex"

