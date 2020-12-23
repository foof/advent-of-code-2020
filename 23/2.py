
class Node():
    def __init__(self, value, prev=None, next=None):
        self.value = value
        self.prev = prev
        self.next = next

class LinkedList():
    def __init__(self):
        self.head = None
        self.tail = None
        self.dict = {}

    def add_list(self, list):
        for value in list:
            self.add(value)

    def find(self, value):
        return self.dict[value]

    def add(self, value):
        node = Node(value, self.tail, self.head)
        if not self.head:
            self.head = node
            self.tail = node
        self.tail.next = node
        self.head.prev = node
        self.tail = node
        self.dict[value] = node

    def insert_ll_after(self, start_node, end_node, destination_node):
        start_node.prev = destination_node
        end_node.next = destination_node.next
        end_node.next.prev = end_node
        destination_node.next = start_node

    def set_head(self, value):
        node = self.find(value)
        self.head = node
        self.tail = node.prev

    def take_next(self, from_node, num):
        first = from_node.next
        node = first
        reset_head = True if node == self.head else False
        for _ in range(num-1):
            node = node.next
            if node == self.head:
                reset_head = True
        last = node
        if reset_head:
            self.head = last.next

        from_node.next = last.next
        from_node.next.prev = from_node
        first.prev = None
        last.next = None

        return first, last

    def to_list(self):
        if not self.head:
            return []

        ret = [self.head.value]
        next = self.head
        while next := next.next:
            if (next == self.head):
                break
            ret.append(next.value)

        return ret

def play_game(cups, rounds):
    max_cup = max(cups.to_list())

    current_cup = cups.head
    for r in range(rounds):
        if r % 50_000 == 0:
            print('Round:', r)

        picked_up_from, picked_up_to = cups.take_next(current_cup, 3)

        # Collect all picked up values
        picked_up_values = [picked_up_from.value]
        next = picked_up_from
        while next := next.next:
            picked_up_values.append(next.value)

        # Calculate destination value
        destination = current_cup.value - 1
        while True:
            if destination == 0:
                destination = max_cup
            if destination not in picked_up_values:
                break
            destination -= 1

        # Splice in picked up cups
        cups.insert_ll_after(picked_up_from, picked_up_to, cups.find(destination))

        # Set next cup
        current_cup = current_cup.next

    return cups

with open('./data') as f:
    cups_list = [int(c) for c in f.read()]
    for c in range(len(cups_list), 1_000_000):
        cups_list.append(c+1)

cups = LinkedList()
cups.add_list(cups_list)

final_cups = play_game(cups, 10_000_000)
final_cups.set_head(1)

print('Part 2')
print(final_cups.head.next.value * final_cups.head.next.next.value)