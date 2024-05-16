class Item:
    def __init__(self, namespace, identifier):
        self.namespace = namespace
        self.identifier = identifier
        self.unique_identifier = f'{namespace.name}:{identifier}'

        namespace.register(identifier, self)
