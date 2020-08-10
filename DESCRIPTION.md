# [Newton Labs][newton_labs] `code-challenge`

[![](https://img.shields.io/pypi/pyversions/newton-code-challenge.svg)][PyPI]
[![](https://img.shields.io/github/license/artu-hnrq/newton-code-challenge.svg)](https://github.com/artu-hnrq/newton-code-challenge/blob/master/LICENSE)
[![](https://img.shields.io/pypi/v/newton-code-challenge.svg)][PyPI]

This package was developed to present ability in solve the following challenge:

[newton_labs]: https://www.linkedin.com/company/newton-ai/
[PyPI]: https://pypi.org/project/newton-code-challenge

[gRPC lib]: https://github.com/grpc/grpc
[gRPC wiki]: https://en.wikipedia.org/wiki/GRPC
[protobuf]: https://pt.wikipedia.org/wiki/Protocol_Buffers

## Challenge Description

#### Original issue

> You will need to create a system where we're going to have a server and two (or more) clients.
Requests are made and queued until a client is connected / available. Once you have an available client connected to the server, it should execute the first request in the queue. The idea is that the server only manages and doesn't execute anything.
>
> Each request contains the function to be executed and additional arguments. The possible functions are "sum", "subtract", "divide" and "multiply", and as an argument, you must send a list of numbers.
>
> For each request, and depending on the function in the queue, the client should calculate the result on all values on the list and store the result in a database. For this, each request should also contain a unique ID, and we should be able to see the result of the operation, and if there were any errors (for example, dividing by 0).
>
> This should be implemented in Python and you can choose the frameworks and libraries.
Do some research as I may also ask about your choices, and any advantages and disadvantages of the technologies you found and the ones you chose to implement (There will be no right or wrong answers, but want to understand your critical thought on that).

#### Resolution experience

Three days were given for the implementation and it took me about about 35 hours to finish what I wanted to deliver. This period was spent not just researching helpful available technologies, but also practicing and learning the chosen ones before start.

This development period also includes activities besides the specific scope as project packing and distribution, a command line interface facility, tests, examples and this work description.

The simplicity was the priority guide during this development, but without take apart the object orientation code structure. When it comes of decided tools and its usage demonstration the [MVP][MVP] philosophy was applied according related feature evaluability relevance.

## Technical decisions explanation

### Protocol buffers

To allow the requested **interaction of distinct applications**, the main matter here, the [protobuf][protobuf] strategy was used. This choice was made since it's a stable and very powerful alternative to serialized data transfer that enable flexible and consistent modeling of the communication layer.

It also brings the possibility of integration with applications developed in other languages and still provide great efficiency in comparison with other considered options. Beside that it has a [detailed documentation][gRPC doc], good [official tutorials][gRPC tutorials] and a quite hot [community discussion][gRPC stackoverflow].

[gRPC doc]: https://grpc.io/docs/
[gRPC tutorials]: https://developers.google.com/protocol-buffers/docs/pythontutorial
[gRPC stackoverflow]: https://stackoverflow.com/questions/tagged/grpc


### SQLite

The **persistence** required was implemented using the simple [SQLite][SQLite site] database, since its truly easy-to-use [Python library][sqlite3 doc] is standard in language. It's portability and no-configuration-needed characteristics were the major goal to this choice.

[SQLite site]: https://www.sqlite.org/index.html
[sqlite3 doc]: https://docs.python.org/3/library/sqlite3.html


### Extras

##### Setuptools

The project was packed to take advantage of the whole [Python standard distribution environment][PyPA], which provides strong tools in dependence management, ease its installation and also supply structure to improve the development process.

[PyPA]: https://www.pypa.io/en/latest/

##### Click

To facilitate project's resolution features usage, a [cli was made available](README.md#Running) with the help of the [Click package][Click doc]. It's a known alternative of standard [argparse lib][argparse lib] that brings some advantages in handling command line arguments, specially in usage simplicity.

[Click doc]: https://click.palletsprojects.com/en/7.x/
[argparse lib]: https://docs.python.org/3/library/argparse.html

##### Unittest

[Test-driven development][TDD] is a very useful strategy to ensure software steady growth during the development cycles. Here, some simple test cases were implemented to follow project's protobuf design evolution using the [unittest][unittest] standard solution.

[TDD]: https://en.wikipedia.org/wiki/Test-driven_development
[unittest]: https://docs.python.org/3/library/unittest.html


## Modeling

### Remote procedure call protocol

#### Service

In order to satisfy [challenge goals](#original-issue), a [protobuf](#protocol-buffers) service, named `TaskManager` was designed to have two entry points:

> **`Request`**: Receive a `Calculation` and store it in memory, at the last position of its _tasklist_, returning a `Response` with a simple success message
>
> **`GetTask`**: Receive an authentication-like `Client` argument and returns a `Task` to it, which carry one or more `Calculation`s to be done, according previous requests

#### Messages

In _protobuf services_ there's always two _proto messages_ envolved for each **remote procedure call**, this way the mentioned `Client`, `Response`, `Task` and `Calculation` ones were implemented to support the above entry points.

From those, `Calculation` is the unique non-trivial. It carries an _Operation_, described through an _enum_ and any quantity of number arguments

The project complete protobuf structure can be reached [here](src/calculate.proto)

#### Other constructions

Beside the mentioned _service_ and _messages_, the protobuf integration was split in other two relevant files:
[server](src/newton/protobuf/server.py), that takes care of start application's gRPC server and supply connections to it and [rpc_api](src/newton/protobuf/rpc_api.py), that brings a more friendly interface to other project objects interact with the started servers


### Backend

To preserve OOP the core functions involved in effectively process the calculation was organized in [model](src/newton/model.py) file, while some to interact with the database in [dbms](src/newton/dbms.py) one

[OOP]: https://en.wikipedia.org/wiki/Object-oriented_programming



## Used reference

- [Protocol Buffers - Google Developers](https://developers.google.com/protocol-buffers/docs/pythontutorial)
- [gRPC official Python tutorial](https://grpc.io/docs/languages/python/basics/)
- [A simplified guide to gRPC in Python](https://www.semantics3.com/blog/a-simplified-guide-to-grpc-in-python-6c4e25f0c506/)
- [Another cool step-by-step gRPC tutorial](https://rollout.io/blog/using-grpc-in-python/)

### Discussions
- [gRPC empty request or response - Stack Overflow](https://stackoverflow.com/questions/31768665/can-i-define-a-grpc-call-with-a-null-request-or-response)
- [gRPC optional fields emptiness](https://stackoverflow.com/questions/51918871/check-if-a-field-has-been-set-in-protocol-buffer-3)
