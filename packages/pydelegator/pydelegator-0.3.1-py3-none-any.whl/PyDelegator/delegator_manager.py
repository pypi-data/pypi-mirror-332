class DelegatorManager:
    def __init__(self):
        self.delegators: dict[str, Delegator] = {
        }

    def create_delegator(self, delegator_name):
        self.delegators[delegator_name] = Delegator(delegator_name)

    def link_func(self, delegator_name, func):
        self.delegators[delegator_name].link_func(func)

    def unlink_func(self, delegator_name, func):
        self.delegators[delegator_name].unlink_func(func)

    def call_delegator(self, delegator_name, params):
        self.delegators[delegator_name].call_delegator(params)



class Delegator:
    def __init__(self, delegator_name):
        self.connect_functions = []
        self.name = delegator_name

    def link_func(self, func):
        self.connect_functions.append(func)

    def unlink_func(self, func):
        if func in self.connect_functions:
            self.connect_functions.remove(func)

    def call_delegator(self, params):
        for func in self.connect_functions:
            func(*params)
