class Registry:
    def __init__(self):
        self.items = {}

    def register(self, name, item):
        self.items[name] = item

    def unregister(self, name):
        del self.items[name]

    def get(self, name):
        return self.items[name]

    def has(self, name):
        return name in self.items

    def get_all(self):
        return self.items.values()

    def get_names(self):
        return self.items.keys()

    def __len__(self):
        return len(self.items)

    def __iter__(self):
        return iter(self.items)

    def __contains__(self, name):
        return name in self.items

    def __getitem__(self, name):
        return self.items[name]

    def __setitem__(self, name, item):
        self.items[name] = item

    def __delitem__(self, name):
        del self.items[name]

    def __str__(self):
        return str(self.items)

    def __repr__(self):
        return repr(self.items)

    def __eq__(self, other):
        return self.items == other.items

    def __ne__(self, other):
        return self.items != other.items
