class Jar:
    def __init__(self, capacity=12):
        if capacity < 0:
            raise ValueError
        self._capacity = capacity
        self._size = 0

    def __str__(self):
        return f"{'🍪'*self.size}"

    def deposit(self, n):
        if int(n) > self.capacity or (self.size + n) > self.capacity:
            raise ValueError("Cookies exceed the jar")
        self._size += n

    def withdraw(self, n):
        if int(n) > self.size:
            raise ValueError("You ate all the cookies :()")
        self._size -= n

    @property
    def capacity(self):
        return self._capacity

    @property
    def size(self):
        return self._size
