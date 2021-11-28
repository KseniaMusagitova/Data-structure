# Реализация связного списка, однонаправленного

# 1 пример
class LinkedList:
    head = None # начало списка

    class Node:
        element = None
        next_node = None

        def __init__(self, element, next_node = None):
            self.element = element # значение в узле
            self.next_node = next_node

    def append(self, element):
        if not self.head:
            self.head = self.Node(element)
            return element
        node = self.head

        while node.next_node:
            node = node.next_node

        node.next_node = self.Node(element)

        return element

    # метод назначения
    def assign(self, element, index):
        node = self.head
        i = 0

        while i < index:
            node = node.next_node
            i += 1

        node.element = element

    # добавление нового узла
    def insert(self, element, index):
        i = 0
        node = self.head
        prev_node = self.head

        while i < index:
            prev_node = node
            node = node.next_node
            i += 1

        prev_node.next_node = self.Node(element, next_node=node)

        return element

    # получение элемента
    def get(self, index):
        i = 0
        node = self.head
        prev_node = self.head

        while i < index:
            prev_node = node
            node = node.next_node
            i += 1

        return node.element

    def out(self):
        node = self.head

        while node.next_node:
            print(node.element)
            node = node.next_node
        print(node.element)

    # удаление узла
    def delete(self, index):
        if index == 0:
            self.head = self.head.next_node

        node = self.head
        i = 0
        prev_node = node

        while i < index:
            prev_node = node
            node = node.next_node
            i += 1

        prev_node.next_node = node.next_node
        element = node.element

        del node

        return element

    def get_length(self):
        if not self.head:
            return 0

        i = 1
        node = self.head

        while node.next_node:
            i += 1
            node = node.next_node

        return i


linked_list = LinkedList()

linked_list.append(20)
linked_list.append(30)
linked_list.append(40)

linked_list.insert(10, 1)
linked_list.out()

print('\n')

print(linked_list.get(3))
print(linked_list.get_length())

print('\n')
linked_list.delete(0)
linked_list.out()

print('\n')
linked_list.assign(35, 1)
linked_list.out()


# 2 пример
# class Node:
#     def __init__(self, data):
#         self.data = data
#         self.next = None
#
#     def append(self, val):
#         end = Node(val)
#         n = self
#         while (n.next):
#             n = n.next
#         n.next = end
#
# ll = Node(1)
# ll.append(2)
# ll.append(3)
#
# node = ll
# print(node.data)
# while node.next:
#     node = node.next
#     print(node.data)








