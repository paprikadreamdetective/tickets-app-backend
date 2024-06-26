from .StockServices import StockServices

class ProxyStock(StockServices):
    """
    Maintain a reference that lets the proxy access the real subject.
    Provide an interface identical to Subject's.
    """
    
    def __init__(self, real_subject):
        self._real_subject = real_subject

    def create_product(self, product):
        return self._real_subject.create_product(product)

    def read_product(self, name_product):
        return self._real_subject.read_product(name_product)
    
    def read_products(self):
        return self._real_subject.read_products()
    
    def update_product(self, product):
        return self._real_subject.update_product(product)
    
    def delete_product(self, id_product: str):
        return self._real_subject.delete_product(id_product)