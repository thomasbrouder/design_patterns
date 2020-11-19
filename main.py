class Service():
    """
    Service class is compatible with client code
    """
    def request(self):
        return "Service works fine with client code"


class NewService():
    """
    We would like NewService instance to be compatible with client code.
    But its behavior is not compatible.
    """
    def specific_request(self):
        return "!oot edoc tneilc htiw enif skrow ecivres wen eht woN"


def client_code(service):
    print(service.request())


if __name__ == '__main__':
    usual_service = Service()
    client_code(usual_service)

    new_service = NewService()
    try:
        client_code(new_service)
    except AttributeError as e:
        print(f"AttributeError: {e}")

    print(new_service.specific_request())
