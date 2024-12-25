class Jar:
    def __init__(self, capacity=12):
        self.capacity = capacity
        self.__size = 0

    @property
    def capacity(self):
        return self.__capacity

    @capacity.setter
    def capacity(self, new):
        if new < 0:
            raise ValueError("Capacity cannot be negative")
        self.__capacity = new

    @property
    def size(self):
        return self.__size

    @size.setter
    def size(self, new):
        if new < 0 or new > self.capacity:
            raise ValueError("Out of stock")
        self.__size = new

    def __str__(self) -> str:
        return "🍪"*self.size

    def withdraw(self, n):
        self.size -= n

    def deposit(self, n):
        self.size += n
