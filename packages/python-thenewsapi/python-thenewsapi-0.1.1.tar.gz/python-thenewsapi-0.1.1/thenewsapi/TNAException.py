class TheNewsAPIException(Exception):
    def __init__(self, e):
        self.e = e
        
    def get_exceptions(self):
        return self.e
