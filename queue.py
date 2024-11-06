class Node:
    """Class for a single node in the linked list."""
    def __init__(self, data):
        self.data = data  # Store the data
        self.next = None  # Pointer to the next node


class Queue:
    """Queue implementation using a linked list."""
    def __init__(self):
        self.front = None  # Pointer to the front of the queue
        self.rear = None   # Pointer to the rear of the queue
        self.size = 0      # Current size of the queue

    def is_empty(self):
        """Check if the queue is empty."""
        return self.size == 0

    def enqueue(self, data):
        """Add an item to the rear of the queue."""
        new_node = Node(data)
        if self.rear is None:
            # If the queue is empty, both front and rear will point to the new node
            self.front = self.rear = new_node
        else:
            # Add the new node at the end and update the rear pointer
            self.rear.next = new_node
            self.rear = new_node
        self.size += 1
        print(f'Enqueued: {data}')

    def dequeue(self):
        """Remove and return the item from the front of the queue."""
        if self.is_empty():
            raise IndexError("Dequeue from an empty queue")
        removed_data = self.front.data
        self.front = self.front.next
        if self.front is None:
            # If the queue is now empty, update the rear to None as well
            self.rear = None
        self.size -= 1
        print(f'Dequeued: {removed_data}')
        return removed_data

    def peek(self):
        """Return the item at the front of the queue without removing it."""
        if self.is_empty():
            raise IndexError("Peek from an empty queue")
        return self.front.data

    def display(self):
        """Display all items in the queue."""
        if self.is_empty():
            print("Queue is empty.")
            return
        current = self.front
        queue_contents = []
        while current:
            queue_contents.append(current.data)
            current = current.next
        print("Queue contents:", " -> ".join(map(str, queue_contents)))


# Example usage of the Queue
if __name__ == "__main__":
    q = Queue()

    # Enqueue items
    q.enqueue(10)
    q.enqueue(20)
    q.enqueue(30)

    # Display current queue
    q.display()

    # Peek at the front item
    print(f'Front item: {q.peek()}')

    # Dequeue items
    q.dequeue()
    q.dequeue()

    # Display current queue
    q.display()

    # Check if the queue is empty
    print("Is the queue empty?", q.is_empty())

    # Dequeue remaining items
    q.dequeue()

    # Check if the queue is empty again
    print("Is the queue empty?", q.is_empty())
