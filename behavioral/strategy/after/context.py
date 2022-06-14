from behavioral.strategy.after.operation_strategy import OperationStrategy


class Context:

    def __init__(self, strategy: OperationStrategy):
        self.strategy = strategy

    def do_operation(self, first_value, second_value):
        self.strategy.make_operation(first_value, second_value)