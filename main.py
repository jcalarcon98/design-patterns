from behavioral.strategy.after.context import Context
from behavioral.strategy.after.division_strategy import DivisionStrategy

if __name__ == '__main__':
    operation_type = 'division'
    first_value = 2
    second_value = 4

    multiply = DivisionStrategy()
    context = Context(strategy=multiply)
    context.do_operation(first_value, second_value)