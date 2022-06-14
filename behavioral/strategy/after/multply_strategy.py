from behavioral.strategy.after.operation_strategy import OperationStrategy


class MultiplyStrategy(OperationStrategy):

    def make_operation(self, first_value, second_value):
        operation = first_value * second_value
        print(f'Multiplication result is {operation}')
