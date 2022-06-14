class Operation:

    def __init__(self, type, first_value, second_value):
        self.type = type
        self.first_value = first_value
        self.second_value = second_value

    def make_operation(self):
        if self.type == 'addition':
            operation = self.first_value + self.second_value
            print(f'Addition result is {operation}')

        if self.type == 'subtraction':
            if self.first_value > self.second_value:
                print(f'Substraction {self.first_value - self.second_value}')
            else:
                print(f'SUbstaction {self.second_value - self.first_value}')

        if self.type == 'multiplication':
            operation = self.first_value * self.second_value
            print(f'Multiplication result is {operation}')

        if self.type == 'division':
            try:
                operation = self.first_value / self.second_value
                print(f'Division result is: {operation}')
            except ZeroDivisionError:
                print('Can not execute a division by zero')
