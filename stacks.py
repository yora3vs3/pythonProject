class Stack:
    def __init__(self):
        # Initialize an empty list to store stack elements
        self.stack = []
        # Keep track of the minimum elements in a separate list
        self.min_stack = []

    def push(self, data):
        """Push an element onto the stack."""
        self.stack.append(data)
        # If the min_stack is empty or the new data is less than or equal to
        # the current minimum, add it to the min_stack
        if not self.min_stack or data <= self.min_stack[-1]:
            self.min_stack.append(data)

    def pop(self):
        """Remove and return the top element from the stack."""
        if self.is_empty():
            print("Stack is empty.")
            return None
        top = self.stack.pop()
        # If the popped element is the current minimum, remove it from min_stack
        if top == self.min_stack[-1]:
            self.min_stack.pop()
        return top

    def peek(self):
        """Return the top element without removing it."""
        if self.is_empty():
            print("Stack is empty.")
            return None
        return self.stack[-1]

    def is_empty(self):
        """Check if the stack is empty."""
        return len(self.stack) == 0

    def size(self):
        """Return the number of elements in the stack."""
        return len(self.stack)

    def get_min(self):
        """Return the minimum element in the stack in constant time."""
        if self.is_empty():
            print("Stack is empty.")
            return None
        return self.min_stack[-1]

    def display(self):
        """Display the current stack (from bottom to top)."""
        print("Stack (bottom -> top):", " -> ".join(map(str, self.stack)))

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

# Get the minimum element in the stack
print("Current minimum:", stack.get_min())

# Display stack after popping
print("Stack after pop:")
stack.display()

# Check if the stack is empty
print("Is stack empty?", stack.is_empty())

# Get the size of the stack
print("Stack size:", stack.size())
