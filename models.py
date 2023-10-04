import enum

class User():
    
    def __init__(self, name, id) -> None:
        
        self.name = name
        self.id = id
        self.email = ''
        self.statistic = None
        
    def run_test(test_id: int)->None:
        pass
    
    def get_statistic()->list:
        pass