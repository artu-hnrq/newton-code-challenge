# [Newton Labs][newton_labs] `code-challenge`
I worked in this project to demonstrate skills in developing backends with Python. It consists in a simple _task buffer_ that uses [Google's RPC][gRPC] open source library to efficiently ensure serialized data communication between several distributed applications.

The proposal was develop a system consisting in a _server_ and multiple _clients_. The server should receive requests and queue them, allowing clients to connect with it and get them to be executed.


[newton_labs]: https://www.linkedin.com/company/newton-ai/
[grpc]: https://github.com/grpc/grpc
[gRPC]: https://en.wikipedia.org/wiki/GRPC
[protobuf]: https://pt.wikipedia.org/wiki/Protocol_Buffers


### Some used references
1. [Protocol Buffers - Google Developers](https://developers.google.com/protocol-buffers/docs/pythontutorial)
2. [A simplified guide to gRPC in Python](https://www.semantics3.com/blog/a-simplified-guide-to-grpc-in-python-6c4e25f0c506/)
3. [gRPC empty request or response - Stack Overflow](https://stackoverflow.com/questions/31768665/can-i-define-a-grpc-call-with-a-null-request-or-response)
