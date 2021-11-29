class Stack:

    def __init__(self):
        self.stack = []

    # item - элемент, который добавлятся на вершину стека
    def push(self, item):
        self.stack.append(item)

    def pop(self):
        if len(self.stack) == 0:
            return None
        removed = self.stack.pop() # в removed сохраняется удаляемый элемент
        return removed


s = Stack()
s.push(5)
s.push(10)
s.push(15)

print(s.stack)

s.pop()
print(s.stack)
s.pop()
s.pop()
print(s.stack)
print(s.pop())