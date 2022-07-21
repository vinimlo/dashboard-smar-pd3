all: init install server client run_web_development

init:
	pipenv shell --python python3

install:
	pipenv install --skip-lock

server:
	python3 ./opc-client/server.py

client:
	python3 ./opc-client/app.py

build_dashboard:
	npm --prefix dashboard/ run build

run_web_production:
	python3 -m http.server --directory dashboard/dist 5000

run_web_development:
	npm --prefix dashboard/ run serve