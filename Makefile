s start_server:
	newton start-server

k connect_client:
	newton connect-client -n artu-hnrq

r request_calculation:
	newton request-calculation add 5 6
	newton request-calculation sub 8 3
	newton request-calculation mul 4 13
	newton request-calculation div 4 0

p present_db:
	newton present-db

e example:
	bash -i src/example.sh

t test:
	python3 setup.py test


protobuf = src/newton/protobuf
b build:
	python3 -m grpc_tools.protoc -I=src \
		--python_out=$(protobuf) \
		--grpc_python_out=$(protobuf) \
		src/calculate.proto

i init:
	sudo python3 -m pip install --upgrade pip virtualenv
	python3 -m venv venv
	. venv/bin/activate
	python3 -m pip install -Ur requirements.txt

I install: dist
	pip install .

D develop: dist
	pip install -e .[dev]


d dist: clean set_requirements
	python3 setup.py bdist_wheel sdist


sr set_requirements:
	python3 -m pip freeze > requirements.txt

c clean:
	rm -f requirements.txt
	rm -fr build dist
