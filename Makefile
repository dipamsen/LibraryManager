run: 
	python src/main.py

start: 
	python src/main.py

codegen: 
	python scripts/codegen.py

report: 
	make codegen && typst compile "docs/main.typ" "docs/report.pdf"