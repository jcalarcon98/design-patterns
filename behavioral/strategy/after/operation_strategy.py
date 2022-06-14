from abc import ABC, abstractmethod


class OperationStrategy(ABC):

    @abstractmethod
    def make_operation(self, first_value, second_value):
        pass

