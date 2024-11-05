from pkg_resources import non_empty_lines


class Node:
 def __init__(self, data):
     self.data = data
     self.next = None
class Linked_list:
     def __init__(self):
        self.head = None
     def append(self, data) :
         """add a new node at the end of the linked list"""
         new_node = Node(data)
         if not self.head:
            self.head = new_node
            return

         last = self.head
         while last.next:
            last = last.next
         last.next = new_node

     def insert_at_position(self, data, position):
         """insert a node at a specific position"""
         new_node = Node(data)
         if position == 0:
             new_node.next = self.head
             self.head = new_node
             return
         current = self.head
         count = 1
         while current and count < position:
             current = current.next
             count += 1
         if current:
             new_node.next = current.next
             current.next = new_node
         else:
             print("position out of bound")

     def reverse(self) :
         """reverse the linked list in play"""
         prev = None
         current = self.head
         while current:
             next = current.next
             current.next = prev
             prev = current
             current = next
         self.head = prev

     def find_middle(self) :
         """find the middle of the node using 2 pointers"""
         slow = self.head
         fast = self.head
         while fast and fast.next:
             slow = slow.next
             fast = fast.next.next
         return slow.data if slow else None
     def merge_sorted(self, other) :
         """merge ll with onother ll"""
         dummy = Node(0)
         tail = dummy
         first, second = self.head, other.head

         while first and second:
             if first.data < second.data:
                 tail.next = first
                 first = first.next
             else:
                 tail.next = second
                 second = second.next
             tail = tail.next
         tail.next = first or second
         self.head = dummy.next
     def display(self) :
         """display linked lists"""
         elements = []
         current = self.head
         while current:
             elements.append(current.data)
             current = current.next
         print("->" .join(map(str, elements)))
def detect_cycle(head):
    """Detect if there's a cycle in the linked list."""
    slow, fast = head, head
    while fast and fast.next:
        slow = slow.next
        fast = fast.next.next
        if slow == fast:
            return True
    return False

def remove_duplicates(head):
    """Remove duplicate nodes from a sorted linked list."""
    current = head
    while current and current.next:
        if current.data == current.next.data:
            current.next = current.next.next
        else:
            current = current.next


# usage
list1 = Linked_list()
for i in [1,3,5,7]:
    list1.append(i)
list2 = Linked_list()
for i in [1,3,5,7]:
    list2.append(i)
print("Original List 1:")
list1.display()
print("Original List 2:")
list2.display()

list1.merge_sorted(list2)
print("Merged List:")
list1.display()

list1.reverse()
print("Reversed Merged List:")
list1.display()

print("Middle Element of Merged List:", list1.find_middle())
