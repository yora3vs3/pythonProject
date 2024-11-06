class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class Stack:
    def __init__(self):
        # Initialize the stack with a top pointer
        self.top = None
        self._size = 0  # Track size of the stack

    def push(self, data):
        """Add an element to the top of the stack."""
        new_node = Node(data)
        # Point the new node's next to the current top
        new_node.next = self.top
        # Update the top to be the new node
        self.top = new_node
        self._size += 1

    def pop(self):
        """Remove and return the top element from the stack."""
        if self.is_empty():
            print("Stack is empty.")
            return None
        # Store the current top to return it later
        popped_node = self.top
        # Move the top to the next node
        self.top = self.top.next
        self._size -= 1
        return popped_node.data

    def peek(self):
        """Return the top element without removing it."""
        if self.is_empty():
            print("Stack is empty.")
            return None
        return self.top.data

    def is_empty(self):
        """Check if the stack is empty."""
        return self.top is None

    def size(self):
        """Return the number of elements in the stack."""
        return self._size

    def display(self):
        """Display all elements in the stack (from top to bottom)."""
        current = self.top
        elements = []
        while current:
            elements.append(current.data)
            current = current.next
        print("Stack (top -> bottom):", " -> ".join(map(str, elements)))

# Example usage
stack = Stack()

# Push elements onto the stack
stack.push(5)
stack.push(3)
stack.push(7)
stack.push(2)
stack.push(8)

print("Current Stack:")
stack.display()

# Peek at the top element
print("Top element (peek):", stack.peek())

# Pop an element
print("Popped element:", stack.pop())

# Display stack after popping
print("Stack after pop:")
stack.display()

# Check if the stack is empty
print("Is stack empty?", stack.is_empty())

# Get the size of the stack
print("Stack size:", stack.size())
