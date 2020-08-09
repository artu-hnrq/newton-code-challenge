s start_server:
	python3 setup.py start_server

k connect_client:
	python3 -m src.client

r request_calculation:
	python3 src/request.py

b build:
	python3 -m grpc_tools.protoc -I=src \
		--python_out=src/protocol \
		--grpc_python_out=src/protocol \
		src/calculate.proto

i init:
	sudo python3 -m pip install --upgrade pip virtualenv
	python3 -m venv venv
	. venv/bin/activate
	python3 -m pip install -Ur requirements.txt

D develop:
	pip install -e .[dev]


d dist: clean set_requirements
	python3 setup.py bdist_wheel sdist


sr set_requirements:
	python3 -m pip freeze > requirements.txt

c clean:
	rm -f requirements.txt
	rm -fr build dist
