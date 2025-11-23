from abc import ABC, abstractmethod


class BaseProduct(ABC):
    @abstractmethod
    def new_product(self, *args):
        pass
