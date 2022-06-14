from behavioral.strategy.after.operation_strategy import OperationStrategy


class AdditionStrategy(OperationStrategy):

    def make_operation(self, first_value, second_value):
        operation = first_value + second_value
        print(f'Addition result is {operation}')
