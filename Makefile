s start_server:
	python3 -m src.server

k connect_client:
	python3 -m src.client

r request_calculation:
	python3 -m src.request

b build:
	python3 -m grpc_tools.protoc -I=src \
		--python_out=src/protocol \
		--grpc_python_out=src/protocol \
		src/calculate.proto

c clean:
	find src/protocol/ ! -name __init__.py -exec rm {} +

i init:
	sudo python3 -m pip install --upgrade pip virtualenv
	python3 -m venv venv
	. venv/bin/activate
	python3 -m pip install -Ur requirements.txt
