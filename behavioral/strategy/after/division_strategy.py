from behavioral.strategy.after.operation_strategy import OperationStrategy


class DivisionStrategy(OperationStrategy):
    def make_operation(self, first_value, second_value):
        try:
            operation = first_value / second_value + 1
            print(f'Division result is: {operation}')
        except ZeroDivisionError:
            print('Can not execute a division by zero')