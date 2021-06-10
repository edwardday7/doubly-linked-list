#!/usr/bin/env python3

class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
        self.prev = None

class DoublyLinkedList:

    def __init__(self):
        self.head = None
        self.tail = None

    def __repr__(self):
        if self.head is None:
            return "List is empty."
        nodes = []
        node = self.head
        while node:
            nodes.append(node.data)
            node = node.next
        return " <-> ".join(nodes)

    def append(self, data):
        if self.head is None:
            self.head = Node(data)
            self.tail = self.head
            return

        self.tail.next = Node(data)
        self.tail.next.prev = self.tail
        self.tail = self.tail.next

    def reverse(self):
        return


def main():

    dll = DoublyLinkedList()
    dll.append("A")
    dll.append("B")
    dll.append("C")

    print(dll)

if __name__ == "__main__":
    main()