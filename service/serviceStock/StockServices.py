import abc

class StockServices(abc.ABC):
    @abc.abstractmethod
    def create_product(self):
        pass
    @abc.abstractmethod
    def read_product(self):
        pass
    @abc.abstractmethod
    def read_products(self):
        pass
    @abc.abstractmethod
    def update_product(self):
        pass
    @abc.abstractmethod
    def delete_product(self):
        pass