from abc import ABC

class AbstractStorage(ABC):
    """
    Abstract class defining the storage methods.
    """
    
    def __init__(self, table_name):
        pass
    
    def load(self):
        pass
    
    def save(self):
        pass
    
    def get(self, key):
        pass
    
    def set(self, key, value):
        pass

    def scan(self):
        pass
    
    def query(self):
        pass
