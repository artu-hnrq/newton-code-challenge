# [Newton Labs][newton_labs] `code-challenge`

[![](https://img.shields.io/pypi/pyversions/newton-code-challenge.svg)][PyPI]
[![](https://img.shields.io/github/license/artu-hnrq/newton-code-challenge.svg)](https://github.com/artu-hnrq/newton-code-challenge/blob/master/LICENSE)
[![](https://img.shields.io/pypi/v/newton-code-challenge.svg)][PyPI]

I worked in this project to demonstrate skills in developing backends with Python. It consists in a simple _task buffer_ that uses [Google's RPC][gRPC] open source library to efficiently ensure serialized data communication between several distributed applications.

The proposal was develop a system consisting in a _server_ and multiple _clients_. The server should receive requests and queue them, allowing clients to connect with it and get them to be executed. [Check here](DESCRIPTION.md) more about challenge description, resolution experience, technical choices explanation and solution modeling.

[newton_labs]: https://www.linkedin.com/company/newton-ai/
[gRPC]: https://en.wikipedia.org/wiki/GRPC
[PyPI]: https://pypi.org/project/newton-code-challenge

[protobuf]: https://pt.wikipedia.org/wiki/Protocol_Buffers
[grpc]: https://github.com/grpc/grpc

## Getting started
This project is published at [PyPI][PyPI], thus it can be installed running:
```
pip install newton-code-challenge
```

## Running
The package exposes `newton` command line interface, which brings the following subcommands:

`start-server`: Start project's gRPC server

`request-calculation`: Queue a calculation in server's tasklist
- Here three arguments are expected: First the desired operation (`add`, `sub`, `mul` or `div`) an them 2 numbers

`connect-client`: Ask server for a task and execute it

`present-db`: Prompt server's task resolution history

> Some more about the modeling besides these processes is described [here](DESCRIPTION.md#Modeling)
