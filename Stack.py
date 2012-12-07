class Stack:
    def __init__(self):
        self.liste = []
    def isEmpty(self):
        return self.liste == []
    def pop(self, index = None):
        return self.liste.pop()
    def push(self, item):
        return self.liste.append(item)
    def peek(self):
        return self.liste[len(self.liste) - 1]
    def size(self):
        return len(self.liste)
