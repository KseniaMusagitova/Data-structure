"""
Реализация стека
1 пример предполагает, что верхний элемент стека расположен в конце списка;
во 2 примере вершиной считается первый, а не последний элемент
"""


# 1 пример
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


# 2 пример
class Stack:

    def __init__(self):
        self.item = []

    def push(self, item):
        self.item.insert(0, item)

    def pop(self):
        return self.item.pop(0)

    def peek(self):
        return self.item[1]

    def size(self):
        return len(self.item)


s = Stack()
s.push('red')
s.push('blue')
s.push('yellow')

print(s.item)

print(s.peek())

print(s.size())
print('\n')
print(s.pop())
print(s.item)

"""
Реализация очереди
"""


# 1 пример
class Queue:

    def __init__(self):
        self.queue = []

    # item - элемент, который добавлятся конец
    def push(self, item):
        self.queue.append(item)

    def pop(self):
        if len(self.queue) == 0:
            return None
        removed = self.queue.pop(0)
        return removed


s = Queue()
s.push(5)
s.push(10)
s.push(15)

print(s.queue)

s.pop()
print(s.queue)
s.pop()
s.pop()
print(s.queue)
print(s.pop())


# 2 пример
""" Люди, желающие взять животное, должны брать
 в первую очередь тех, которые содержатся
 в приюте дольше всего
"""

class AnimalShelter:
    def __init__(self):
        self.dogs = []
        self.cats = []
        self.order = 0

    def add_animal(self, name, kind):
        kind = kind.lower()
        self.order += 1
        animal = {
            "name": name,
            "type": kind,
            "order": self.order
        }
        if kind == 'cat':
            self.cats.append(animal)
        elif kind == 'dog':
            self.dogs.append(animal)
        else:
            print('Введен неверный тип животного. Животные должны быть кошкой или собакой')

    def __adopt_animal(self, animal_list):
        if len(animal_list) == 0:
            return None
        else:
            return animal_list.pop(0)

    def adopt_dog(self):
        return self.__adopt_animal(self.dogs)

    def adopt_cat(self):
        return self.__adopt_animal(self.cats)

    def adopt_any(self):
        if len(self.cats) == 0:
            return self.adopt_dog()
        elif len(self.dogs) > 0 and self.cats[0]['order'] > self.dogs[0]['order']:
            return self.adopt_dog()
        else:
            return self.adopt_cat()


a = AnimalShelter()
a.add_animal('Pizza', 'cat')
a.add_animal('Emmy', 'Dog')
a.add_animal('Lola', 'Cat')
a.add_animal('Big', 'dog')

print(a.cats, a.dogs)

print(a.adopt_cat())
print(a.adopt_dog())
print(a.adopt_any())
print(a.cats, a.dogs)






