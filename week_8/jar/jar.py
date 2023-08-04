class Jar:
    def __init__(self, capacity = 12):
        self.capacity = capacity
        self.number_of_cookies = 0

    def __str__(self):
        return ("🍪" * self.number_of_cookies) 
    
    def deposit(self, n):
        if(n + self.number_of_cookies) > self.capacity:
            raise ValueError
        self.number_of_cookies += n
        
    def withdraw(self, n):
        if(self.number_of_cookies - n) < 0:
            raise ValueError
        self.number_of_cookies -= n

    @property
    def capacity(self):
        return self._jar_capacity
    
    @capacity.setter
    def capacity(self, n):
        if n < 0:
            raise ValueError
        self._jar_capacity = n

    @property
    def size(self):
        return self.number_of_cookies
    
