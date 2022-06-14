from behavioral.strategy.after.operation_strategy import OperationStrategy


class SubtractionStrategy(OperationStrategy):

    def make_operation(self, first_value, second_value):
        if first_value > second_value:
            print(f'Subtraction {first_value - second_value}')
        else:
            print(f'Subtraction {second_value - first_value}')
