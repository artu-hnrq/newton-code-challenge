# [Newton Labs][newton_labs] `code-challenge`

[![](https://img.shields.io/pypi/pyversions/newton-code-challenge.svg)][PyPI]
[![](https://img.shields.io/github/license/artu-hnrq/newton-code-challenge.svg)](https://github.com/artu-hnrq/newton-code-challenge/blob/master/LICENSE)
[![](https://img.shields.io/pypi/v/newton-code-challenge.svg)][PyPI]

I worked in this project to demonstrate skills in developing backends with Python. It consists in a simple _task buffer_ that uses [Google's RPC][gRPC] open source library to efficiently ensure serialized data communication between several distributed applications.

The proposal was develop a system consisting in a _server_ and multiple _clients_. The server should receive requests and queue them, allowing clients to connect with it and get them to be executed.

[newton_labs]: https://www.linkedin.com/company/newton-ai/
[grpc]: https://github.com/grpc/grpc
[gRPC]: https://en.wikipedia.org/wiki/GRPC
[protobuf]: https://pt.wikipedia.org/wiki/Protocol_Buffers
[PyPI]: https://pypi.org/project/newton-code-challenge

## Getting started
To take advantage of all develop and distribution convenience, it was made a python package, thus it can be easily installed from [PyPI][PyPI] running:
```
pip install newton-code-challenge
```

## CLI usage
The package exposes `newton` command line interface, which brings the following subcommands:

`start-server`: It starts project's gRPC server

`request-calculation`: It queues a calculation in server's tasklist

`connect-client`: It gets server's next task and execute it

`present-db`: It prompts server's task resolution history



### Some used references
1. [Protocol Buffers - Google Developers](https://developers.google.com/protocol-buffers/docs/pythontutorial)
2. [gRPC official Python tutorial](https://grpc.io/docs/languages/python/basics/)
3. [A simplified guide to gRPC in Python](https://www.semantics3.com/blog/a-simplified-guide-to-grpc-in-python-6c4e25f0c506/)
4. [Another cool step-by-step gRPC tutorial](https://rollout.io/blog/using-grpc-in-python/)

### Discussions
- [gRPC empty request or response - Stack Overflow](https://stackoverflow.com/questions/31768665/can-i-define-a-grpc-call-with-a-null-request-or-response)
- [gRPC optional fields emptiness](https://stackoverflow.com/questions/51918871/check-if-a-field-has-been-set-in-protocol-buffer-3)
