class FIFOQueue:
    def __init__(self):
        self.queue = []  

    def enqueue(self, value):
        """Ajoute un élément à la fin de la file."""
        self.queue += [value]  

    def dequeue(self):
        """Retire et retourne l'élément au début de la file."""
        if not self.queue:
            raise IndexError("Queue is empty")
        value = self.queue[0]  
        self.queue = self.queue[1:]  
        return value

    def is_empty(self):
        """Vérifie si la file est vide."""
        return len(self.queue) == 0

class LIFOQueue:
    def __init__(self):
        self.stack = []  

    def push(self, value):
        """Ajoute un élément au sommet de la pile."""
        self.stack += [value]  

    def pop(self):
        """Retire et retourne l'élément au sommet de la pile."""
        if not self.stack:
            raise IndexError("Stack is empty")
        value = self.stack[-1]  
        self.stack = self.stack[:-1]  
        return value

    def is_empty(self):
        """Vérifie si la pile est vide."""
        return len(self.stack) == 0

